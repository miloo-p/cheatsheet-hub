"""Baut die Spickzettel-Website als EIN Artifact.

Ablauf:
  1. Die Einzelseiten werden wie bisher aus den *_data.py gebaut (build_core, build_gsap,
     build_three, build_cro). Der JavaScript-Zettel ist handgeschrieben (js-spickzettel.html).
  2. Dieses Skript übernimmt daraus Kopf, Abschnitte, Karten und Demos und erzeugt:
       site/index.html            Hub (Startseite des Artifacts, ohne eigenes <html>-Gerüst)
       site/<key>.html            eine vollständige Seite pro Zettel
       site/assets/app.css        gemeinsame Gestaltung
       site/assets/app.js         gemeinsame Logik (Highlighting, Filter, Menüs, Demos, Kopieren)
       site/assets/search.json    Suchindex für den Hub
  Neuen Zettel hinzufügen: Einzelseite bauen, Eintrag in SHEETS ergänzen, Skript ausführen.
"""
import html, json, re, pathlib, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import sheetgen

SITE = HERE / "site"
(SITE / "assets").mkdir(parents=True, exist_ok=True)

CATEGORIES = [
    ("grundlagen", "Web-Grundlagen", "Die vier Sprachen des Webs, in Lernreihenfolge. Jede Karte zeigt eine kurze und eine ausführliche Schreibweise."),
    ("animation", "Animation & 3D", "Bewegung und Raum im Browser. Mit Live-Demos auf fast jeder Karte, direkt zum Ausprobieren."),
    ("produkt", "Produkt & Wirkung", "Was Besucher zu Kunden macht, aus Entwicklersicht: messen, testen, schneller werden und rechtlich sauber bleiben."),
]

# key, Kategorie, Titel, Datei der Einzelseite, Sprache fürs Highlighting, Badge, Niveau, Kurztext, alte Artifact-ID, Farben
SHEETS = [
    dict(key="html", cat="grundlagen", title="HTML", src="html-spickzettel.html", lang="html", badge="HTML", level="Basis",
         old="YPbjHyWZpJ8tEecBdsXRob",
         blurb="Das Fundament: Semantik, Bilder, Formulare fürs Backend, native Dialoge und Barrierefreiheit.",
         c=("#a8326a", "#f8e2ec", "#4b52a8", "#e6e7f7", "#f39ac0", "#3a1d2a", "#aeb2f5", "#22243f", "#f39ac0")),
    dict(key="css", cat="grundlagen", title="CSS", src="css-spickzettel.html", lang="css", badge="CSS", level="Basis",
         old="9i6icDS2mpDmQm3j3fzdpT",
         blurb="Layout und Gestaltung: Box Model, Selektoren, Flexbox, Grid, Positionierung, Responsive Design und Animation.",
         c=("#177258", "#dcf1e9", "#a8452a", "#f8e6df", "#6fd3ad", "#15302a", "#f0a487", "#36221c", "#6fd3ad")),
    dict(key="js", cat="grundlagen", title="JavaScript", src="js-spickzettel.html", lang="js", badge="JS", level="Basis",
         old="EgkjrRmDocu7CAwqekbRN7",
         blurb="Die Sprache selbst: Arrays, Objekte, Funktionen, Asynchronität und typische Frontend-Muster.",
         c=("#9a6f00", "#fbf1d3", "#2f6f8f", "#e1eef5", "#f0c35a", "#2e2a1c", "#8cc7e6", "#1b2b38", "#f0c35a")),
    dict(key="ts", cat="grundlagen", title="TypeScript", src="ts-spickzettel.html", lang="ts", badge="TS", level="Aufbauend auf JavaScript",
         old="W9b8p3sj4TGiwhcaTx8DLW",
         blurb="Typen für Frontend und Backend: Unions, Generics, Utility Types, API-Daten, React und Express.",
         c=("#2b5fae", "#e2eaf7", "#7a3f97", "#f2e7f7", "#8db4f2", "#1b2740", "#d3a3ec", "#2b1f35", "#8db4f2")),
    dict(key="gsap", cat="animation", title="GSAP", src="gsap-spickzettel.html", lang="js", badge="GSAP", level="Aufbauend auf CSS und JavaScript",
         old="DVpdoSZy1Zrmuy21bkjg4a",
         blurb="Animationen mit GSAP 3.15: Tweens, Timelines, ScrollTrigger, Flip, SplitText und React. Jeweils im Vergleich mit CSS und Web Animations API.",
         c=("#3d7a12", "#e4f2d6", "#7a5a17", "#f3ead6", "#9be15d", "#1f2e14", "#e2c27a", "#2f2716", "#9be15d")),
    dict(key="three", cat="animation", title="Three.js", src="three-spickzettel.html", lang="js", badge="3D", level="Aufbauend auf JavaScript",
         old="VyafP1kRKSM7o16WBGaAgL",
         blurb="3D im Browser mit Three.js r186: Szene und Render-Loop, Licht und Schatten, Interaktion, Performance und React Three Fiber.",
         c=("#2563c9", "#e1eafa", "#8a4b14", "#f6e8da", "#7fb0ff", "#17243d", "#f0b07a", "#33241a", "#7fb0ff")),
    dict(key="cro", cat="produkt", title="Conversion-Optimierung", src="cro-spickzettel.html", lang="html", badge="CRO", level="Aufbauend auf HTML und JavaScript",
         old="Qop5DCJN4ZFtwtX83EXoXT",
         blurb="Tracking, A/B-Tests, Formulare, Core Web Vitals und Rechtspflichten in Deutschland, als Vorher/Nachher mit Messhinweisen. Plus Lesestoff aus Marketing-Sicht.",
         c=("#0f7a5c", "#d9f2ea", "#5b55a8", "#e8e6f7", "#5fd3ae", "#143029", "#b3adf2", "#24223d", "#5fd3ae")),
]
HUB_OLD = "8MMr1HXJMFnYe4ubTYDY4x"

