# views/info.py
from __future__ import annotations
import json, os
from flask import Blueprint, render_template, current_app

bp = Blueprint("info", __name__, url_prefix="/info")

@bp.route("/")
def info_home():
    changelog_path = os.path.join(current_app.static_folder, "changelog.json")
    changes = []
    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8") as f:
            changes = json.load(f)
    return render_template("info.html", changes=changes)
