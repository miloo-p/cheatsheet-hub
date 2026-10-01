# cheatsheet-hub

Spickzettel-Hub, eine Nachschlage-Website aus dem Fullstack-Bootcamp: 7 Spickzettel mit 159 Karten zu
HTML, CSS, JavaScript, TypeScript, GSAP, Three.js und Conversion-Optimierung.

Jede Karte enthält Code-Beispiele (meist zwei Varianten nebeneinander), eine aufklappbare
Erklärung mit Bild zum Merken, Ablauf, typischem Fehler und Selbsttest sowie Links zur Doku.
GSAP und Three.js haben Live-Demos, die ihre Bibliotheken erst beim ersten Klick laden.

## Aufbau

```
site/                 fertige Website (statisch, ohne Build-Schritt lauffähig)
  index.html          Hub mit Volltextsuche (ohne <html>-Gerüst, siehe unten)
                      Jeder Zettel hat ein Inhaltsverzeichnis aller Karten (Seitenleiste bzw. Menü)
  html.html … cro.html  eine Seite pro Zettel
  assets/app.css      gemeinsame Gestaltung
  assets/app.js       Highlighting, Filter, Menüs, Kopieren, Demos
  assets/search.json  Suchindex für den Hub
generator/            Python-Skripte, aus denen site/ entsteht
  *_data.py           Inhalte der Zettel (Karten, Erklärungen, Links, Demos)
  js-spickzettel.html Inhalte des JavaScript-Zettels (handgeschrieben)
  sheetgen.py         rendert einen Zettel aus *_data.py als Einzelseite
  build_*.py          Konfiguration je Zettel (Farben, Texte, Bibliotheken)
  sitegen.py          baut aus den Einzelseiten die gemeinsame Website
  build_all.sh        alles in einem Rutsch
  check_site.py       lokaler Test mit Playwright (Fehler, Überlauf, Suche, Menüs)
```

## Bauen

```bash
cd generator
./build_all.sh
```

Lokal ansehen: `cd site && python3 -m http.server`, dann http://localhost:8000/index.html.
`index.html` hat bewusst kein eigenes `<html>`-Gerüst, weil es als Claude-Artifact
veröffentlicht wird und die Plattform das Gerüst ergänzt. Im Browser funktioniert es trotzdem.

## Neuen Zettel hinzufügen

1. `neu_data.py` nach dem Muster der anderen Dateien anlegen.
2. `build_neu.py` nach dem Muster von `build_gsap.py` anlegen und in `build_all.sh` eintragen.
3. In `sitegen.py` einen Eintrag in `SHEETS` ergänzen (Kategorie, Farben, Kurztext).
4. `./build_all.sh` ausführen.
