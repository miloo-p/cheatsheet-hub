import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sheetgen import build, HUB
from cro_data import SECTIONS, INFOBOX
HUBLINK = f'<a href="{HUB}" target="_blank" rel="noopener">Spickzettel-Hub</a>'
extra = """
.short .lbl { color: var(--warn); background: var(--warn-soft); }
.short pre { border-left-color: var(--warn); }
.long .lbl { color: var(--accent); background: var(--accent-soft); }
.long pre { border-left-color: var(--accent); }
.disclaimer { font-size: 13px; color: var(--muted); border-left: 3px solid var(--line); padding-left: 10px; max-width: 70ch; margin: 0; }
"""
cfg = dict(key="cro", title="Conversion-Optimierung", eyebrow="Produkt & Wirkung · Conversion", hl="html",
    labels=("Vorher", "Nachher"), wann_heading="So misst du es",
    colors=dict(accent="#0f7a5c", accent_soft="#d9f2ea", long="#5b55a8", long_soft="#e8e6f7",
                accent_d="#5fd3ae", accent_soft_d="#143029", long_d="#b3adf2", long_soft_d="#24223d", kw="#5fd3ae"),
    extra_css=extra,
    lede="{n} Themen der Conversion-Optimierung aus Entwicklersicht: messen, testen, Formulare, Ladezeit und die rechtlichen Pflichten in Deutschland. Jede Karte zeigt ein typisches <b>Vorher</b> und ein verbessertes <b>Nachher</b>. In der Erklärung steht statt „Wann welche Schreibweise?“ jeweils <b>So misst du es</b>, denn eine Änderung ist erst dann eine Verbesserung, wenn die Zahlen es zeigen. Zahlen und Rechtslage sind mit Quellen belegt (Stand Oktober 2026). Ganz unten gibt es einen Kasten mit Lesestoff aus Marketing-Sicht.</p><p class=\"disclaimer\">Die Karten zum Recht ersetzen keine Rechtsberatung. Sie zeigen, was du als Entwickler kennen solltest, um die richtigen Fragen zu stellen.",
    legend_html='<span><b class="lbl" style="color:var(--warn);background:var(--warn-soft)">Vorher</b> häufige Umsetzung mit Problem</span><span><b class="lbl" style="color:var(--accent);background:var(--accent-soft)">Nachher</b> verbesserte Umsetzung</span>',
    placeholder="Filtern, z.B. Funnel, Formular, Consent …",
    infobox=INFOBOX,
    footer=f"Übungsidee: Nimm ein Projekt aus deinem Kurs und schreibe einen Tracking-Plan mit fünf Events. Baue den <code>track()</code>-Wrapper mit Consent-Prüfung ein und miss die Core Web Vitals mit <code>web-vitals</code>. Formulare und Barrierefreiheit vertiefst du im HTML-Spickzettel, alle Zettel im {HUBLINK}.")
print("cro", build(cfg, SECTIONS, "cro-spickzettel.html"))
