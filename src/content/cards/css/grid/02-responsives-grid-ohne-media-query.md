---
title: "Responsives Grid ohne Media Query"
description: "Das Grid berechnet selbst, wie viele Spalten passen. Ganz ohne Breakpoints."
code:
  short: |-
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
      gap: 1rem;
    }
  long: |-
    .cards {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
    }
    @media (width >= 36rem) {
      .cards { grid-template-columns: repeat(2, 1fr); }
    }
    @media (width >= 54rem) {
      .cards { grid-template-columns: repeat(3, 1fr); }
    }
    @media (width >= 72rem) {
      .cards { grid-template-columns: repeat(4, 1fr); }
    }
preview:
  height: 200
  sizes: [375, 800, 1200]
  html: |-
    <div class="cards"><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div></div>
    <p class="hint">Breite umschalten: Die Spaltenzahl passt sich ohne Media Query an.</p>
  css: |-
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
      gap: 1rem;
    }

    .cards > div { background: var(--surface); border: 1px solid var(--line); border-top: 4px solid var(--brand); border-radius: 8px; padding: 14px; font-weight: 600; }
explain:
  picture: "Wie beim Fliesenlegen: Du sagst nur, wie groß eine Fliese mindestens sein soll, und der Fliesenleger rechnet selbst aus, wie viele in eine Reihe passen."
  steps:
    - "`minmax(16rem, 1fr)` heißt: Jede Spalte ist mindestens 16rem breit und darf wachsen."
    - "`auto-fill` legt so viele Spalten an, wie mit mindestens 16rem hineinpassen."
    - "Der übrige Platz wird über `1fr` gleichmäßig auf die Spalten verteilt."
    - "Wird das Fenster schmaler, fällt automatisch eine Spalte weg. Die Media-Query-Variante macht dasselbe in festen Stufen."
  mistake: "`auto-fill` und `auto-fit` verwechseln. Bei wenigen Karten legt `auto-fill` leere Spalten an und die Karten bleiben schmal, `auto-fit` lässt die vorhandenen Karten in den freien Platz wachsen. Außerdem läuft das Grid auf Bildschirmen unter 16rem über. Abhilfe: `minmax(min(16rem, 100%), 1fr)`."
  when: "`auto-fill` mit `minmax` für Kartenraster, Galerien und Produktlisten. Media Queries, wenn sich das Layout an bestimmten Breiten grundlegend ändern soll."
  question: "Wie viele Spalten entstehen bei `repeat(auto-fill, minmax(200px, 1fr))` in einem 650px breiten Container ohne gap?"
  answer: "Drei. Vier Spalten bräuchten mindestens 800px. Die drei Spalten werden dann auf je etwa 217px gestreckt."
links:
  - text: "repeat() mit auto-fill"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/repeat"
  - text: "minmax()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/minmax"
---
