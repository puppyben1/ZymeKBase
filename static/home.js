// 动态计数器
async function initCounters() {
  const res = await fetch('/api/stats');
  const s = await res.json();
  const map = {
    models: 'draw_circle1',
    samples: 'draw_circle2',
    unique_samples: 'draw_circle3',
    sources: 'draw_circle4',
    activities: 'draw_circle5'
  };
  for (const [k, id] of Object.entries(map)) {
    const el = document.getElementById(id)?.querySelector('h3');
    if (!el) continue;
    const target = Number(s[k] || 0);
    const start = performance.now();
    const duration = 800; // ms
    function step(t) {
      const p = Math.min(1, (t - start) / duration);
      el.textContent = Math.round(target * p);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
}

// 3D 图
async function initPCA3D() {
  const res = await fetch('/api/pca3d');
  const data = await res.json();
  const trace = {
    type: 'scatter3d',
    mode: 'markers',
    x: data.x, y: data.y, z: data.z,
    text: data.labels || [],
    marker: {
      size: 4,
      opacity: 0.85,
      color: data.color,
      colorbar: { title: 'lgKm' },
      colorscale: 'Plasma' // 与你导出图的色带一致
    },
    hovertemplate: 'PC1=%{x}<br>PC2=%{y}<br>PC3=%{z}<br>lgKm=%{marker.color}<extra></extra>'
  };
  const layout = {
    title: '3D PCA colored by lgKm',
    margin: {l:0,r:0,t:40,b:0},
    scene: {
      xaxis: { title: 'PC1' },
      yaxis: { title: 'PC2' },
      zaxis: { title: 'PC3' }
    }
  };
  Plotly.newPlot('pca3d', [trace], layout, {responsive: true});
}

document.addEventListener('DOMContentLoaded', () => {
  initCounters();
  initPCA3D();
});
