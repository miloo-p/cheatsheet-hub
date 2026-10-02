/*
 * Logik der Zettelseiten: Kopieren, Filter, Erklärungen, Varianten, Menüs, Leiste,
 * Inhaltsverzeichnis, Sprung zu Karten und Live-Demos.
 * Bewusst ohne Framework, die Seiten sind fertiges HTML.
 */
(function () {
  var body = document.body;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* Kopieren-Buttons */
  document.querySelectorAll(".v pre").forEach(function (pre) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "copy"; b.textContent = "Kopieren";
    b.setAttribute("aria-label", "Code kopieren");
    b.addEventListener("click", function () {
      var text = pre.textContent;
      function done(msg) { b.textContent = msg; setTimeout(function () { b.textContent = "Kopieren"; }, 1600); }
      function fallback() {
        var r = document.createRange(); r.selectNodeContents(pre);
        var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
        done("Markiert");
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done("Kopiert"); }, fallback);
      } else fallback();
    });
    pre.parentElement.appendChild(b);
  });

  /* Filter */
  var input = document.getElementById("filter");
  var cards = Array.prototype.slice.call(document.querySelectorAll(".card"));
  var sections = Array.prototype.slice.call(document.querySelectorAll("main section"));
  var empty = document.getElementById("empty");
  if (input) input.addEventListener("input", function () {
    var q = input.value.trim().toLowerCase(), total = 0;
    cards.forEach(function (c) { var hit = !q || c.textContent.toLowerCase().indexOf(q) !== -1; c.hidden = !hit; if (hit) total++; });
    sections.forEach(function (s) { s.hidden = !s.querySelector(".card:not([hidden])"); });
    if (empty) empty.hidden = total > 0;
    if (q) window.scrollTo({ top: document.querySelector("main").offsetTop - 60 });
  });

  /* Alle Erklärungen */
  var tAll = document.getElementById("toggle-all");
  var exps = Array.prototype.slice.call(document.querySelectorAll(".explain"));
  function syncAll() { if (tAll) tAll.textContent = exps.length && exps.every(function (d) { return d.open; }) ? "Alle Erklärungen zuklappen" : "Alle Erklärungen aufklappen"; }
  if (tAll) tAll.addEventListener("click", function () {
    var open = !exps.every(function (d) { return d.open; });
    exps.forEach(function (d) { d.open = open; d.dataset.bulk = "1"; });
    syncAll();
  });
  exps.forEach(function (d) {
    d.addEventListener("toggle", function () {
      syncAll();
      if (d.open && !d.dataset.bulk) {
        var card = d.closest(".card");
        requestAnimationFrame(function () { card.scrollIntoView({ block: "nearest", behavior: reduce ? "auto" : "smooth" }); });
      }
      delete d.dataset.bulk;
    });
  });

  /* Varianten (gilt seitenübergreifend) */
  var modes = { "show-both": "", "show-short": "only-short", "show-long": "only-long" };
  var btns = Object.keys(modes).map(function (id) { return document.getElementById(id); }).filter(Boolean);
  function setMode(id) {
    body.classList.remove("only-short", "only-long");
    if (modes[id]) body.classList.add(modes[id]);
    btns.forEach(function (b) { b.setAttribute("aria-pressed", String(b.id === id)); });
    store("sz-variant", id);
  }
  btns.forEach(function (b) { b.addEventListener("click", function () { setMode(b.id); }); });
  if (btns.length) { var saved = store("sz-variant"); if (saved && modes.hasOwnProperty(saved)) setMode(saved); }

  /* Menüs: schließen bei Klick daneben, Link-Klick oder Escape */
  var menus = Array.prototype.slice.call(document.querySelectorAll("details.menu"));
  document.addEventListener("click", function (e) {
    menus.forEach(function (m) { if (m.open && !m.contains(e.target)) m.open = false; });
  });
  menus.forEach(function (m) {
    m.addEventListener("toggle", function () { if (m.open) menus.forEach(function (o) { if (o !== m) o.open = false; }); });
    m.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { m.open = false; }); });
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") menus.forEach(function (m) { if (m.open) { m.open = false; m.querySelector("summary").focus(); } }); });

  /* Leiste: am Handy beim Runterscrollen ausblenden, Fortschritt, Nach oben */
  var bar = document.getElementById("topbar"), prog = document.getElementById("progress-bar"), totop = document.getElementById("totop");
  var lastY = window.scrollY, ticking = false;
  function onScroll() {
    var y = window.scrollY, max = document.documentElement.scrollHeight - window.innerHeight;
    if (prog) prog.style.width = (max > 0 ? Math.min(100, y / max * 100) : 0) + "%";
    if (bar) {
      var small = window.innerWidth < 760;
      var anyOpen = menus.some(function (m) { return m.open; }) || document.activeElement === input;
      if (small && y > lastY + 4 && y > 160 && !anyOpen) bar.classList.add("hide");
      else if (y < lastY - 4 || y < 160) bar.classList.remove("hide");
    }
    if (totop) totop.hidden = y < window.innerHeight * 1.5;
    lastY = y; ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  if (totop) totop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });
  onScroll();

  /* Inhaltsverzeichnis: aktuelle Karte markieren, gefilterte Karten ausblenden */
  var tocLinks = {};
  document.querySelectorAll(".toc-list li[data-for]").forEach(function (li) {
    (tocLinks[li.dataset.for] = tocLinks[li.dataset.for] || []).push(li);
  });
  var sideToc = document.querySelector("aside.toc");
  var lockUntil = 0;
  function markActive(id, force) {
    if (!force && Date.now() < lockUntil) return;
    document.querySelectorAll('.toc-list a[aria-current="true"]').forEach(function (a) { a.removeAttribute("aria-current"); });
    (tocLinks[id] || []).forEach(function (li) {
      var a = li.querySelector("a"); a.setAttribute("aria-current", "true");
      if (sideToc && sideToc.contains(li) && sideToc.offsetParent !== null) {
        var r = a.getBoundingClientRect(), t = sideToc.getBoundingClientRect();
        if (r.top < t.top + 40 || r.bottom > t.bottom - 40) sideToc.scrollTop += r.top - t.top - t.height / 3;
      }
    });
  }
  if ("IntersectionObserver" in window && cards.length) {
    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) visible[e.target.id] = e.target; else delete visible[e.target.id]; });
      var best = null;
      Object.keys(visible).forEach(function (id) {
        var top = visible[id].getBoundingClientRect().top;
        if (best === null || Math.abs(top - 90) < Math.abs(best.top - 90)) best = { id: id, top: top };
      });
      if (best) markActive(best.id);
    }, { rootMargin: "-70px 0px -55% 0px" });
    cards.forEach(function (c) { if (c.id) io.observe(c); });
  }
  if (input) input.addEventListener("input", function () {
    cards.forEach(function (c) { (tocLinks[c.id] || []).forEach(function (li) { li.hidden = c.hidden; }); });
    document.querySelectorAll(".toc-sec[data-sec]").forEach(function (sec) { sec.hidden = !sec.querySelector("li[data-for]:not([hidden])"); });
  });

  /* Sprung zu einer Karte per #id */
  function jump() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    if (el.classList.contains("card")) {
      el.scrollIntoView({ block: "start" });
      lockUntil = Date.now() + 900; markActive(id, true);
      el.classList.remove("flash"); void el.offsetWidth; el.classList.add("flash");
    }
  }
  window.addEventListener("hashchange", jump);
  if (location.hash) setTimeout(jump, 50);

  /* Live-Demos: Bibliotheken erst beim ersten Klick laden */
  window.loadScripts = function (urls) {
    return urls.reduce(function (p, u) {
      return p.then(function () {
        return new Promise(function (res, rej) {
          if (document.querySelector('script[src="' + u + '"]')) return res();
          var s = document.createElement("script"); s.src = u; s.onload = res;
          s.onerror = function () { rej(new Error("Konnte " + u + " nicht laden")); };
          document.head.appendChild(s);
        });
      });
    }, Promise.resolve());
  };
  var active = {}, loading = null;
  function stop(id) { if (active[id]) { try { active[id](); } catch (e) { console.warn(e); } active[id] = null; } }
  function getDemos() {
    if (window.DEMOS) return Promise.resolve(window.DEMOS);
    if (!window.DEMO_LOADER) return Promise.reject(new Error("Keine Demos auf dieser Seite"));
    if (!loading) loading = window.DEMO_LOADER().then(function (d) { window.DEMOS = d; return d; }, function (e) { loading = null; throw e; });
    return loading;
  }
  document.querySelectorAll(".demo[data-demo]").forEach(function (box) {
    var id = box.dataset.demo, stage = box.querySelector(".stage"), btn = box.querySelector(".run");
    var tpl = box.querySelector("template");
    btn.addEventListener("click", function () {
      var first = !window.DEMOS;
      if (first) { btn.disabled = true; btn.textContent = "Lädt …"; }
      getDemos().then(function (DEMOS) {
        btn.disabled = false;
        var fn = DEMOS[id];
        if (!fn) return;
        if (window.DEMO_SINGLE) Object.keys(active).forEach(function (k) { if (k !== id) stop(k); });
        stop(id);
        stage.innerHTML = tpl ? tpl.innerHTML : "";
        var ret;
        try {
          if (window.gsap && !window.DEMO_SINGLE) {
            var ctx = gsap.context(function () { ret = fn(stage); }, stage);
            active[id] = function () { ctx.revert(); if (typeof ret === "function") ret(); };
          } else {
            ret = fn(stage);
            active[id] = typeof ret === "function" ? ret : null;
          }
        } catch (e) {
          console.error(e);
          stage.innerHTML = '<span class="note">Demo-Fehler: ' + String(e.message || e) + "</span>";
        }
        btn.textContent = "↻ Neu starten";
      }, function (e) {
        btn.disabled = false; btn.textContent = "▶ Abspielen";
        stage.innerHTML = '<span class="note">Bibliothek konnte nicht geladen werden. Bitte später erneut versuchen.</span>';
        console.error(e);
      });
    });
  });

  /* Vorschau: Breite umschalten und auf die Bühne skalieren, Animationen neu starten */
  document.querySelectorAll(".preview").forEach(function (box) {
    var stage = box.querySelector(".stage"), frame = box.querySelector("iframe");
    var sizes = Array.prototype.slice.call(box.querySelectorAll("[data-w]"));
    var replay = box.querySelector(".replay"), width = 0;
    function fit() {
      if (!width) return;
      var scale = Math.min(1, stage.clientWidth / width);
      frame.style.width = width + "px";
      frame.style.height = stage.clientHeight / scale + "px";
      frame.style.transform = scale < 1 ? "scale(" + scale + ")" : "";
    }
    sizes.forEach(function (b) {
      b.addEventListener("click", function () {
        width = Number(b.dataset.w);
        sizes.forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
        fit();
      });
    });
    if (sizes.length) {
      width = Number(sizes[0].dataset.w);
      if ("ResizeObserver" in window) new ResizeObserver(fit).observe(stage);
      fit();
    }
    if (replay) replay.addEventListener("click", function () { frame.srcdoc = frame.srcdoc; });
  });
})();