PLANNED = [
    ("Node & Express", "Routing, Middleware, Fehlerbehandlung, Umgebungsvariablen"),
    ("SQL & Datenbanken", "SELECT, JOIN, Relationen, Migrations, ORM-Grundlagen"),
    ("React Hooks", "useEffect im Detail, useRef, useContext, eigene Hooks"),
    ("Git", "Branches, Merge vs. Rebase, Konflikte lösen, Pull Requests"),
]

OLD2KEY = {s["old"]: s["key"] for s in SHEETS}

def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()

def relink(s):
    """Artifact-Links auf andere Zettel werden zu relativen Links im selben Tab."""
    def rep(m):
        aid, frag = m.group(1), m.group(2) or ""
        target = "index.html" if aid == HUB_OLD else (OLD2KEY.get(aid, "") + ".html")
        return f'href="{target}{frag}"'
    s = re.sub(r'href="https://claude\.ai/artifact/([A-Za-z0-9]+)(#[A-Za-z0-9_-]+)?"\s*target="_blank"\s*rel="noopener"', rep, s)
    s = re.sub(r'href="https://claude\.ai/artifact/([A-Za-z0-9]+)(#[A-Za-z0-9_-]+)?"', rep, s)
    return s

def extract(sheet):
    s = (HERE / sheet["src"]).read_text()
    g = lambda pat, default="": (re.search(pat, s, re.S).group(1) if re.search(pat, s, re.S) else default)
    part = dict(
        h1=g(r"<h1>(.*?)</h1>"),
        eyebrow=g(r'<div class="eyebrow">.*?</a> · (.*?)</div>'),
        lede=g(r'<p class="lede">(.*?)\s*<div class="legend">'),
        legend=g(r'<div class="legend">(.*?)</div>\s*</header>'),
        placeholder=html.unescape(g(r'id="filter" type="search" placeholder="(.*?)"')),
        has_long='<div class="seg" role="group"' in s,
        short_lbl=strip_tags(g(r'id="show-short"[^>]*>(.*?)</button>')),
        long_lbl=strip_tags(g(r'id="show-long"[^>]*>(.*?)</button>')),
        infobox=g(r'<aside class="infobox" id="mehr">(.*?)</aside>'),
        footer=g(r"<footer>(.*?)</footer>"),
    )
    start = s.index("<section id=")
    end = min(i for i in [s.find('<aside class="infobox"'), s.find('<p class="empty"')] if i > 0)
    secs = s[start:end].rstrip()
    # IDs, Kartenrumpf, Links
    out, n = [], 0
    for m in re.finditer(r'(<section id="([^"]+)">)(.*?)(</section>)', secs, re.S):
        sid, body = m.group(2), m.group(3)
        i = 0
        def art(mm):
            nonlocal i
            i += 1
            return f'<article class="card" id="{sheet["key"]}-{sid}-{i}">'
        body = re.sub(r'<article class="card">', art, body)
        body = re.sub(r'(<article class="card" id="[^"]+">)(.*?)(\s*<details class="explain">)',
                      lambda mm: mm.group(1) + '\n        <div class="card-main">' + mm.group(2) + '\n        </div>' + mm.group(3), body, flags=re.S)
        n += i
        out.append(m.group(1) + body + m.group(4))
    part["sections"] = relink("\n\n  ".join(out))
    part["footer"] = relink(part["footer"])
    part["lede"] = relink(part["lede"])
    part["nav"] = re.findall(r'<section id="([^"]+)">\s*<h2>(.*?) <span', secs, re.S)
    part["count"] = n
    # Demos
    loader = ""
    if sheet["key"] == "gsap":
        libs = re.findall(r'<script src="(https://cdnjs[^"]+)"></script>', s)
        body = re.search(r'var DEMOS = window\.DEMOS = \{\};\n(.*?)\n</script>', s, re.S).group(1)
        loader = ("<script>\nwindow.DEMO_LOADER = async function () {\n  await loadScripts(" + json.dumps(libs) + ");\n"
                  "  gsap.registerPlugin(ScrollTrigger, Flip, SplitText);\n  var DEMOS = {};\n" + body + "\n  return DEMOS;\n};\n</script>")
    elif sheet["key"] == "three":
        importmap = re.search(r'(<script type="importmap">.*?</script>)', s, re.S).group(1)
        gsaplib = re.search(r'<script src="(https://cdnjs[^"]+gsap\.min\.js)"></script>', s).group(1)
        mod = re.search(r'<script type="module">\n(.*?)</script>', s, re.S).group(1)
        mod = mod.replace('import * as THREE from "three";\n', "").replace('import { OrbitControls } from "three/addons/controls/OrbitControls.js";\n', "")
        mod = mod.replace("window.DEMO_SINGLE = true;\n", "").replace("const DEMOS = window.DEMOS = {};", "const DEMOS = {};")
        loader = (importmap + "\n<script>\nwindow.DEMO_SINGLE = true;\nwindow.DEMO_LOADER = async function () {\n"
                  "  const THREE = await import(\"three\");\n  const { OrbitControls } = await import(\"three/addons/controls/OrbitControls.js\");\n"
                  f"  await loadScripts([{json.dumps(gsaplib)}]);\n" + mod + "\n  return DEMOS;\n};\n</script>")
    part["loader"] = relink(loader)
    return part

