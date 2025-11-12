# views/home.py
from __future__ import annotations

import os
from typing import List

from flask import Blueprint, current_app, render_template, request, url_for
from sqlalchemy import func, or_, text, desc

from app import db
from models import NanoEnzyme, Figure

bp = Blueprint("home", __name__)


# ---------------------------
# helpers
# ---------------------------

def _count_safe(stmt: text) -> int:
    try:
        return int(db.session.execute(stmt).scalar() or 0)
    except Exception:
        return 0


def _discover_embeds() -> List[str]:
    """
    Scan static/embeds for *.html and return a list sorted by mtime (newest first).
    """
    embeds_dir = os.path.join(current_app.static_folder, "embeds")
    files: List[str] = []
    if os.path.isdir(embeds_dir):
        files = [f for f in os.listdir(embeds_dir) if f.lower().endswith(".html")]
        files.sort(key=lambda f: os.path.getmtime(os.path.join(embeds_dir, f)), reverse=True)
    return files


# ---------------------------
# routes
# ---------------------------

@bp.route("/")
def index():
    # --- search latest nanozyme cards
    q = (request.args.get("q") or "").strip()
    query = db.session.query(NanoEnzyme)

    if q:
        like = f"%{q}%"
        filters = []
        for col in ("name", "substrate", "notes"):
            if hasattr(NanoEnzyme, col):
                filters.append(getattr(NanoEnzyme, col).ilike(like))
        if filters:
            query = query.filter(or_(*filters))

    if hasattr(NanoEnzyme, "created_at"):
        items = query.order_by(desc(NanoEnzyme.created_at)).limit(200).all()
    else:
        items = query.limit(200).all()

    # latest figures
    if hasattr(Figure, "created_at"):
        figures = db.session.query(Figure).order_by(desc(Figure.created_at)).limit(12).all()
    else:
        figures = db.session.query(Figure).limit(12).all()

    # 3D embeds
    plot_embeds = _discover_embeds()

    # --- dynamic stats (robust to missing columns)
    table_name = getattr(NanoEnzyme, "__tablename__", "nanoenzymes")
    column_names = {col.name for col in NanoEnzyme.__table__.columns}

    def has_column(name: str) -> bool:
        return name in column_names

    samples = db.session.query(func.count(NanoEnzyme.id)).scalar() or 0

    # activities (distinct)
    if has_column("activity"):
        activities = db.session.query(func.count(func.distinct(NanoEnzyme.activity))).scalar() or 0
    else:
        activities = 0

    # data sources (distinct DOI, ignore blanks)
    if has_column("doi"):
        data_sources = (
            db.session.query(func.count(func.distinct(NanoEnzyme.doi)))
            .filter(NanoEnzyme.doi.isnot(None))
            .filter(NanoEnzyme.doi != "")
            .scalar()
            or 0
        )
    else:
        data_sources = 0

    # unique samples via DISTINCT formula|surf (or similar), with safe fallbacks
    if has_column("formula") and (has_column("surf") or has_column("surface")):
        surf_col = "surf" if has_column("surf") else "surface"
        expr = f"COALESCE(formula,'') || '|' || COALESCE({surf_col},'')"
        unique = _count_safe(text(f"SELECT COUNT(DISTINCT {expr}) FROM {table_name}"))
    elif has_column("formula"):
        unique = db.session.query(func.count(func.distinct(NanoEnzyme.formula))).scalar() or 0
    elif has_column("name"):
        unique = db.session.query(func.count(func.distinct(NanoEnzyme.name))).scalar() or 0
    else:
        unique = samples

    stats_cards = [
        dict(
            label="Total samples",
            value=samples,
            href=url_for("database.list_view"),
        ),
        dict(
            label="Unique samples",
            value=unique,
            href=url_for("database.list_view"),
        ),
        dict(
            label="Data sources",
            value=data_sources,
            href=url_for("info.info_home"),
        ),
        dict(
            label="Activities",
            value=activities,
            href=url_for("database.list_view"),
        ),
    ]

    stats_snapshot = {card["label"]: card["value"] for card in stats_cards}
    current_app.logger.info("[home] stats=%s | embeds=%d", stats_snapshot, len(plot_embeds))

    return render_template(
        "index.html",
        q=q,
        items=items,
        figures=figures,
        plot_embeds=plot_embeds,
        stats_cards=stats_cards,
    )


@bp.route("/visualizations")
def visualizations():
    """
    Standalone 3D gallery page (templates/visualizations.html).
    """
    plot_embeds = _discover_embeds()
    return render_template("visualizations.html", plot_embeds=plot_embeds)
