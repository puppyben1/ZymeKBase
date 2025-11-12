// Counter animation (runs once when visible)
(function(){
const els = document.querySelectorAll('.stat-num');
if(!('IntersectionObserver' in window) || els.length===0){ return; }
const step = (ts, start, from, to, dur, el) => {
const p = Math.min(1, (ts - start) / dur);
const val = Math.floor(from + (to - from) * p);
el.textContent = val.toLocaleString();
if(p < 1) requestAnimationFrame(t => step(t, start, from, to, dur, el));
};
const io = new IntersectionObserver(entries => {
entries.forEach(e => {
if(e.isIntersecting){
const el = e.target; const to = parseInt(el.getAttribute('data-target')||'0',10);
if(!el.dataset.done){ el.dataset.done = '1'; requestAnimationFrame(t => step(t, t, 0, to, 900, el)); }
io.unobserve(el);
}
});
}, { threshold: 0.7 });
els.forEach(el => io.observe(el));
})();


// Bootstrap tooltips (if any)
(function(){
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
tooltipTriggerList.forEach(el => new bootstrap.Tooltip(el));
})();


// DataTables init if #data-table exists
(function(){
const tbl = document.getElementById('data-table');
if(tbl && window.jQuery){
jQuery(tbl).DataTable({
pageLength: 25,
order: [],
language: { url: 'https://cdn.datatables.net/plug-ins/1.13.8/i18n/en-GB.json' }
});
}
})();


// Theme toggle (light/dark) with localStorage
(function(){
const root = document.body;
const btn = document.getElementById('themeToggle');
const key = 'nz-theme';
const apply = v => root.setAttribute('data-theme', v);
const saved = localStorage.getItem(key);
if(saved){ apply(saved); }
btn && btn.addEventListener('click', () => {
const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
apply(next); localStorage.setItem(key, next);
btn.innerHTML = next === 'dark' ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
});
})();