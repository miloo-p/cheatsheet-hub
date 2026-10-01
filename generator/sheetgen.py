"""Gemeinsamer Generator für alle Spickzettel.

build(cfg, SECTIONS, outfile)

Karte (aus den *_data.py): dict(t, d, k, a, e, l, demo=None)
  k / a  : Code der beiden Spalten. a=None -> nur ein Code-Block (Label cfg["single_label"]).
  e      : (bild, schritte, fehler, wann, frage, antwort)
  l      : [(linktext, url), ...]
  demo   : optional dict(html=Startmarkup der Bühne, js=Funktionskörper mit Variable `stage`,
           h=Bühnenhöhe in px). Rückgabe einer Funktion = Aufräumen.
"""
import html, re, pathlib, json

HERE = pathlib.Path(__file__).parent
HUB = "https://claude.ai/artifact/8MMr1HXJMFnYe4ubTYDY4x"

_base = (HERE / "js-spickzettel.html").read_text()
BASE_STYLE = re.search(r"<style>(.*?)</style>", _base, re.S).group(1)
BASE_SCRIPT = re.search(r"<script>(.*?)</script>", _base, re.S).group(1)

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">'

JS_KW = "const|let|var|function|return|if|else|for|of|in|async|await|new|class|extends|constructor|super|this|throw|try|catch|finally|import|export|default|from|as|true|false|null|undefined|typeof|delete|break|get"
TS_KW = JS_KW + "|type|interface|keyof|readonly|enum|is|string|number|boolean|void|unknown|any|never|switch|case"

def _hl_js(kw):
    return r'''  // Syntax-Highlighting
  var RE = new RegExp("(\\/\\/[^\\n]*|\\/\\*[\\s\\S]*?\\*\\/)|(\"(?:[^\"\\\\\\n]|\\\\.)*\"|'(?:[^'\\\\\\n]|\\\\.)*'|`(?:[^`\\\\]|\\\\.)*`)|\\b(''' + kw + r''')\\b", "g");
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

'''

HL_CSS = r'''  // Syntax-Highlighting für CSS
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

'''

HL_HTML = r'''  // Syntax-Highlighting für HTML
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

'''

HL = {"js": _hl_js(JS_KW), "ts": _hl_js(TS_KW), "css": HL_CSS, "html": HL_HTML}

EXTRA_CSS = """
/* Live-Demos */
.demo { border: 1px solid var(--line); border-radius: 8px; overflow: hidden; background: var(--bg); min-width: 0; }
.demo-bar { display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 6px 8px 6px 10px; border-bottom: 1px solid var(--line); background: var(--surface); }
.demo-bar .lbl { color: var(--fg); background: var(--line); }
.demo-bar .run { font: inherit; font-size: 12.5px; font-weight: 600; border: 1px solid var(--line); background: var(--fg); color: var(--bg); padding: 4px 10px; border-radius: 6px; cursor: pointer; }
.demo-bar .run:hover { background: var(--accent); border-color: var(--accent); color: var(--bg); }
.demo-bar .run:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.stage { position: relative; height: var(--h, 160px); overflow: hidden; padding: 12px; font-size: 13px; color: var(--fg); }
.stage.flush { padding: 0; }
.stage canvas { display: block; width: 100%; height: 100%; }
.stage .box { width: 44px; height: 44px; border-radius: 8px; background: var(--accent); }
.stage .box.alt { background: var(--long); }
.stage .box.warn { background: var(--warn); }
.stage .row { display: flex; gap: 8px; align-items: center; }
.stage .col { display: grid; gap: 8px; }
.stage .note { position: absolute; left: 12px; bottom: 8px; font-family: var(--font-mono); font-size: 11px; color: var(--muted); }
.stage .chip { font-family: var(--font-mono); font-size: 12px; padding: 4px 8px; border-radius: 6px; background: var(--surface); border: 1px solid var(--line); }
.stage .scroller { position: absolute; inset: 0; overflow-y: auto; padding: 12px; }
.stage .spacer { height: 220px; display: grid; place-items: center; color: var(--muted); font-family: var(--font-mono); font-size: 11px; }
/* Infobox */
.infobox { border: 1px solid var(--line); border-left: 4px solid var(--long); background: var(--surface); border-radius: 10px; padding: 18px 20px; display: grid; gap: 10px; margin-bottom: 40px; }
.infobox h2 { font-size: 20px; margin: 0; }
.infobox p { margin: 0; color: var(--muted); max-width: 70ch; }
.infobox ul { margin: 0; padding-left: 18px; display: grid; gap: 6px; }
.infobox li { max-width: 75ch; }
.infobox a { color: var(--long); }
"""

