(function () {
  const menu = document.querySelector('.menu-button');
  const nav = document.querySelector('.site-nav');
  if (menu && nav) {
    menu.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menu.setAttribute('aria-expanded', String(open));
    });
  }

  const input = document.querySelector('#doc-search');
  const results = document.querySelector('#search-results');
  if (!input || !results) return;
  const root = document.body.dataset.root || '';
  const index = window.__DOC_SEARCH__ || [];

  function closeResults() {
    results.classList.remove('open');
    results.innerHTML = '';
  }

  input.addEventListener('input', () => {
    const query = input.value.trim().toLowerCase();
    if (query.length < 2) return closeResults();
    const matches = index.filter(item =>
      (item.title + ' ' + item.description + ' ' + item.text).toLowerCase().includes(query)
    ).slice(0, 8);
    results.innerHTML = matches.length
      ? matches.map(item => `<a href="${root}${item.url}"><strong>${item.title}</strong><span>${item.description}</span></a>`).join('')
      : '<div class="search-empty">No matching help pages.</div>';
    results.classList.add('open');
  });

  input.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      closeResults();
      input.blur();
    }
  });

  document.addEventListener('click', event => {
    if (!event.target.closest('.site-search')) closeResults();
  });
})();