# ---------------------------------------------------------------- CSS
def build_css():
    colors = []
    for sh in SHEETS:
        a, as_, l, ls, ad, asd, ld, lsd, kw = sh["c"]
        k = sh["key"]
        colors.append(f'body[data-sheet="{k}"] {{ --accent: {a}; --accent-soft: {as_}; --long: {l}; --long-soft: {ls}; --code-kw: {kw}; }}')
        colors.append(f'@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) body[data-sheet="{k}"] {{ --accent: {ad}; --accent-soft: {asd}; --long: {ld}; --long-soft: {lsd}; }} }}')
        colors.append(f':root[data-theme="dark"] body[data-sheet="{k}"] {{ --accent: {ad}; --accent-soft: {asd}; --long: {ld}; --long-soft: {lsd}; }}')
    cro = """
body[data-sheet="cro"] .short .lbl { color: var(--warn); background: var(--warn-soft); }
body[data-sheet="cro"] .short pre { border-left-color: var(--warn); }
body[data-sheet="cro"] .long .lbl { color: var(--accent); background: var(--accent-soft); }
body[data-sheet="cro"] .long pre { border-left-color: var(--accent); }
.disclaimer { font-size: 13px; color: var(--muted); border-left: 3px solid var(--line); padding-left: 10px; max-width: 70ch; margin: 0; }
"""
    ui = """
/* ---------- Grundgerüst für Unterseiten ---------- */
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; }
img { max-width: 100%; }
[hidden] { display: none !important; }
:root { padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }

/* ---------- Kompakte Leiste ---------- */
.topbar { display: block; margin: 0; position: sticky; top: env(safe-area-inset-top, 0px); z-index: 20; background: var(--bg); border-bottom: 1px solid var(--line); transition: transform .25s ease; }
.topbar.hide { transform: translateY(-110%); }
.topbar-row { min-width: 0; max-width: 1180px; margin: 0 auto; padding-inline: 20px; padding-block: 8px; display: flex; gap: 8px; align-items: center; }
.tb-home, .menu > summary { display: inline-flex; align-items: center; gap: 6px; font-size: 13.5px; font-weight: 600; color: var(--fg); text-decoration: none; padding: 8px 12px; border-radius: 8px; border: 1px solid var(--line); background: var(--surface); white-space: nowrap; cursor: pointer; }
.tb-home:hover, .menu > summary:hover { border-color: var(--accent); }
.tb-home:focus-visible, .menu > summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.tb-title { font-family: var(--font-display); font-weight: 800; font-size: 17px; white-space: nowrap; }
.topbar #filter { flex: 1 1 0; width: 0; min-width: 0; max-width: 460px; }
.menu { position: relative; }
.menu > summary { list-style: none; }
.menu > summary::-webkit-details-marker { display: none; }
.menu > summary::after { content: ""; width: 6px; height: 6px; border-right: 2px solid currentColor; border-bottom: 2px solid currentColor; transform: rotate(45deg) translateY(-2px); }
.menu-panel { position: absolute; right: 0; top: calc(100% + 6px); background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 10px; box-shadow: 0 10px 30px rgb(0 0 0 / .18); width: max-content; min-width: 220px; max-width: min(320px, calc(100vw - 32px)); display: grid; gap: 10px; z-index: 30; }
.menu-panel nav { display: grid; gap: 2px; }
.menu-panel nav a { padding: 7px 10px; border-radius: 6px; text-decoration: none; color: var(--fg); font-size: 14px; border: 0; background: transparent; }
.menu-panel nav a:hover { background: var(--accent-soft); }
.menu-panel .seg { display: flex; }
.menu-panel .seg button { flex: 1; }
.menu-panel h4 { margin: 0; font-family: var(--font-mono); font-size: 11px; letter-spacing: .07em; text-transform: uppercase; color: var(--muted); }
.progress { height: 2px; }
#progress-bar { display: block; height: 100%; width: 0; background: var(--accent); }
.totop { position: fixed; right: 16px; bottom: calc(16px + env(safe-area-inset-bottom, 0px)); z-index: 15; font: inherit; font-size: 13px; font-weight: 600; padding: 9px 14px; border-radius: 999px; border: 1px solid var(--line); background: var(--surface); color: var(--fg); box-shadow: 0 6px 20px rgb(0 0 0 / .15); cursor: pointer; }
.totop:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (max-width: 760px) {
  .tb-label, .tb-title, .menu .sum-label { display: none; }
  .topbar-row { padding-inline: 16px; gap: 6px; }
  .tb-home, .menu > summary { padding: 8px 10px; }
}

/* ---------- Karten: offene Erklärung über volle Breite ---------- */
.grid { align-items: start; grid-auto-flow: dense; }
.card-main { display: grid; gap: 10px; min-width: 0; align-content: start; }
.card { scroll-margin-top: 76px; }
section { scroll-margin-top: 76px; }
.card:has(> .explain[open]) { grid-column: 1 / -1; }
@media (min-width: 900px) {
  .card:has(> .explain[open]) { grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); column-gap: 28px; align-items: start; }
  .card:has(> .explain[open]) > .explain { border-top: 0; padding-top: 0; border-left: 1px dashed var(--line); padding-left: 24px; }
}
.card.flash { animation: flash 1.8s ease-out; }
@keyframes flash { from { box-shadow: 0 0 0 3px var(--accent); } to { box-shadow: 0 0 0 0 transparent; } }
@media (prefers-reduced-motion: reduce) { .card.flash { animation: none; outline: 2px solid var(--accent); } .topbar { transition: none; } }

/* ---------- Kopieren und Kartenlinks ---------- */
.v { position: relative; }
.copy { position: absolute; top: 22px; right: 6px; font-family: var(--font-mono); font-size: 11px; padding: 3px 8px; border-radius: 5px; border: 1px solid rgb(255 255 255 / .18); background: rgb(255 255 255 / .08); color: var(--code-fg); cursor: pointer; opacity: .75; }
.copy:hover, .copy:focus-visible { opacity: 1; }
.copy:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.anchor { margin-left: 6px; color: var(--muted); text-decoration: none; font-weight: 400; opacity: .35; }
.card:hover .anchor, .anchor:focus-visible { opacity: 1; }
"""
    css = sheetgen.BASE_STYLE + sheetgen.EXTRA_CSS + "\n".join(colors) + cro + ui
    (SITE / "assets" / "app.css").write_text(css)

