# views/__init__.py
from __future__ import annotations

import importlib
from flask import Flask


def _maybe_register(app: Flask, module: str, url_prefix: str | None = None, bp_name: str = "bp") -> None:
    """
    Try importing ``views.<module>`` and register the defined Blueprint (defaults to attribute ``bp``).
    Missing modules or blueprints are logged as warnings instead of crashing the app.
    """
    try:
        mod = importlib.import_module(f"views.{module}")
        bp = getattr(mod, bp_name)
        if url_prefix:
            app.register_blueprint(bp, url_prefix=url_prefix)
        else:
            app.register_blueprint(bp)
        app.logger.debug("Registered blueprint: %s", module)
    except Exception as exc:
        app.logger.warning("Skip blueprint %s: %s", module, exc)


def init_blueprints(app: Flask) -> None:
    """Register all blueprints needed by the UI layers."""
    candidates: list[tuple[str, str | None]] = [
        ("home", None),
        ("database", "/database"),
        ("visual2d", "/visualization/2d"),
        ("data", "/data"),
        ("upload", "/upload"),
        ("figure", "/figure"),
        ("predict", "/predict"),
        ("assistant", "/assistant"),
        ("offer", "/offer"),
        ("info", "/info"),
    ]
    for module, prefix in candidates:
        _maybe_register(app, module, prefix)
