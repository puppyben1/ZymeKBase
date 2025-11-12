# ai/predictor.py
from __future__ import annotations
import random

class Predictor:
    def __init__(self):
        pass

    def predict(self, activity: str, mode: str, payload: dict) -> dict:
        # dummy values for now
        base = {"POD": -1.1, "OXD": -0.8, "CAT": -0.3, "SOD": -0.5, "GPx": -0.9}.get(activity, -0.7)
        jitter = (random.random() - 0.5) * 0.2
        pred = base + jitter
        return {
            "activity": activity,
            "mode": mode,
            "pred_mean": round(pred, 3),     # e.g., lgKm
            "pred_lo": round(pred - 0.15, 3),
            "pred_hi": round(pred + 0.15, 3),
            "explain": [
                {"feature": "formula", "effect": 0.12},
                {"feature": "ph", "effect": -0.08},
                {"feature": "temp_c", "effect": 0.05},
            ],
            "echo": payload
        }
