from __future__ import annotations
import random
from pathlib import Path
import matplotlib.pyplot as plt
from app import create_app, db
from models import Figure
from config import BASE_DIR

random.seed(42)
UPLOAD_DIR = BASE_DIR / "static" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

TITLES = [
    'Km / Vmax 散点', 'ROC 曲线', '混淆矩阵热图',
    '学习曲线', '超参数响应面', '特征重要性条形图'
]
TAGS = [
    'nanozyme,catboost', 'classification,auc', 'heatmap',
    'learning-curve', 'response-surface', 'feature-importance'
]

def make_scatter(path: Path):
    import numpy as np
    x = np.linspace(0, 10, 200)
    y = np.sin(x) + 0.1 * np.random.randn(200)
    plt.figure()
    plt.plot(x, y)
    plt.title('Demo Scatter')
    plt.xlabel('x'); plt.ylabel('y')
    plt.tight_layout(); plt.savefig(path); plt.close()

def make_bar(path: Path):
    import numpy as np
    vals = np.abs(np.random.randn(10))
    plt.figure()
    plt.bar(range(len(vals)), vals)
    plt.title('Demo Bar')
    plt.tight_layout(); plt.savefig(path); plt.close()

def make_heatmap(path: Path):
    import numpy as np
    m = np.random.rand(10, 10)
    plt.figure()
    plt.imshow(m)
    plt.title('Demo Heatmap')
    plt.colorbar()
    plt.tight_layout(); plt.savefig(path); plt.close()

MAKERS = [make_scatter, make_scatter, make_heatmap, make_scatter, make_heatmap, make_bar]

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        for i in range(6):
            fname = f"demo_{i+1}.png"
            path = UPLOAD_DIR / fname
            MAKERS[i](path)
            fig = Figure(
                title=TITLES[i],
                tags=TAGS[i],
                description='自动生成的示例图',
                filename=fname,
            )
            db.session.add(fig)
        db.session.commit()
        print('OK: 写入 6 张示例图到', UPLOAD_DIR)