# ---------------------------------------------------------------- JS
def build_js():
    hl = {k: v for k, v in sheetgen.HL.items()}
    js = r'''/* Gemeinsame Logik aller Spickzettel-Seiten */
(function () {
  var body = document.body, lang = body.dataset.lang || "js";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* Highlighting */
  var HL = {};
''' + "".join(f'  HL["{k}"] = function () {{\n{v}  }};\n' for k, v in hl.items()) + r'''
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
'''
    (SITE / "assets" / "app.js").write_text(js)

FONTS = sheetgen.FONTS

# ---------------------------------------------------------------- Unterseiten
def build_page(sheet, part):
    k = sheet["key"]
    nav = "".join(f'<a href="#{sid}">{html.escape(strip_tags(t))}</a>' for sid, t in part["nav"])
    if part["infobox"]:
        nav += '<a href="#mehr">Mehr aus Marketing-Sicht</a>'
    seg = ""
    if part["has_long"]:
        seg = f'''<h4>Code-Varianten</h4>
          <div class="seg" role="group" aria-label="Varianten anzeigen">
            <button type="button" id="show-both" aria-pressed="true">Beide</button>
            <button type="button" id="show-short" aria-pressed="false">{html.escape(part["short_lbl"])}</button>
            <button type="button" id="show-long" aria-pressed="false">{html.escape(part["long_lbl"])}</button>
          </div>'''
    infobox = f'<aside class="infobox" id="mehr">{part["infobox"]}</aside>' if part["infobox"] else ""
    others = " · ".join(f'<a href="{s["key"]}.html">{html.escape(s["title"])}</a>' for s in SHEETS if s["key"] != k)
    page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(sheet["title"])} · Spickzettel</title>
{FONTS}
<link rel="stylesheet" href="assets/app.css">
</head>
<body data-sheet="{k}" data-lang="{sheet["lang"]}">
<header class="topbar" id="topbar">
  <div class="topbar-row">
    <a class="tb-home" href="index.html" aria-label="Zur Übersicht">←<span class="tb-label"> Übersicht</span></a>
    <span class="tb-title">{html.escape(sheet["title"])}</span>
    <input id="filter" type="search" placeholder="{html.escape(part["placeholder"])}" aria-label="Karten auf dieser Seite filtern">
    <details class="menu">
      <summary><span class="sum-label">Themen</span><span class="sum-short" aria-hidden="true">☰</span></summary>
      <div class="menu-panel"><nav aria-label="Abschnitte">{nav}</nav></div>
    </details>
    <details class="menu">
      <summary aria-label="Ansicht"><span class="sum-label">Ansicht</span><span aria-hidden="true">⚙</span></summary>
      <div class="menu-panel">
        {seg}
        <h4>Erklärungen</h4>
        <button type="button" class="ghost" id="toggle-all">Alle Erklärungen aufklappen</button>
      </div>
    </details>
  </div>
  <div class="progress" aria-hidden="true"><span id="progress-bar"></span></div>
