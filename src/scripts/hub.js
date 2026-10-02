/*
 * Volltextsuche der Startseite. Der Index (search.json) wird erst beim ersten Fokus geladen.
 */
(function () {
  var q = document.getElementById("q"), res = document.getElementById("results");
  if (!q || !res) return;
  var base = q.dataset.base, INDEX = null, loading = null;

  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function load() {
    if (INDEX) return Promise.resolve(INDEX);
    if (!loading) loading = fetch(q.dataset.index).then(function (r) { return r.json(); }).then(function (d) {
      INDEX = d.map(function (e) { e.hay = (e.t + " " + e.d + " " + e.sec + " " + e.st + " " + e.x).toLowerCase(); e.head = (e.t + " " + e.sec).toLowerCase(); return e; });
      return INDEX;
    }, function (e) { loading = null; throw e; });
    return loading;
  }
  function snippet(e, v) {
    var src = e.d + " " + e.x, i = src.toLowerCase().indexOf(v);
    if (i < 0) return esc(e.d);
    var a = Math.max(0, i - 50), b = Math.min(src.length, i + v.length + 70);
    return (a > 0 ? "… " : "") + esc(src.slice(a, i)) + "<mark>" + esc(src.slice(i, i + v.length)) + "</mark>" + esc(src.slice(i + v.length, b)) + (b < src.length ? " …" : "");
  }
  function run() {
    var v = q.value.trim().toLowerCase();
    if (!v) { res.innerHTML = ""; return; }
    load().then(function (idx) {
      if (q.value.trim().toLowerCase() !== v) return;
      var hits = idx.filter(function (e) { return e.hay.indexOf(v) !== -1; });
      hits.sort(function (a, b) { return (b.head.indexOf(v) !== -1) - (a.head.indexOf(v) !== -1); });
      res.innerHTML = hits.length ? hits.slice(0, 15).map(function (h) {
        return '<a href="' + base + h.s + '/#' + esc(h.id) + '"><span class="r-c">' + esc(h.t) + ' <span class="r-p">' + esc(h.st) + ' › ' + esc(h.sec) + '</span></span><span class="r-x">' + snippet(h, v) + '</span></a>';
      }).join("") + (hits.length > 15 ? '<p class="hint">' + (hits.length - 15) + ' weitere Treffer. Präziser suchen grenzt ein.</p>' : "")
      : '<p class="hint">Kein Treffer. Das Thema könnte ein guter nächster Spickzettel sein.</p>';
    }, function () { res.innerHTML = '<p class="hint">Der Suchindex konnte nicht geladen werden.</p>'; });
  }
  q.addEventListener("focus", load, { once: true });
  q.addEventListener("input", run);
})();