DEMO_RUNTIME = r'''
(function () {
  var active = {};
  function stop(id) {
    if (active[id]) { try { active[id](); } catch (e) { console.warn(e); } active[id] = null; }
  }
  document.querySelectorAll(".demo").forEach(function (box) {
    var id = box.dataset.demo, stage = box.querySelector(".stage"), btn = box.querySelector(".run");
    var tpl = box.querySelector("template");
    btn.addEventListener("click", function () {
      var fn = (window.DEMOS || {})[id];
      if (!fn) { stage.innerHTML = '<span class="note">Bibliothek lädt noch, bitte gleich nochmal klicken.</span>'; return; }
      if (window.DEMO_SINGLE) { Object.keys(active).forEach(function (k) { if (k !== id) stop(k); }); }
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
        stage.innerHTML = '<span class="note">Demo-Fehler: ' + String(e.message || e) + '</span>';
      }
      btn.textContent = "↻ Neu starten";
    });
  });
})();
'''

def fmt(s):
    out = []
    for i, p in enumerate(s.split("`")):
        e = html.escape(p, quote=False)
        out.append(f"<code>{e}</code>" if i % 2 else e)
    return "".join(out)

def _explain(e, wann_heading):
    bild, steps, fehler, wann, frage, antwort = e
    li = "".join(f"<li>{fmt(s)}</li>" for s in steps)
    return f"""<details class="explain"><summary>Erklärung</summary>
          <div class="ex">
            <div class="ex-b"><h4>Vorstellung</h4><p>{fmt(bild)}</p></div>
            <div class="ex-b"><h4>Was passiert, Schritt für Schritt</h4><ol>{li}</ol></div>
            <div class="ex-b warn"><h4>Typischer Fehler</h4><p>{fmt(fehler)}</p></div>
            <div class="ex-b"><h4>{html.escape(wann_heading)}</h4><p>{fmt(wann)}</p></div>
            <div class="ex-b quiz"><h4>Selbsttest</h4><p>{fmt(frage)}</p>
              <details class="answer"><summary>Lösung zeigen</summary><p>{fmt(antwort)}</p></details></div>
          </div>
        </details>"""