</header>

<main class="wrap">
  <header>
    <div class="eyebrow">{part["eyebrow"]}</div>
    <h1>{part["h1"]}</h1>
    <p class="lede">{part["lede"]}
    <div class="legend">{part["legend"]}</div>
  </header>

  {part["sections"]}

  {infobox}
  <p class="empty" id="empty" hidden>Kein Konzept passt zu diesem Suchbegriff.</p>

  <footer>{part["footer"]}<br><br>Weitere Zettel: {others}</footer>
</main>

<button type="button" class="totop" id="totop" hidden>↑ Nach oben</button>
<script src="assets/app.js"></script>
{part["loader"]}
</body>
</html>
"""
    page = page.replace('<span class="sum-short" aria-hidden="true">☰</span>', '<span aria-hidden="true">☰</span>')
    (SITE / f"{k}.html").write_text(page)

# ---------------------------------------------------------------- Suchindex
def build_index(parts):
    idx = []
    for sh in SHEETS:
        p = parts[sh["key"]]
        for m in re.finditer(r'<section id="([^"]+)">\s*<h2>(.*?) <span.*?</section>', p["sections"], re.S):
            sid, stitle = m.group(1), strip_tags(m.group(2))
            for a in re.finditer(r'<article class="card" id="([^"]+)">(.*?)</article>', m.group(0), re.S):
                cid, body = a.group(1), a.group(2)
                title = strip_tags(re.search(r"<h3>(.*?)</h3>", body, re.S).group(1))
                desc = strip_tags((re.search(r"<p>(.*?)</p>", body, re.S) or re.search(r"(.*)", "")).group(1))
                ex = re.search(r'<div class="ex">(.*?)</details>\s*</div>', body, re.S)
                text = strip_tags(ex.group(1)) if ex else ""
                idx.append(dict(id=cid, s=sh["key"], st=sh["title"], sec=stitle, t=title, d=desc, x=text[:900]))
    (SITE / "assets" / "search.json").write_text(json.dumps(idx, ensure_ascii=False, separators=(",", ":")))
    return idx

# ---------------------------------------------------------------- Hub
def build_hub(parts):
    hubsrc = (HERE / "spickzettel-hub.html").read_text()
    hubcss = re.search(r"<style>(.*?)</style>", hubsrc, re.S).group(1)
    for sh in SHEETS:
        if f".sheet.{sh['key']} " not in hubcss:
            pass
    data = []
    for sh in SHEETS:
        p = parts[sh["key"]]
        secs = []
        for sid, t in p["nav"]:
            sec_html = re.search(rf'<section id="{re.escape(sid)}">(.*?)</section>', p["sections"], re.S).group(1)
            concepts = [dict(id=a, t=strip_tags(h)) for a, h in re.findall(r'<article class="card" id="([^"]+)">.*?<h3>(.*?)</h3>', sec_html, re.S)]
            secs.append(dict(id=sid, title=strip_tags(t), concepts=concepts))
        data.append(dict(cat=sh["cat"], key=sh["key"], title=sh["title"], blurb=sh["blurb"], badge=sh["badge"], level=sh["level"], sections=secs))
    page = """<title>Spickzettel-Hub</title>
