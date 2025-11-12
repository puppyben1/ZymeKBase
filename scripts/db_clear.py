# scripts/db_clear.py
from __future__ import annotations
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app, db
try:
    from app.models import NanoEnzyme  # 如果你的模型在 app/models.py
except Exception:
    from models import NanoEnzyme      # 如果在根目录 models.py

def clear_table():
    app = create_app()
    with app.app_context():
        # 仅清空 NanoEnzyme 表
        db.session.query(NanoEnzyme).delete()
        db.session.commit()
        print("[OK] NanoEnzyme table cleared.")

if __name__ == "__main__":
    clear_table()
