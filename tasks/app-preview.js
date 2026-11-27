(() => {
  // Preserve a 390 × 780 app viewport while fitting the phone into the page.
  document.querySelectorAll('.device-viewport').forEach(viewport => {
    const fit = () => {
      const scale = viewport.getBoundingClientRect().width / 390;
      viewport.style.setProperty('--app-scale', String(scale));
    };
    fit();
    if (typeof ResizeObserver !== 'undefined') {
      new ResizeObserver(fit).observe(viewport);
    } else {
      window.addEventListener('resize', fit);
    }
  });
})();
