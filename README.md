# Cheatsheet Hub

**Live: https://miloo-p.github.io/cheatsheet-hub/**

Mein persönliches Glossar aus dem Frontend-Teil meines Fullstack-Bootcamps. Hier sammle ich, was ich gelernt habe, damit es nicht verloren geht, während ich im Backend-Modul stecke.

Das Projekt ist **vibe-gecodet**: Inhalte, Generator und Website sind im Gespräch mit Claude (KI von Anthropic) entstanden. Ich habe Richtung, Themen und Aufbau vorgegeben, Claude hat geschrieben, gebaut und getestet. Mehr dazu unter [Wie das entstanden ist](#wie-das-entstanden-ist).

## Was drin ist

7 Spickzettel mit 159 Karten, gruppiert in drei Bereiche:

| Bereich | Zettel | Karten | Schwerpunkt |
|---|---|---|---|
| Web-Grundlagen | HTML | 24 | Semantik, Formulare fürs Backend, native Dialoge, Barrierefreiheit |
| | CSS | 28 | Box Model, Selektoren, Flexbox, Grid, Responsive Design, Animation |
| | JavaScript | 27 | Arrays, Objekte, Funktionen, Asynchronität, typische Muster |
| | TypeScript | 27 | Unions, Generics, Utility Types, API-Daten, React und Express |
| Animation & 3D | GSAP | 17 | Tweens, Timelines, ScrollTrigger, Flip, SplitText, mit Live-Demos |
| | Three.js | 17 | Szene, Licht, Schatten, Interaktion, Performance, mit 3D-Demos |
| Produkt & Wirkung | Conversion-Optimierung | 19 | Tracking, A/B-Tests, Core Web Vitals, Rechtliches in Deutschland |

### Aufbau einer Karte

Jede Karte erklärt ein Konzept und folgt immer demselben Muster:

- **Zwei Varianten nebeneinander.** Was die Spalten bedeuten, hängt vom Zettel ab:
  - **HTML:** natives Element und Nachbau mit `<div>`
  - **CSS:** Kurzschreibweise und Einzeleigenschaften
  - **JavaScript, TypeScript:** kurze und ausführliche Schreibweise
  - **GSAP:** mit und ohne Bibliothek
  - **Conversion:** vorher und nachher
- **Erklärung zum Aufklappen**, in fünf Teilen:
  - ein Bild aus dem Alltag zum Merken
  - was Schritt für Schritt passiert
  - der typische Fehler
  - wann man welche Variante nimmt
  - eine Selbsttest-Frage mit verdeckter Lösung
- **Doku-Links** zu MDN (auf Deutsch, wo vorhanden) und den offiziellen Dokus.
- **Live-Demo** bei GSAP und Three.js. Die Bibliotheken werden erst beim ersten Klick geladen.

### Bedienung

- **Hub mit Volltextsuche:** Die Suche durchsucht alle Zettel inklusive der Erklärungen und springt direkt zur Karte.
- **Inhaltsverzeichnis auf jeder Seite:** Am Desktop als Seitenleiste, die die aktuelle Karte markiert. Am Handy im Menü.
- **Filter pro Seite.** Zusätzlich lässt sich umschalten, ob beide Code-Varianten oder nur eine angezeigt werden.
- **Kopieren-Button** an jedem Code-Block und ein **Link** an jeder Karte.
- **Hell und dunkel:** passt sich dem System an.
- **Handytauglich:** Die Leiste blendet sich beim Scrollen aus.

## Ansehen

Die Website ist statisch, es braucht also keinen Server mit eigener Logik:

```bash
cd site
python3 -m http.server
```

Dann `http://localhost:8000/index.html` öffnen.

Veröffentlicht wird automatisch: Jeder Push auf `main` startet den Workflow `.github/workflows/pages.yml`, der `site/` auf GitHub Pages stellt. Zusätzlich gibt es eine Version als Claude-Artifact.

`site/index.html` hat absichtlich kein eigenes `<html>`-Gerüst, weil die Artifact-Plattform das ergänzt. Für GitHub Pages fügt der Workflow es beim Veröffentlichen hinzu.

## Projektstruktur

```
site/                     fertige Website
  index.html              Hub mit Kategorien und Volltextsuche
  html.html … cro.html    eine Seite pro Zettel
  assets/app.css          gemeinsame Gestaltung
  assets/app.js           Highlighting, Filter, Menüs, Inhaltsverzeichnis, Kopieren, Demos
  assets/search.json      Suchindex für den Hub
generator/                Python-Skripte, aus denen site/ entsteht
  *_data.py               Inhalte der Zettel: Karten, Erklärungen, Links, Demos
  js-spickzettel.html     Inhalte des JavaScript-Zettels (als HTML geschrieben)
  sheetgen.py             rendert einen Zettel aus *_data.py als Einzelseite
  build_*.py              Einstellungen je Zettel: Farben, Texte, Bibliotheken
  sitegen.py              setzt alles zur gemeinsamen Website zusammen
  build_all.sh            baut alles in einem Rutsch
  check_site.py           lokaler Test mit Playwright
```

## Bauen und erweitern

```bash
cd generator
./build_all.sh          # baut site/ komplett neu
python3 check_site.py   # optional: prüft Fehler, Layout am Handy, Suche und Menüs
```

Für das Bauen reicht Python 3. Für den Test braucht es zusätzlich Playwright mit Chromium.

**Karte ändern:** In der passenden `*_data.py` den Text oder Code anpassen und neu bauen. Text in Backticks wird automatisch als Code formatiert.

**Neuen Zettel hinzufügen:**
1. `neu_data.py` nach dem Muster der anderen Dateien anlegen.
2. `build_neu.py` nach dem Muster von `build_gsap.py` anlegen und in `build_all.sh` eintragen.
3. In `sitegen.py` einen Eintrag in `SHEETS` ergänzen: Kategorie, Farben, Kurztext.
4. `./build_all.sh` ausführen.

Ideen für die nächsten Zettel: Node & Express, SQL & Datenbanken, React Hooks, Git.

## Wie das entstanden ist

Angefangen hat es mit einer einfachen Frage: Wie halte ich mein Frontend-Wissen frisch, während das Bootcamp im Backend weitergeht? Daraus wurde zuerst eine Liste mit JavaScript-Konzepten, dann ein Spickzettel, dann mehrere. Am Ende stand eine eigene kleine Website mit Generator.

Die Arbeitsteilung:

- **Von mir:** welche Themen, welches Format, was fehlt, was sich falsch anfühlt. Zum Beispiel jedes Beispiel kurz und ausführlich, Doku-Links, Live-Demos, Erklärungen zum Aufklappen, später der Umbau zu einer gemeinsamen Website und das Inhaltsverzeichnis.
- **Von Claude:** Texte, Code-Beispiele, Generator, Gestaltung und die Tests im Browser.

Beim Bau wurde geprüft:

- Die Demo-Code-Pfade liefen im Browser mit den echten Bibliotheken: GSAP 3.15 und Three.js r186.
- Die Seiten wurden am Handy und am Desktop, hell und dunkel gerendert.
- Zahlen und Rechtsaussagen im Conversion-Zettel sind mit Quellen verlinkt, Stand Oktober 2026.

## Hinweise

- Die Inhalte sind KI-generiert und mit Sorgfalt geprüft, aber nicht fehlerfrei. Wer einen Fehler findet: gerne ein Issue anlegen.
- Die Karten zum deutschen Recht (Bestell-Button, Cookie-Banner, BFSG) sind keine Rechtsberatung.
- Bibliotheken ändern sich. Versionsangaben beziehen sich auf den Stand beim Erstellen.
