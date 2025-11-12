# views/offer.py
from __future__ import annotations
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models import UploadRequest  # add model per below

bp = Blueprint("offer", __name__, url_prefix="/offer")

@bp.route("/sample", methods=["GET", "POST"])
def offer_sample():
    if request.method == "POST":
        payload = {
            "formula": request.form.get("formula") or "",
            "activity": request.form.get("activity") or "",
            "ph": request.form.get("ph") or "",
            "temp_c": request.form.get("temp_c") or "",
            "substrate_mM": request.form.get("substrate_mM") or "",
            "catalyst_mg_per_mL": request.form.get("catalyst_mg_per_mL") or "",
            "doi": request.form.get("doi") or "",
            "km": request.form.get("km") or "",
            "vmax": request.form.get("vmax") or "",
        }
        ur = UploadRequest(payload_json=payload, status="pending")
        db.session.add(ur)
        db.session.commit()
        flash("Submitted. Will be reviewed.", "success")
        return redirect(url_for("offer.offer_sample"))
    return render_template("offer_sample.html")
