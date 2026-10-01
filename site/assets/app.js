/* Gemeinsame Logik aller Spickzettel-Seiten */
(function () {
  var body = document.body, lang = body.dataset.lang || "js";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* Highlighting */
  var HL = {};
  HL["js"] = function () {
  // Syntax-Highlighting
  var RE = new RegExp("(\\/\\/[^\\n]*|\\/\\*[\\s\\S]*?\\*\\/)|(\"(?:[^\"\\\\\\n]|\\\\.)*\"|'(?:[^'\\\\\\n]|\\\\.)*'|`(?:[^`\\\\]|\\\\.)*`)|\\b(const|let|var|function|return|if|else|for|of|in|async|await|new|class|extends|constructor|super|this|throw|try|catch|finally|import|export|default|from|as|true|false|null|undefined|typeof|delete|break|get)\\b", "g");
  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  document.querySelectorAll("pre").forEach(function (pre) {
    var src = pre.textContent, out = "", last = 0, m;
    RE.lastIndex = 0;
    while ((m = RE.exec(src))) {
      out += esc(src.slice(last, m.index));
      var cls = m[1] ? "c" : m[2] ? "s" : "k";
      out += '<span class="' + cls + '">' + esc(m[0]) + "</span>";
      last = RE.lastIndex;
    }
    pre.innerHTML = out + esc(src.slice(last));
  });

  };
  HL["ts"] = function () {
  // Syntax-Highlighting
  var RE = new RegExp("(\\/\\/[^\\n]*|\\/\\*[\\s\\S]*?\\*\\/)|(\"(?:[^\"\\\\\\n]|\\\\.)*\"|'(?:[^'\\\\\\n]|\\\\.)*'|`(?:[^`\\\\]|\\\\.)*`)|\\b(const|let|var|function|return|if|else|for|of|in|async|await|new|class|extends|constructor|super|this|throw|try|catch|finally|import|export|default|from|as|true|false|null|undefined|typeof|delete|break|get|type|interface|keyof|readonly|enum|is|string|number|boolean|void|unknown|any|never|switch|case)\\b", "g");
  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  document.querySelectorAll("pre").forEach(function (pre) {
    var src = pre.textContent, out = "", last = 0, m;
    RE.lastIndex = 0;
    while ((m = RE.exec(src))) {
      out += esc(src.slice(last, m.index));
      var cls = m[1] ? "c" : m[2] ? "s" : "k";
      out += '<span class="' + cls + '">' + esc(m[0]) + "</span>";
      last = RE.lastIndex;
    }
    pre.innerHTML = out + esc(src.slice(last));
  });

  };
  HL["css"] = function () {
  // Syntax-Highlighting für CSS
  var RE = /(\/\*[\s\S]*?\*\/|<!--[\s\S]*?-->|\/\/[^\n]*)|("(?:[^"\\\n]|\\.)*")|(@[a-z-]+)|^([ \t]*)(--[a-z0-9-]+|[a-z-]+)(?=[ \t]*:(?!:)[^{\n]*;)/gm;
  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  document.querySelectorAll("pre").forEach(function (pre) {
    var src = pre.textContent, out = "", last = 0, m;
    RE.lastIndex = 0;
    while ((m = RE.exec(src))) {
      if (m[0] === "") { RE.lastIndex++; continue; }
      out += esc(src.slice(last, m.index));
      if (m[1]) out += '<span class="c">' + esc(m[1]) + "</span>";
      else if (m[2]) out += '<span class="s">' + esc(m[2]) + "</span>";
      else if (m[3]) out += '<span class="k">' + esc(m[3]) + "</span>";
      else out += esc(m[4]) + '<span class="k">' + esc(m[5]) + "</span>";
      last = RE.lastIndex;
    }
    pre.innerHTML = out + esc(src.slice(last));
  });

  };
  HL["html"] = function () {
  // Syntax-Highlighting für HTML
  var RE = /(<!--[\s\S]*?-->|\/\*[\s\S]*?\*\/|\/\/[^\n]*)|("(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')|(<\/?[a-zA-Z][a-zA-Z0-9-]*|<!doctype|<!DOCTYPE)/g;
  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  document.querySelectorAll("pre").forEach(function (pre) {
    var src = pre.textContent, out = "", last = 0, m;
    RE.lastIndex = 0;
    while ((m = RE.exec(src))) {
      out += esc(src.slice(last, m.index));
      var cls = m[1] ? "c" : m[2] ? "s" : "k";
      out += '<span class="' + cls + '">' + esc(m[0]) + "</span>";
      last = RE.lastIndex;
    }
    pre.innerHTML = out + esc(src.slice(last));
  });

  };

  (HL[lang] || HL.js)();

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

  /* Link pro Karte */
  document.querySelectorAll("article.card[id] h3").forEach(function (h) {
    var a = document.createElement("a");
    a.className = "anchor"; a.href = "#" + h.parentElement.closest("article").id;
    a.textContent = "#"; a.setAttribute("aria-label", "Link zu dieser Karte");
    h.appendChild(a);
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

  /* Sprung zu einer Karte per #id */
  function jump() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    if (el.classList.contains("card")) {
      el.scrollIntoView({ block: "start" });
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
  document.querySelectorAll(".demo").forEach(function (box) {
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
})();
