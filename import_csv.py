from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd
from app import create_app, db
from models import NanoEnzyme

def main(path: Path):
    app = create_app()
    with app.app_context():
        df = pd.read_excel(path) if path.suffix.lower() in {'.xlsx', '.xls'} else pd.read_csv(path)
        cols = {c.lower(): c for c in df.columns}
        name_col = cols.get('name') or cols.get('名称')
        if not name_col:
            raise SystemExit("缺少 name/名称 列")
        def pick(*keys):
            for k in keys:
                if k in cols: return cols[k]
            return None
        substrate_col = pick('substrate', '底物')
        km_col = pick('km')
        vmax_col = pick('vmax')
        notes_col = pick('notes', '备注')
        cnt = 0
        for _, row in df.iterrows():
            it = NanoEnzyme(
                name=str(row[name_col]).strip(),
                substrate=str(row[substrate_col]).strip() if substrate_col else "",
                km=float(row[km_col]) if km_col and pd.notna(row[km_col]) else None,
                vmax=float(row[vmax_col]) if vmax_col and pd.notna(row[vmax_col]) else None,
                notes=str(row[notes_col]).strip() if notes_col and pd.notna(row[notes_col]) else "",
            )
            db.session.add(it); cnt += 1
        db.session.commit()
        print(f"OK: 导入 {cnt} 条记录")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python import_csv.py data/sample_data.xlsx")
        raise SystemExit(2)
    main(Path(sys.argv[1]))
