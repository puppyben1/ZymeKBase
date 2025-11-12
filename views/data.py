from __future__ import annotations
from flask import Blueprint, render_template, request, abort
from app import db
from models import NanoEnzyme

bp = Blueprint("data", __name__)

@bp.route("/")
def list_():
    page = max(int(request.args.get("page", 1)), 1)
    per_page = 20
    q = (request.args.get("q") or "").strip()
    query = db.session.query(NanoEnzyme)
    if q:
        like = f"%{q}%"
        query = query.filter(
            (NanoEnzyme.name.ilike(like)) |
            (NanoEnzyme.substrate.ilike(like)) |
            (NanoEnzyme.notes.ilike(like))
        )
    items = query.order_by(NanoEnzyme.created_at.desc()).offset((page-1)*per_page).limit(per_page).all()
    return render_template("data_list.html", items=items, q=q, page=page, per_page=per_page)

@bp.route("/<int:item_id>")
def detail(item_id: int):
    it = db.session.get(NanoEnzyme, item_id)
    if not it:
        abort(404)
    return render_template("data_detail.html", it=it)
