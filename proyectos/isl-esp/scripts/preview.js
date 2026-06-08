// scripts/preview.js — Hover preview para referencias cruzadas a figuras
// Carga figures-map.json y añade data-preview a los enlaces .quarto-xref

(function() {
  'use strict';

  // Construir ruta base del sitio (para servir el JSON y las imágenes)
  var baseUrl = '';
  var meta = document.querySelector('meta[name="quarto:site-url"]');
  if (meta) {
    baseUrl = meta.getAttribute('content');
    if (!baseUrl.endsWith('/')) baseUrl += '/';
  } else {
    // Fallback: detectar desde la URL actual
    var parts = window.location.pathname.split('/');
    // Subir hasta la raíz del proyecto
    var depth = (window.location.pathname.match(/chapters\//g) || []).length;
    baseUrl = window.location.origin + parts.slice(0, -(depth + 1) || 1).join('/') + '/';
  }

  var jsonUrl = baseUrl + 'figures-map.json';

  fetch(jsonUrl)
    .then(function(r) { return r.json(); })
    .then(function(map) {
      document.querySelectorAll('a.quarto-xref').forEach(function(a) {
        var href = a.getAttribute('href');
        if (!href) return;
        var m = href.match(/#(fig-[\w-]+)/);
        if (!m) return;
        var key = m[1];
        if (!map[key]) return;

        var imgPath = map[key];
        // Resolver ruta baseUrl + imgPath
        var fullUrl = baseUrl + imgPath;
        a.setAttribute('data-preview', '');
        a.style.setProperty('--preview-img', 'url(' + fullUrl + ')');
      });
    })
    .catch(function(err) {
      console.warn('preview.js: no se pudo cargar figures-map.json', err);
    });
})();
