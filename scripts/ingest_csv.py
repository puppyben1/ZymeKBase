# -*- coding: utf-8 -*-
"""
ingest_csv.py —— CSV 导入 & 规范化 & 留痕（按你的表头）
用法：
(.venv) python -m scripts.ingest_csv data/data.csv

说明：
- 导入阶段仅“解析为 float”，不做四舍五入；小数位在前端展示/导出时再控制。
- activity 缺失用 ReactionType 回填；name 优先 formula，空则 Sample-行号。
- provenance（JSON）记录 name 与 activity 的兜底/回填来源。
"""

import sys
import math
import json
import re
import pandas as pd

from app import create_app
from models import db, NanoEnzyme

# —— 默认 CSV 路径（可通过命令行覆盖）
DEFAULT_CSV_PATH = "data/data.csv"

# —— 活性写法统一（常见别名）
ACTIVITY_MAP = {
    "peroxidase": "POD", "pod": "POD", "hrp": "POD", "hrplike": "POD",
    "oxidase": "OXD", "oxd": "OXD",
    "catalase": "CAT", "cat": "CAT",
    "superoxidedismutase": "SOD", "sod": "SOD",
    "gpx": "GPx", "glutathioneperoxidase": "GPx"
}

# —— 你的 CSV 表头 → 数据库字段名的映射（按你提供的首行）
RENAME = {
    # 主键/识别
    "formula": "formula",
    "activity": "activity",
    "ReactionType": "ReactionType",  # 仅用于回填

    # 目标
    "Km, mM": "km",
    "Vmax, mM/s": "vmax",

    # 条件
    "ph": "ph",
    "temp, °C": "temp_c",

    # DOI / 链接
    "link": "doi",

    # 可选属性（先入库但不在主表展示）
    "length, nm": "length_nm",
    "width, nm":  "width_nm",
    "depth, nm":  "depth_nm",
    "SurfaceArea, m^2/g": "SurfaceArea_m2_g",
    "Zpotential": "Zpotential_mV",
    "Mw(coat), g/mol": "Mw_coat_g_per_mol",
    "surface": "surface",
    "surf": "surf",
    "pol": "pol",
    "C min, mM": "C_min_mM",
    "C max, mM": "C_max_mM",
    "C(const), mM": "C_const_mM",
    "Ccat(mg/mL)": "Ccat_mg_per_mL",

    # "Syngony": 若后续需要再加入
    # "#": 序号列，忽略
}

# =========================
# 工具函数
# =========================

def _strip_all_spaces(s: str) -> str:
    """清理前后空白字符（含 \t、NBSP 等）。"""
    if s is None:
        return ""
    s = str(s).replace("\u00A0", " ")
    return s.strip()

def as_float(x):
    """
    宽松解析：空/非法→None；去除空白与千分位逗号；支持科学计数法。
    不做四舍五入，尽可能保留原值（以 float 入库）。
    """
    if x is None:
        return None
    s = _strip_all_spaces(x)
    if s == "":
        return None
    # 去千分位逗号
    s = s.replace(",", "")
    try:
        return float(s)
    except Exception:
        return None

def norm_activity(val, fallback, logs: dict):
    """
    统一活性名称：
      - 优先使用 activity
      - 缺失时用 ReactionType 回填，并记录 provenance
      - 统一映射到 POD/OXD/CAT/SOD/GPx；若未知，保持原大写
    """
    raw = None
    if val is not None and _strip_all_spaces(val) != "":
        raw = str(val)
    elif fallback is not None and _strip_all_spaces(fallback) != "":
        raw = str(fallback)
        logs["activity_filled_from"] = "reactiontype"

    if raw is None:
        return None

    key = re.sub(r"[^a-z]", "", raw.lower())
    return ACTIVITY_MAP.get(key, raw.upper())

# =========================
# 主流程
# =========================

def main(csv_path: str = DEFAULT_CSV_PATH):
    app = create_app()
    with app.app_context():
        # 1) 读取 CSV（保持原始字符串，防止科学计数法被提前转换）
        try:
            df = pd.read_csv(csv_path, dtype=str, encoding="utf-8-sig")
        except UnicodeDecodeError:
            # 兜底：某些编辑器可能写成默认 UTF-8
            df = pd.read_csv(csv_path, dtype=str, encoding="utf-8")

        original_cols = list(df.columns)

        # 2) 列名映射（只映射我们关心的；未映射的保持原样或忽略）
        present_map = {src: dst for src, dst in RENAME.items() if src in df.columns}
        df = df.rename(columns=present_map)

        # 3) 构造 provenance、name、activity
        provenance = []
        names = []
        activities = []

        for idx, row in df.iterrows():
            logs = {}

            # name：优先 formula；为空 → Sample-行号
            formula = _strip_all_spaces(row.get("formula"))
            name = _strip_all_spaces(row.get("name")) if "name" in df.columns else ""
            if not name:
                if formula:
                    name = formula
                    logs["name_fallback"] = "formula"
                else:
                    name = f"Sample-{idx+1}"
                    logs["name_fallback"] = "autoid"
            names.append(name)

            # activity 统一与回填
            act = norm_activity(row.get("activity"), row.get("ReactionType"), logs)
            activities.append(act)

            provenance.append(logs)

        df["name"] = names
        df["activity"] = activities

        # 4) 数值列解析为 float（不四舍五入；展示时再格式化）
        numeric_targets = [
            "km", "vmax",
            "ph", "temp_c",
            "length_nm", "width_nm", "depth_nm",
            "SurfaceArea_m2_g", "Zpotential_mV", "Mw_coat_g_per_mol",
            "C_min_mM", "C_max_mM", "C_const_mM", "Ccat_mg_per_mL",
        ]
        for col in numeric_targets:
            if col in df.columns:
                df[col] = df[col].apply(as_float)

        # 5) DOI 规范化（允许裸 DOI 或完整链接）
        if "doi" in df.columns:
            df["doi"] = df["doi"].fillna("").astype(str).map(_strip_all_spaces)

        # 6) 写入 provenance（JSON）
        df["data_provenance"] = [json.dumps(p, ensure_ascii=False) for p in provenance]

        # 7) 清空并写库（仅写模型中存在的列）
        db.session.query(NanoEnzyme).delete()
        model_cols = [c.name for c in NanoEnzyme.__table__.columns if c.name != "id"]
        to_write_cols = [c for c in model_cols if c in df.columns]
        sub = df[to_write_cols].copy()

        db.session.bulk_insert_mappings(NanoEnzyme, sub.to_dict(orient="records"))
        db.session.commit()

        print(f"[OK] Imported rows: {len(sub)}")

        # 提示未使用的 CSV 列（便于你后续决定是否纳入）
        ignored = []
        for c in original_cols:
            if c in ("#", "Syngony"):
                continue
            mapped = (c in RENAME)  # 我们在映射表里写过
            if mapped:
                # 在映射表里，但你这份 CSV 可能没有该列，或已改名进 df
                continue
            # 不在映射，并且最终也没写进 DB
            # 注意：有些列可能被你手动加进 models.py，这里就会被写入
            if c not in present_map and c not in df.columns:
                ignored.append(c)
        if ignored:
            print("[INFO] Unused CSV columns (ignored):", ignored)

        # 提示：哪些映射列在 CSV 中不存在（方便你补全/检查表头）
        missing_mapped = [src for src in RENAME.keys() if src not in original_cols]
        if missing_mapped:
            print("[INFO] Expected but missing CSV columns:", missing_mapped)


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV_PATH
    main(csv_path)
