# views/predict.py
from __future__ import annotations
from flask import Blueprint, render_template, request, jsonify
from ai.predictor import Predictor  # stub you already have or create per below

bp = Blueprint("predict", __name__, url_prefix="/predict")
_model = Predictor()

@bp.route("/explorative", methods=["GET", "POST"])
def explorative():
    result = None
    if request.method == "POST":
        payload = {
            "activity": request.form.get("activity") or "POD",
            "formula": request.form.get("formula") or "",
            "ph": request.form.get("ph") or "",
            "temp_c": request.form.get("temp_c") or "",
            "size_nm": request.form.get("size_nm") or "",
            "surface_type": request.form.get("surface_type") or "",
        }
        result = _model.predict(activity=payload["activity"], mode="explorative", payload=payload)
    return render_template("predict_explorative.html", result=result)

@bp.route("/detailed", methods=["GET", "POST"])
def detailed():
    return render_template("predict_detailed.html")

@bp.route("/customized", methods=["GET", "POST"])
def customized():
    return render_template("predict_customized.html")

@bp.post("/api/<mode>")
def api_predict(mode: str):
    data = request.json or {}
    activity = data.get("activity", "POD")
    out = _model.predict(activity=activity, mode=mode, payload=data)
    return jsonify(out)
