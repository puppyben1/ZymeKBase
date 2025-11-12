from __future__ import annotations
from pathlib import Path
from flask import Blueprint, render_template, abort, redirect, url_for, flash
from models import Figure
from config import BASE_DIR

# 兼容你当前结构：若有 exts.py，则优先用；否则回退到 app.py 的 db
try:
    from exts import db   # 推荐结构
except ImportError:
    from app import db     # 兼容你现有结构

bp = Blueprint("figure", __name__)

@bp.route("/<int:fid>")
def detail(fid: int):
    it = db.session.get(Figure, fid)
    if not it:
        abort(404)
    return render_template("figure_detail.html", f=it)

@bp.route("/<int:fid>/delete", methods=["POST"])
def delete(fid: int):
    it = db.session.get(Figure, fid)
    if not it:
        abort(404)

    # 删除磁盘文件（静默容错）
    if it.filename:
        (BASE_DIR / "static" / "uploads" / it.filename).unlink(missing_ok=True)

    # 删库并提交
    db.session.delete(it)
    db.session.commit()
    flash("图片已删除。", "success")
    return redirect(url_for("home.index"))
