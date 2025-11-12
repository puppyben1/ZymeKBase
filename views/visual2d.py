# views/visual2d.py
from __future__ import annotations

import json
import math
import os
from typing import Dict, List, Optional

import pandas as pd
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, abort
from werkzeug.utils import secure_filename
from sqlalchemy import desc, or_
from sqlalchemy.orm import load_only

from app import db
from models import Viz2D, NanoEnzyme

bp = Blueprint("visual2d", __name__, url_prefix="/visualization/2d")

ALLOWED_EXT = {"png", "jpg", "jpeg", "svg", "pdf"}
MAX_POINTS = 2000
FEATURE_OPTIONS: Dict[str, str] = {
    "temp_c": "Temperature (°C)",
    "ph": "pH",
    "vmax": "Vmax (mM/s)",
}
PALETTE = ["#2563eb", "#9333ea", "#059669", "#f97316", "#dc2626", "#0d9488", "#f59e0b"]


def _plots_dir() -> str:
    d = os.path.join(current_app.static_folder, "plots")
    os.makedirs(d, exist_ok=True)
    return d


def _save_file(file_storage) -> Optional[str]:
    if not file_storage or not getattr(file_storage, "filename", ""):
        return None
    fn = secure_filename(file_storage.filename)
    if "." not in fn:
        return None
    ext = fn.rsplit(".", 1)[1].lower()
    if ext not in ALLOWED_EXT:
        return None
    base, ext2 = os.path.splitext(fn)
    final = f"{base}_{os.urandom(4).hex()}{ext2}"
    out_path = os.path.join(_plots_dir(), final)
    file_storage.save(out_path)
    return final


def _color_for(activity: str | None) -> str:
    key = activity or "Unknown"
    return PALETTE[hash(key) % len(PALETTE)]


def _get_float(args, name: str) -> float | None:
    val = (args.get(name) or "").strip()
    if not val:
        return None
    try:
        return float(val)
    except Exception:
        return None


def _apply_filters(query, args):
    kw = (args.get("q") or "").strip()
    if kw:
        like = f"%{kw}%"
        conds = []
        for column in (NanoEnzyme.formula, NanoEnzyme.activity, NanoEnzyme.notes, NanoEnzyme.substrate):
            conds.append(column.ilike(like))
        query = query.filter(or_(*conds))

    if args.get("activity"):
        query = query.filter(NanoEnzyme.activity == args.get("activity"))

    if args.get("formula"):
        query = query.filter(NanoEnzyme.formula.ilike(f"%{args.get('formula')}%"))

    ph_min = _get_float(args, "ph_min")
    ph_max = _get_float(args, "ph_max")
    if ph_min is not None:
        query = query.filter(NanoEnzyme.ph >= ph_min)
    if ph_max is not None:
        query = query.filter(NanoEnzyme.ph <= ph_max)

    t_min = _get_float(args, "temp_min")
    t_max = _get_float(args, "temp_max")
    if t_min is not None:
        query = query.filter(NanoEnzyme.temp_c >= t_min)
    if t_max is not None:
        query = query.filter(NanoEnzyme.temp_c <= t_max)

    if args.get("has_km"):
        query = query.filter(NanoEnzyme.km.isnot(None))
    if args.get("has_vmax"):
        query = query.filter(NanoEnzyme.vmax.isnot(None))

    return query


def _build_heatmap(rows: List[Dict[str, float]]) -> Dict[str, List[List[float]]]:
    cols = ["km", "vmax", "ph", "temp_c"]
    if not rows:
        return {"cols": cols, "matrix": []}
    df = pd.DataFrame(rows, columns=cols).dropna(how="all")
    if df.empty:
        return {"cols": cols, "matrix": []}
    corr = df.corr().abs().fillna(0)
    ordered = [c for c in cols if c in corr.columns]
    matrix = [[round(float(corr.loc[r, c]), 3) for c in ordered] for r in ordered]
    return {"cols": ordered, "matrix": matrix}


