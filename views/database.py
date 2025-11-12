# views/database.py
from __future__ import annotations

from flask import Blueprint, request, render_template, current_app, abort
from sqlalchemy import or_, func

from app import db
from models import NanoEnzyme

bp = Blueprint("database", __name__, url_prefix="/database")

# ------------ helpers ------------

def _has(col: str) -> bool:
    return hasattr(NanoEnzyme, col)

def _get_float(name: str):
    v = request.args.get(name, "").strip()
    if v == "":
        return None
    try:
        return float(v)
    except Exception:
        return None

def _apply_filters(q):
    a = request.args

    # keyword (name/substrate/notes)
    kw = (a.get("q") or "").strip()
    if kw:
        like = f"%{kw}%"
        conds = []
        for col in ("name", "substrate", "notes"):
            if _has(col):
                conds.append(getattr(NanoEnzyme, col).ilike(like))
        if conds:
            q = q.filter(or_(*conds))

    # activity exact match
    if _has("activity") and a.get("activity"):
        q = q.filter(NanoEnzyme.activity == a.get("activity"))

    # formula substring
    if _has("formula") and a.get("formula"):
        q = q.filter(NanoEnzyme.formula.ilike(f"%{a.get('formula')}%"))

    # pH range
    ph_min = _get_float("ph_min")
    ph_max = _get_float("ph_max")
    if _has("ph"):
        if ph_min is not None:
            q = q.filter(NanoEnzyme.ph >= ph_min)
        if ph_max is not None:
            q = q.filter(NanoEnzyme.ph <= ph_max)

    # temperature range (temp_c)
    t_min = _get_float("temp_min")
    t_max = _get_float("temp_max")
    if _has("temp_c"):
        if t_min is not None:
            q = q.filter(NanoEnzyme.temp_c >= t_min)
        if t_max is not None:
            q = q.filter(NanoEnzyme.temp_c <= t_max)

    # has_km / has_vmax
    if a.get("has_km"):
        q = q.filter(NanoEnzyme.km.isnot(None))
    if a.get("has_vmax"):
        q = q.filter(NanoEnzyme.vmax.isnot(None))

    # extend later: substrate_min/max, catalyst_min ... only if columns exist
    return q

@bp.route("/")
def list_view():
    q = db.session.query(NanoEnzyme)
    q = _apply_filters(q)

    # stats for the current filter (optional)
    total = q.count()

    # fetch rows for table (client-side DataTables will paginate/sort)
    # cap to a reasonable number for initial render
    initial_limit = current_app.config.get("TABLE_INITIAL_LIMIT", 5000)
    items = q.limit(initial_limit).all()

    # column availability flags to control template columns
    flags = dict(
        has_activity=_has("activity"),
        has_formula=_has("formula"),
        has_ph=_has("ph"),
        has_temp=_has("temp_c"),
        has_doi=_has("doi"),
    )

    return render_template("database_list.html", items=items, total=total, flags=flags)


@bp.route("/<int:item_id>")
def detail_view(item_id: int):
    obj = db.session.get(NanoEnzyme, item_id)
    if not obj:
        abort(404)
    return render_template("database_detail.html", it=obj)
