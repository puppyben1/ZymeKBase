# nanozyme-lite (Python 3.12 兼容)

- Flask + SQLite
- NanoEnzyme 表（搜索/详情/导入）
- 图片上传与展示
- 预测演示 stub（可替换成真实模型）
- 无 Marshmallow / Flask-Migrate，避免版本牵连

## 运行
```powershell
cd nanozyme-lite-py312
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python init_db.py
python import_csv.py data/sample_data.xlsx
python make_demo_charts.py
python app.py
```