def _prepare_payload(rows, feature_key: str) -> Dict[str, object]:
    scatter = {"x": [], "y": [], "text": [], "color": []}
    violin_map: Dict[str, List[float]] = {}
    heat_rows: List[Dict[str, float]] = []

    for row in rows:
        data_row = {
            "km": row.km,
            "vmax": row.vmax,
            "ph": row.ph,
            "temp_c": row.temp_c,
        }
        if any(value is not None for value in data_row.values()):
            heat_rows.append(data_row)

        log_km = None
        if row.km is not None and row.km > 0:
            log_km = math.log10(row.km)

        feature_val = getattr(row, feature_key, None)
        if log_km is not None and feature_val is not None:
            scatter["x"].append(feature_val)
            scatter["y"].append(log_km)
            hover = f"{row.formula or 'Unknown'} · {row.activity or 'N/A'}"
            if row.doi:
                hover += f"<br>{row.doi}"
            scatter["text"].append(hover)
            scatter["color"].append(_color_for(row.activity))

        if log_km is not None:
            act_key = row.activity or "Unknown"
            violin_map.setdefault(act_key, []).append(log_km)

    heatmap = _build_heatmap(heat_rows)
    violin = [{"activity": act, "values": vals} for act, vals in violin_map.items() if vals]
    return {"scatter": scatter, "heatmap": heatmap, "violin": violin}


@bp.route("/", methods=["GET"])
def list_view():
    args = request.args
    feature = args.get("feature", "temp_c")
    if feature not in FEATURE_OPTIONS:
        feature = "temp_c"

    query = db.session.query(NanoEnzyme)
    query = _apply_filters(query, args)
    total = query.count()
    rows = (
        query.options(
            load_only(
                NanoEnzyme.id,
                NanoEnzyme.formula,
                NanoEnzyme.activity,
                NanoEnzyme.km,
                NanoEnzyme.vmax,
                NanoEnzyme.ph,
                NanoEnzyme.temp_c,
                NanoEnzyme.doi,
            )
        )
        .limit(MAX_POINTS)
        .all()
    )

    payload = _prepare_payload(rows, feature)
    payload.update(
        feature_key=feature,
        feature_label=FEATURE_OPTIONS[feature],
        record_count=len(rows),
        total=total,
        max_points=MAX_POINTS,
    )

    return render_template(
        "visual2d_tool.html",
        selected_feature=feature,
        feature_options=FEATURE_OPTIONS,
        payload_json=json.dumps(payload),
        record_count=len(rows),
        total=total,
        max_points=MAX_POINTS,
    )


@bp.route("/new", methods=["GET", "POST"])
def create_view():
    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        kind = (request.form.get("kind") or "").strip()
        tags = (request.form.get("tags") or "").strip()
        notes = request.form.get("notes") or ""
        config_json = request.form.get("config_json") or ""

        if not title:
            flash("Title is required.", "danger")
            return redirect(url_for("visual2d.create_view"))

        image_filename = None
        if "image" in request.files:
            image_filename = _save_file(request.files["image"])

        obj = Viz2D(
            title=title,
            kind=kind,
            tags=tags,
            notes=notes,
            config_json=config_json,
            image_filename=image_filename,
        )
        db.session.add(obj)
        db.session.commit()
        flash("Created.", "success")
        return redirect(url_for("visual2d.list_view"))

    return render_template("visual2d_form.html", it=None, action="create")


@bp.route("/<int:item_id>", methods=["GET"])
def detail_view(item_id: int):
    it = db.session.get(Viz2D, item_id)
    if not it:
        abort(404)
    return render_template("visual2d_detail.html", it=it)


@bp.route("/<int:item_id>/edit", methods=["GET", "POST"])
def edit_view(item_id: int):
    it = db.session.get(Viz2D, item_id)
    if not it:
        abort(404)
    if request.method == "POST":
        it.title = (request.form.get("title") or it.title).strip()
        it.kind = (request.form.get("kind") or "").strip()
        it.tags = (request.form.get("tags") or "").strip()
        it.notes = request.form.get("notes") or ""
        it.config_json = request.form.get("config_json") or ""

        if "image" in request.files and request.files["image"].filename:
            new_fn = _save_file(request.files["image"])
            if new_fn:
                it.image_filename = new_fn

        db.session.commit()
        flash("Updated.", "success")
        return redirect(url_for("visual2d.detail_view", item_id=it.id))

    return render_template("visual2d_form.html", it=it, action="edit")


@bp.route("/<int:item_id>/delete", methods=["POST"])
def delete_view(item_id: int):
    it = db.session.get(Viz2D, item_id)
    if not it:
        abort(404)
    if it.image_filename:
        try:
            os.remove(os.path.join(_plots_dir(), it.image_filename))
        except Exception:
            pass
    db.session.delete(it)
    db.session.commit()
    flash("Deleted.", "success")
    return redirect(url_for("visual2d.list_view"))
