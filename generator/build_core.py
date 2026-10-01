"""Baut die Web-Grundlagen-Zettel TS, CSS und HTML mit dem gemeinsamen Generator."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sheetgen import build, HUB

URL = dict(
    html="https://claude.ai/artifact/YPbjHyWZpJ8tEecBdsXRob",
    css="https://claude.ai/artifact/9i6icDS2mpDmQm3j3fzdpT",
    js="https://claude.ai/artifact/EgkjrRmDocu7CAwqekbRN7",
    ts="https://claude.ai/artifact/W9b8p3sj4TGiwhcaTx8DLW",
)

def link(key, text):
    return f'<a href="{URL[key]}" target="_blank" rel="noopener">{text}</a>'

HUBLINK = f'<a href="{HUB}" target="_blank" rel="noopener">Spickzettel-Hub</a>'

def main(which=("ts", "css", "html")):
    if "ts" in which:
        from ts_data import SECTIONS
        cfg = dict(key="ts", title="TypeScript Spickzettel", eyebrow="Web-Grundlagen · TypeScript", hl="ts",
            colors=dict(accent="#2b5fae", accent_soft="#e2eaf7", long="#7a3f97", long_soft="#f2e7f7",
                        accent_d="#8db4f2", accent_soft_d="#1b2740", long_d="#d3a3ec", long_soft_d="#2b1f35", kw="#8db4f2"),
            lede="{n} Konzepte, jedes in zwei Schreibweisen. <b>Kurz</b> heißt hier meistens: TypeScript den Typ ableiten lassen oder einen Utility Type benutzen. <b>Ausführlich</b> heißt: jeden Typ ausdrücklich hinschreiben. Beide Varianten sind gleichwertig. Unter jedem Beispiel klappt eine Erklärung auf, mit Bild zum Merken, Ablauf, typischem Fehler und Selbsttest. Die Doku-Links führen zur offiziellen Doku von TypeScript, React und Express. Die gibt es nur auf Englisch.",
            legend=[("Kurz", "Inferenz und kompakte Syntax"), ("Ausführlich", "alle Typen ausgeschrieben")],
            placeholder="Filtern, z.B. Partial, unknown, useState …",
            footer=f"Übungsidee: Nimm ein kleines JavaScript-Projekt aus deinem Kurs, benenne eine Datei in <code>.ts</code> um und arbeite die roten Unterstreichungen ab. Jede davon passt zu einer Karte auf dieser Seite. Grundlagen auffrischen im {link('js', 'JavaScript Spickzettel')}, alle Zettel im {HUBLINK}.")
        print("ts", build(cfg, SECTIONS, "ts-spickzettel.html"))
    if "css" in which:
        from css_data import SECTIONS
        cfg = dict(key="css", title="CSS Spickzettel", eyebrow="Web-Grundlagen · CSS", hl="css",
            colors=dict(accent="#177258", accent_soft="#dcf1e9", long="#a8452a", long_soft="#f8e6df",
                        accent_d="#6fd3ad", accent_soft_d="#15302a", long_d="#f0a487", long_soft_d="#36221c", kw="#6fd3ad"),
            lede="{n} Konzepte, jedes in zwei Schreibweisen. <b>Kurz</b> heißt hier: Kurzschreibweisen wie <code>margin</code>, <code>flex</code> oder <code>inset</code> und moderne Lösungen. <b>Ausführlich</b> heißt: jede Einzeleigenschaft ausgeschrieben oder der klassische Weg, den du in älterem Code findest. Unter jedem Beispiel klappt eine Erklärung auf, mit Bild zum Merken, Ablauf, typischem Fehler und Selbsttest. Die Doku-Links führen zu MDN auf Deutsch.",
            legend=[("Kurz", "Kurzschreibweise, moderner Weg"), ("Ausführlich", "Einzeleigenschaften, klassischer Weg")],
            placeholder="Filtern, z.B. grid, sticky, clamp …",
            footer=f"Übungsidee: Öffne in den Entwicklertools deines Browsers eine beliebige Website, wähle ein Element aus und lies im Styles-Panel, welche Kurzschreibweisen dort verwendet werden. Weiter zum {link('js', 'JavaScript Spickzettel')} oder zurück zum {HUBLINK}.")
        print("css", build(cfg, SECTIONS, "css-spickzettel.html"))
    if "html" in which:
        from html_data import SECTIONS
        cfg = dict(key="html", title="HTML Spickzettel", eyebrow="Web-Grundlagen · HTML", hl="html",
            colors=dict(accent="#a8326a", accent_soft="#f8e2ec", long="#4b52a8", long_soft="#e6e7f7",
                        accent_d="#f39ac0", accent_soft_d="#3a1d2a", long_d="#aeb2f5", long_soft_d="#22243f", kw="#f39ac0"),
            lede="{n} Konzepte, jedes in zwei Schreibweisen. <b>Kurz</b> heißt hier: das passende native Element oder Attribut, das Tastatur, Screenreader und Verhalten gleich mitbringt. <b>Ausführlich</b> heißt: der Nachbau mit <code>&lt;div&gt;</code>, ARIA und JavaScript oder die ältere Schreibweise, die dir in bestehendem Code begegnet. Unter jedem Beispiel klappt eine Erklärung auf, mit Bild zum Merken, Ablauf, typischem Fehler und Selbsttest. Die Doku-Links führen zu MDN auf Deutsch.",
            legend=[("Kurz", "natives Element oder Attribut"), ("Ausführlich", "Nachbau oder ältere Schreibweise")],
            placeholder="Filtern, z.B. dialog, label, alt …",
            footer=f"Übungsidee: Öffne eines deiner Kursprojekte, aktiviere in den Chrome-Entwicklertools unter „Lighthouse“ die Kategorie Barrierefreiheit und arbeite die Hinweise ab. Fast jeder davon passt zu einer Karte auf dieser Seite. Gestaltung geht weiter im {link('css', 'CSS Spickzettel')}, alle Zettel im {HUBLINK}.")
        print("html", build(cfg, SECTIONS, "html-spickzettel.html"))

if __name__ == "__main__":
    main(tuple(sys.argv[1:]) or ("ts", "css", "html"))