""" + FONTS + """
<link rel="stylesheet" href="assets/app.css">
<style>""" + hubcss + """
.sec li a { color: inherit; text-decoration: none; }
.sec li a:hover { color: var(--c); text-decoration: underline; }
#results .r-x { display: block; color: var(--muted); font-size: 12.5px; margin-top: 2px; }
#results a { flex-direction: column; align-items: flex-start; gap: 0; }
#results mark { background: var(--js-soft); color: inherit; border-radius: 3px; padding: 0 2px; }
</style>

<div class="wrap">
  <header>
    <div class="eyebrow">Fullstack-Bootcamp · Nachschlagen &amp; Üben</div>
    <h1>Spickzettel-Hub</h1>
    <p class="lede">Alle Spickzettel an einem Ort, nach Themen gruppiert. Jeder Abschnitt und jede Karte ist direkt verlinkt, und die Suche durchsucht auch die Erklärungen aller Zettel. Jede Karte hat Code-Beispiele, eine Erklärung zum Aufklappen, einen Selbsttest und Links zur Doku.</p>
    <div class="stats" id="stats"></div>
  </header>

  <div class="search">
    <input id="q" type="search" placeholder="Alles durchsuchen, z.B. reduce, Generics, Consent …" aria-label="Alle Spickzettel durchsuchen">
    <div id="results" aria-live="polite"></div>
  </div>

  <nav class="cat-nav" id="catnav" aria-label="Themenbereiche"></nav>
  <div class="sheets" id="sheets"></div>

  <section aria-labelledby="plan-h" style="display:grid;gap:12px">
    <h3 class="plan-h" id="plan-h">Noch nicht erstellt</h3>
    <p class="hint">Vorschläge für die nächsten Zettel, passend zu deinem Backend-Modul.</p>
    <div class="planned" id="planned"></div>
  </section>

  <footer>Tipp: Ein Kürzel hinter dem Link öffnet direkt einen Zettel, z.B. <code>#css</code>, oder eine Karte, z.B. <code>#css-grid-2</code>. Die Kürzel der Karten stehen hinter dem #-Zeichen an jeder Kartenüberschrift.</footer>
