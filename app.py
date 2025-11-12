# app.py
from __future__ import annotations

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # —— Jinja 过滤器：把科学计数法转为普通小数（保留 nd 位，去尾零） ——
    @app.template_filter("fmt_float")
    def fmt_float(v, nd: int = 6):
        if v is None or v == "":
            return ""
        try:
            s = f"{float(v):.{nd}f}".rstrip("0").rstrip(".")
            return s if s != "-0" else "0"
        except Exception:
            return str(v)

    # 提前导入模型以便 create_all 正确建表
    from models import NanoEnzyme, Figure  # noqa: F401

    # 统一注册蓝图（views/__init__.py 内不再使用全局 app）
    from views import init_blueprints
    init_blueprints(app)

    # 首次启动可确保建表
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