def build(cfg, SECTIONS, outfile):
    labels = cfg.get("labels", ("Kurz", "Ausführlich"))
    single = cfg.get("single_label", "Code")
    wann_h = cfg.get("wann_heading", "Wann welche Schreibweise?")
    demos_js = []
    n = 0

    def card(c, idx):
        nonlocal n
        n += 1
        lab = c.get("labels", labels)
        links = "".join(f'<a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a>' for t, u in c["l"])
        if c.get("a") is None:
            code = f'''<div class="v short"><span class="lbl">{html.escape(single)}</span>
<pre>{html.escape(c["k"], quote=False)}</pre></div>'''
        else:
            code = f'''<div class="v short"><span class="lbl">{html.escape(lab[0])}</span>
<pre>{html.escape(c["k"], quote=False)}</pre></div>
        <div class="v long"><span class="lbl">{html.escape(lab[1])}</span>
<pre>{html.escape(c["a"], quote=False)}</pre></div>'''
        demo = ""
        if c.get("demo"):
            d = c["demo"]
            did = f"d{idx}"
            flush = " flush" if d.get("flush") else ""
            demo = f'''<div class="demo" data-demo="{did}">
          <div class="demo-bar"><span class="lbl">Live-Demo</span><button type="button" class="run">▶ Abspielen</button></div>
          <template>{d.get("html", "")}</template>
          <div class="stage{flush}" style="--h:{d.get("h", 160)}px">{d.get("html", "")}</div>
        </div>'''
            demos_js.append(f'DEMOS["{did}"] = function (stage) {{\n{d["js"]}\n}};')
        return f"""
      <article class="card"><h3>{fmt(c["t"])}</h3>
        <p>{fmt(c["d"])}</p>
        {code}
        {demo}
        <div class="docs"><span class="docs-l">Doku</span>{links}</div>
        {_explain(c["e"], wann_h)}
      </article>"""

    idx = 0
    secs = ""
    for sid, title, tag, sub, cards in SECTIONS:
        inner = ""
        for c in cards:
            idx += 1
            inner += card(c, idx)
        secs += f"""
  <section id="{sid}">
    <h2>{html.escape(title)} <span class="tag">{tag}</span></h2>
    <p class="sub">{fmt(sub)}</p>
    <div class="grid">{inner}
    </div>
  </section>
"""
    nav = "".join(f'<a href="#{sid}">{html.escape(t)}</a>' for sid, t, *_ in SECTIONS)
    if cfg.get("infobox"):
        nav += '<a href="#mehr">Mehr</a>'

    c = cfg["colors"]
    style = BASE_STYLE + f"""
/* Farben dieses Zettels */
:root {{ --accent: {c['accent']}; --accent-soft: {c['accent_soft']}; --long: {c['long']}; --long-soft: {c['long_soft']}; --code-kw: {c['kw']}; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --accent: {c['accent_d']}; --accent-soft: {c['accent_soft_d']}; --long: {c['long_d']}; --long-soft: {c['long_soft_d']}; --code-kw: {c['kw']}; }} }}
:root[data-theme="dark"] {{ --accent: {c['accent_d']}; --accent-soft: {c['accent_soft_d']}; --long: {c['long_d']}; --long-soft: {c['long_soft_d']}; --code-kw: {c['kw']}; }}
""" + EXTRA_CSS + cfg.get("extra_css", "")

    script = BASE_SCRIPT
    start = script.index("  // Einfaches Syntax-Highlighting")
    end = script.index("  // Filter")
    script = script[:start] + HL[cfg.get("hl", "js")] + script[end:]
    script = script.replace('"js-cheat-mode"', f'"{cfg["key"]}-cheat-mode"')
    if not cfg.get("has_long", True):
        pass

    seg = ""
    if cfg.get("has_long", True):
        seg = f'''<div class="seg" role="group" aria-label="Varianten anzeigen">
        <button type="button" id="show-both" aria-pressed="true">Beide</button>
        <button type="button" id="show-short" aria-pressed="false">Nur {html.escape(labels[0][0].lower() + labels[0][1:])}</button>
        <button type="button" id="show-long" aria-pressed="false">Nur {html.escape(labels[1][0].lower() + labels[1][1:])}</button>
      </div>'''
    else:
        # Buttons trotzdem anlegen, damit das Basis-Skript sie findet, aber verstecken
        seg = '<div class="seg" hidden><button type="button" id="show-both" aria-pressed="true"></button><button type="button" id="show-short"></button><button type="button" id="show-long"></button></div>'

    legend = cfg.get("legend_html") or "".join(
        f'<span><b class="lbl" style="color:var(--{"accent" if i == 0 else "long"});background:var(--{"accent" if i == 0 else "long"}-soft)">{html.escape(lab)}</b> {html.escape(desc)}</span>'
        for i, (lab, desc) in enumerate(cfg["legend"]))

    infobox = ""
    if cfg.get("infobox"):
        infobox = f'<aside class="infobox" id="mehr">{cfg["infobox"]}</aside>'

    demo_block = ""
    if demos_js:
        if cfg.get("demo_mode") == "module":
            demo_block = cfg.get("head_scripts", "") + "\n<script type=\"module\">\n" + cfg.get("module_prelude", "") + "\nwindow.DEMO_SINGLE = true;\nconst DEMOS = window.DEMOS = {};\n" + "\n\n".join(demos_js) + "\n" + cfg.get("module_post", "") + "\n</script>"
        else:
            demo_block = cfg.get("head_scripts", "") + "\n<script>\n" + cfg.get("classic_prelude", "") + "\nvar DEMOS = window.DEMOS = {};\n" + "\n\n".join(demos_js) + "\n</script>"

    page = f"""<title>{html.escape(cfg["title"])}</title>
{FONTS}
<style>{style}</style>

<div class="wrap">
  <header>
    <div class="eyebrow"><a class="hub" href="{HUB}" target="_blank" rel="noopener">← Spickzettel-Hub</a> · {html.escape(cfg["eyebrow"])}</div>
    <h1>{html.escape(cfg["title"])}</h1>
    <p class="lede">{cfg["lede"].replace("{n}", str(n))}</p>
    <div class="legend">{legend}</div>
  </header>

  <div class="tools">
    <div class="toolrow">
      <input id="filter" type="search" placeholder="{html.escape(cfg["placeholder"])}" aria-label="Konzepte filtern">
      {seg}
      <button type="button" class="ghost" id="toggle-all">Alle Erklärungen aufklappen</button>
    </div>
    <nav>{nav}</nav>
  </div>
{secs}
  {infobox}
  <p class="empty" id="empty" hidden>Kein Konzept passt zu diesem Suchbegriff.</p>

  <footer>{cfg["footer"]}</footer>
</div>

<script>{script}{DEMO_RUNTIME if demos_js else ""}</script>
{demo_block}
"""
    (HERE / outfile).write_text(page)
    return n
