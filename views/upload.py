from __future__ import annotations
from pathlib import Path
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
from models import Figure
from app import db
from config import BASE_DIR

bp = Blueprint("upload", __name__)

UPLOAD_DIR = BASE_DIR / "static" / "uploads"
ALLOWED_EXTS = {".png", ".jpg", ".jpeg", ".gif"}

@bp.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        tags = (request.form.get("tags") or "").strip()
        description = (request.form.get("description") or "").strip()
        file = request.files.get("file")

        if not title:
            flash("标题必填", "error")
            return redirect(url_for("upload.upload"))
        if not file or file.filename == "":
            flash("请选择要上传的图片文件", "error")
            return redirect(url_for("upload.upload"))

        ext = Path(file.filename).suffix.lower()
        if ext not in ALLOWED_EXTS:
            flash("仅支持 png/jpg/jpeg/gif", "error")
            return redirect(url_for("upload.upload"))

        safe_name = secure_filename(Path(file.filename).stem)[:50]
        ts = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
        filename = f"{safe_name}_{ts}{ext}"
        save_path = UPLOAD_DIR / filename
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        file.save(save_path)
        try:
            Image.open(save_path).verify()
        except Exception:
            save_path.unlink(missing_ok=True)
            flash("文件校验失败：不是有效图片", "error")
            return redirect(url_for("upload.upload"))

        fig = Figure(title=title, tags=tags, description=description, filename=filename)
        db.session.add(fig)
        db.session.commit()
        flash("上传成功！", "success")
        return redirect(url_for("data.list_"))

    return render_template("upload.html")

@bp.route("/files/<path:filename>")
def uploaded_file(filename: str):
    return send_from_directory(UPLOAD_DIR, filename)
