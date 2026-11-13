/* Browser-local presentation of authored demos and a synthetic engineering model. */
(() => {
  'use strict';
  const tabs = [...document.querySelectorAll('[data-tab]')];
  function selectTab(tab) {
    tabs.forEach(item => {
      const active = item === tab;
      item.setAttribute('aria-selected', String(active));
      item.tabIndex = active ? 0 : -1;
      document.getElementById(`panel-${item.dataset.tab}`).hidden = !active;
    });
    const key = tab.dataset.tab;
    history.replaceState(null, '', key === 'demo' ? location.pathname : `#${key}`);
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectTab(tab));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) {
        event.preventDefault();
        tabs[next].focus();
        selectTab(tabs[next]);
      }
    });
  });
  const initial = tabs.find(tab => `#${tab.dataset.tab}` === location.hash);
  if (initial) selectTab(initial);

  const exchanges = [...document.querySelectorAll('[data-exchange]')];
  if (exchanges.length) {
    let visible = 1;
    const next = document.querySelector('[data-demo-next]');
    const back = document.querySelector('[data-demo-back]');
    const all = document.querySelector('[data-demo-all]');
    const reset = document.querySelector('[data-demo-reset]');
    const progress = document.querySelector('.demo-progress');
    function update() {
      exchanges.forEach((exchange, index) => { exchange.hidden = index >= visible; });
      next.disabled = visible === exchanges.length;
      back.disabled = visible === 1;
      all.disabled = visible === exchanges.length;
      progress.textContent = `Exchange ${visible} of ${exchanges.length}`;
    }
    function scrollToCurrent() {
      exchanges[visible - 1].scrollIntoView({block: 'start', behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'});
    }
    next.addEventListener('click', () => { visible = Math.min(visible + 1, exchanges.length); update(); scrollToCurrent(); });
    back.addEventListener('click', () => { visible = Math.max(visible - 1, 1); update(); scrollToCurrent(); });
    all.addEventListener('click', () => { visible = exchanges.length; update(); });
    reset.addEventListener('click', () => { visible = 1; update(); scrollToCurrent(); });
  }

  const thickness = document.getElementById('thickness');
  const ice = document.getElementById('ice');
  if (thickness && ice) {
    function updateModel() {
      const t = Number(thickness.value) / 1000;
      const m = Number(ice.value);
      const mass = 0.4 + 7.5 * t + m;
      const leak = 0.225 / t + 0.5;
      const margin = (334000 * m - 21600 * leak) / 1000;
      const pass = mass <= 1.5 + 1e-12 && margin >= -1e-9;
      document.getElementById('thickness-label').textContent = `${thickness.value} mm`;
      document.getElementById('ice-label').textContent = `${m.toFixed(2)} kg`;
      document.getElementById('result-mass').textContent = `${mass.toFixed(3)} kg`;
      document.getElementById('result-energy').textContent = `${margin >= 0 ? '+' : '−'}${Math.abs(margin).toFixed(1)} kJ`;
      const status = document.getElementById('result-status');
      status.className = `model-status ${pass ? 'pass' : 'fail'}`;
      status.textContent = pass ? 'Passes modeled constraints' : `${mass > 1.5 ? 'Mass limit exceeded' : 'Cooling energy shortfall'}${mass > 1.5 && margin < 0 ? ' and cooling energy shortfall' : ''}`;
    }
    thickness.addEventListener('input', updateModel);
    ice.addEventListener('input', updateModel);
    document.querySelector('[data-model-reset]').addEventListener('click', () => { thickness.value = '30'; ice.value = '0.55'; updateModel(); });
    updateModel();
  }
})();
