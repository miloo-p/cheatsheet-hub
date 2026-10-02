# Cheatsheet Hub

**Live: https://miloo-p.github.io/cheatsheet-hub/**

Mein persönliches Glossar aus dem Frontend-Teil meines Fullstack-Bootcamps. Hier sammle ich, was ich gelernt habe, damit es nicht verloren geht, während ich im Backend-Modul stecke.

Das Projekt ist **vibe-gecodet**: Inhalte und Website sind im Gespräch mit Claude (KI von Anthropic) entstanden. Ich habe Richtung, Themen und Aufbau vorgegeben, Claude hat geschrieben, gebaut und getestet. Mehr dazu unter [Wie das entstanden ist](#wie-das-entstanden-ist).

Gebaut ist die Seite mit [Astro](https://astro.build): Jede Karte ist eine eigene Markdown-Datei, Astro macht daraus beim Bauen statische HTML-Seiten.

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
- **Vorschau** bei CSS: Das Ergebnis des Beispiels direkt unter dem Code, isoliert in einem eigenen Rahmen. Bei responsiven Themen lässt sich die Breite umschalten.
- **Live-Demo** bei GSAP und Three.js. Die Bibliotheken werden erst beim ersten Klick geladen.

### Bedienung

- **Startseite mit Volltextsuche:** Die Suche durchsucht alle Zettel inklusive der Erklärungen und springt direkt zur Karte.
- **Inhaltsverzeichnis auf jeder Seite:** Am Desktop als Seitenleiste, die die aktuelle Karte markiert. Am Handy im Menü.
- **Filter pro Seite.** Zusätzlich lässt sich umschalten, ob beide Code-Varianten oder nur eine angezeigt werden.
- **Syntax-Highlighting** mit Shiki, schon beim Bauen erzeugt.
- **Kopieren-Button** an jedem Code-Block und ein **Link** an jeder Karte.
- **Hell und dunkel:** passt sich dem System an.
- **Handytauglich:** Die Leiste blendet sich beim Scrollen aus.

## Lokal starten

Voraussetzung ist Node.js ab Version 22.12.

```bash
npm install
npm run dev       # Entwicklungsserver auf http://localhost:4321/cheatsheet-hub/
npm run build     # fertige Seite nach dist/
npm run preview   # dist/ lokal ansehen
```

Veröffentlicht wird automatisch: Jeder Push auf `main` startet den Workflow `.github/workflows/pages.yml`. Er baut die Seite und stellt sie auf GitHub Pages. Auf anderen Branches wird nur gebaut, so fallen Fehler vor dem Merge auf.

## Projektstruktur

```
src/
  content/
    sheets/<zettel>.md                    ein Zettel: Titel, Farben, Texte, Abschnitte
    cards/<zettel>/<abschnitt>/NN-*.md    eine Karte pro Datei
  content.config.ts                       Schema beider Sammlungen, prüft jede Datei beim Bauen
  pages/
    index.astro                           Startseite mit Bereichen und Suche
    [zettel].astro                        eine Seite pro Zettel, z.B. /css/
    search.json.ts                        Suchindex für die Startseite
  components/                             Karte, Erklärung, Vorschau, Live-Demo, Inhaltsverzeichnis, Farben
  lib/                                    Laden der Inhalte, Inline-Markdown, Loader für Demos
  scripts/                                Browser-Logik: Filter, Menüs, Kopieren, Demos, Suche
  styles/                                 gemeinsame Gestaltung und Startseite
  data/hub.ts                             Themenbereiche und geplante Zettel
```

## Inhalte ändern und erweitern

Alle Inhalte liegen in `src/content/`. Beim Bauen prüft Astro jede Datei gegen das Schema in `src/content.config.ts`. Fehlt ein Feld oder ist ein Link kaputt, bricht der Build mit einer verständlichen Meldung ab.

**Karte ändern:** Die passende Datei öffnen, Text oder Code anpassen, speichern. Im Entwicklungsserver ist die Änderung sofort zu sehen.

So sieht eine Karte aus:

```yaml
---
title: "Box Model: `box-sizing`"
description: "Mit `border-box` zählen Padding und Rahmen zur angegebenen Breite."
code:
  short: |-
    *, *::before, *::after { box-sizing: border-box; }
  long: |-
    .card { width: 258px; /* 300 - 2 × 20 Padding - 2 × 1 Rahmen */ }
explain:
  picture: "Stell dir einen Bilderrahmen vor …"
  steps:
    - "Jedes Element besteht von innen nach außen aus …"
  mistake: "Zwei Spalten mit `width: 50%` und Padding …"
  when: "Die globale `border-box`-Regel gehört an den Anfang …"
  question: "Wie breit ist …?"
  answer: "230px: …"
links:
  - text: "box-sizing"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/box-sizing"
---

Optional: eigene Notizen in Markdown. Sie erscheinen unter der Karte.
```

- In allen Texten funktionieren `Code`, `**fett**` und `[Links](/css/)`. Links mit `/` am Anfang zeigen auf Seiten dieser Website.
- `lang` legt bei Bedarf die Sprache fürs Highlighting fest, z.B. `lang: { short: tsx }`. Sonst gilt die Sprache des Zettels.
- `preview` zeigt HTML und CSS als Vorschau, siehe die Karten in `cards/css/`. Mit `sizes: [375, 1200]` lässt sich die Breite umschalten, mit `replay: true` eine Animation neu starten. Variablen wie `--brand`, `--surface` und `--line` stehen in jeder Vorschau bereit.
- `demo` fügt eine Live-Demo mit JavaScript hinzu, siehe die Karten in `cards/gsap/`.

**Neue Karte:** Datei im passenden Abschnitt anlegen. Die Nummer am Anfang des Dateinamens bestimmt die Reihenfolge und den Anker, z.B. wird `cards/css/grid/03-*.md` zu `/css/#css-grid-3`.

**Neuer Abschnitt:** In `sheets/<zettel>.md` unter `sections` eintragen und einen gleichnamigen Ordner unter `cards/<zettel>/` anlegen.

**Neuer Zettel:**
1. `src/content/sheets/neu.md` nach dem Muster der anderen Dateien anlegen: Name, Bereich, Farben, Texte, Abschnitte.
2. Karten unter `src/content/cards/neu/<abschnitt>/` anlegen.
3. Fertig. Startseite, Suche und Navigation übernehmen den Zettel automatisch.

Ideen für die nächsten Zettel: Node & Express, SQL & Datenbanken, React Hooks, Git.

## Wie das entstanden ist

Angefangen hat es mit einer einfachen Frage: Wie halte ich mein Frontend-Wissen frisch, während das Bootcamp im Backend weitergeht? Daraus wurde zuerst eine Liste mit JavaScript-Konzepten, dann ein Spickzettel, dann mehrere. Am Ende stand eine eigene kleine Website.

Die erste Version wurde von Python-Skripten erzeugt. Weil Inhalte und Darstellung dort eng verwoben waren, ist das Projekt danach auf Astro umgezogen: Jede Karte ist jetzt eine eigene Datei, und Layout, Menüs, Inhaltsverzeichnis und Demos sind Komponenten. Die Inhalte wurden dabei per Skript übernommen und Karte für Karte mit der alten Version verglichen.

Die Arbeitsteilung:

- **Von mir:** welche Themen, welches Format, was fehlt, was sich falsch anfühlt. Zum Beispiel jedes Beispiel kurz und ausführlich, Doku-Links, Live-Demos, Erklärungen zum Aufklappen, die gemeinsame Website, das Inhaltsverzeichnis und der Umzug auf Astro.
- **Von Claude:** Texte, Code-Beispiele, Umsetzung, Gestaltung und die Tests im Browser.

Beim Bau wurde geprüft:

- Die Demo-Code-Pfade liefen im Browser mit den echten Bibliotheken: GSAP 3.15 und Three.js r186.
- Die Seiten wurden am Handy und am Desktop, hell und dunkel gerendert.
- Zahlen und Rechtsaussagen im Conversion-Zettel sind mit Quellen verlinkt, Stand Oktober 2026.

## Hinweise

- Die Inhalte sind KI-generiert und mit Sorgfalt geprüft, aber nicht fehlerfrei. Wer einen Fehler findet: gerne ein Issue anlegen.
- Die Karten zum deutschen Recht (Bestell-Button, Cookie-Banner, BFSG) sind keine Rechtsberatung.
- Bibliotheken ändern sich. Versionsangaben beziehen sich auf den Stand beim Erstellen.