</div>

<script>
var CATS = __CATS__;
var SHEETS = __DATA__;
var PLANNED = __PLANNED__;
(function () {
  /* Weiterleitung per Kürzel: #css oder #css-grid-2 */
  var h = location.hash.slice(1);
  if (h) {
    var key = h.split("-")[0];
    if (SHEETS.some(function (s) { return s.key === key; })) { location.replace(key + ".html" + (h.indexOf("-") > 0 ? "#" + h : "")); return; }
  }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  var total = 0, secCount = 0;
  SHEETS.forEach(function (s) { s.sections.forEach(function (x) { secCount++; total += x.concepts.length; }); });
  document.getElementById("stats").innerHTML = "<span><b>" + SHEETS.length + "</b> Spickzettel</span><span><b>" + secCount + "</b> Abschnitte</span><span><b>" + total + "</b> Konzepte</span>";

  function sheetHtml(s) {
    var n = s.sections.reduce(function (a, x) { return a + x.concepts.length; }, 0);
    var secs = s.sections.map(function (x) {
      return '<div class="sec"><a href="' + s.key + '.html#' + esc(x.id) + '">' + esc(x.title) + '<span class="n">' + x.concepts.length + '</span></a><ul>' +
        x.concepts.map(function (c) { return '<li><a href="' + s.key + '.html#' + esc(c.id) + '">' + esc(c.t) + '</a></li>'; }).join("") + "</ul></div>";
    }).join("");
    return '<article class="sheet ' + esc(s.key) + '" id="sheet-' + esc(s.key) + '">' +
      '<div class="sheet-head"><div class="sheet-id"><div class="badge" aria-hidden="true">' + esc(s.badge) + '</div>' +
      '<div><h3>' + esc(s.title) + '</h3><div class="meta">' + n + ' Konzepte · ' + s.sections.length + ' Abschnitte · ' + esc(s.level) + '</div></div></div>' +
      '<a class="open" href="' + s.key + '.html">Spickzettel öffnen →</a></div>' +
      '<p class="blurb">' + esc(s.blurb) + '</p><div class="secs">' + secs + '</div></article>';
  }
  document.getElementById("catnav").innerHTML = CATS.map(function (c) {
    var k = SHEETS.filter(function (s) { return s.cat === c[0]; }).length;
    return '<a href="#cat-' + c[0] + '">' + esc(c[1]) + ' (' + k + ')</a>';
  }).join("");
  document.getElementById("sheets").innerHTML = CATS.map(function (c) {
    var list = SHEETS.filter(function (s) { return s.cat === c[0]; });
    return '<section class="cat" id="cat-' + c[0] + '" aria-labelledby="h-' + c[0] + '"><div class="cat-head"><h2 id="h-' + c[0] + '">' + esc(c[1]) + '</h2><p>' + esc(c[2]) + '</p></div>' + list.map(sheetHtml).join("") + '</section>';
  }).join("");
  document.getElementById("planned").innerHTML = PLANNED.map(function (p) {
    return '<div class="plan"><em>geplant</em><b>' + esc(p[0]) + '</b><span>' + esc(p[1]) + '</span></div>';
  }).join("");

  /* Volltextsuche: Index wird beim ersten Fokus geladen */
  var q = document.getElementById("q"), res = document.getElementById("results"), INDEX = null, loading = null;
  function load() {
    if (INDEX) return Promise.resolve(INDEX);
    if (!loading) loading = fetch("assets/search.json").then(function (r) { return r.json(); }).then(function (d) {
      INDEX = d.map(function (e) { e.hay = (e.t + " " + e.d + " " + e.sec + " " + e.st + " " + e.x).toLowerCase(); e.head = (e.t + " " + e.sec).toLowerCase(); return e; });
      return INDEX;
    });
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
      var hits = idx.filter(function (e) { return e.hay.indexOf(v) !== -1; });
      hits.sort(function (a, b) { return (b.head.indexOf(v) !== -1) - (a.head.indexOf(v) !== -1); });
      res.innerHTML = hits.length ? hits.slice(0, 15).map(function (h) {
        return '<a href="' + h.s + '.html#' + esc(h.id) + '"><span class="r-c">' + esc(h.t) + ' <span class="r-p">' + esc(h.st) + ' › ' + esc(h.sec) + '</span></span><span class="r-x">' + snippet(h, v) + '</span></a>';
      }).join("") + (hits.length > 15 ? '<p class="hint">' + (hits.length - 15) + ' weitere Treffer. Präziser suchen grenzt ein.</p>' : "")
      : '<p class="hint">Kein Treffer. Das Thema könnte ein guter nächster Spickzettel sein.</p>';
    }, function () { res.innerHTML = '<p class="hint">Der Suchindex konnte nicht geladen werden.</p>'; });
  }
  q.addEventListener("focus", load, { once: true });
  q.addEventListener("input", run);
})();
</script>
"""
    page = (page.replace("__CATS__", json.dumps(CATEGORIES, ensure_ascii=False))
                .replace("__DATA__", json.dumps(data, ensure_ascii=False))
                .replace("__PLANNED__", json.dumps(PLANNED, ensure_ascii=False)))
    (SITE / "index.html").write_text(page)

def main():
    parts = {sh["key"]: extract(sh) for sh in SHEETS}
    build_css(); build_js()
    for sh in SHEETS:
        build_page(sh, parts[sh["key"]])
    idx = build_index(parts)
    build_hub(parts)
    print("Seiten:", len(SHEETS), "Karten:", sum(p["count"] for p in parts.values()), "Index:", len(idx))

if __name__ == "__main__":
    main()
