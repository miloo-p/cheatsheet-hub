---
title: "Spalten mit `repeat()` und `fr`"
description: "Ein Raster mit gleich breiten Spalten. `fr` steht für einen Anteil am freien Platz."
code:
  short: |-
    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }
  long: |-
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      row-gap: 1.5rem;
      column-gap: 1.5rem;
    }
preview:
  height: 170
  html: |-
    <div class="grid"><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div></div>
  css: |-
    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }

    .grid > div { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 14px; text-align: center; font-weight: 600; }
explain:
  picture: "`fr` funktioniert wie Pizzastücke: `1fr 1fr 1fr` teilt die Pizza in drei gleiche Stücke, `2fr 1fr` gibt einer Spalte doppelt so viel."
  steps:
    - "`display: grid` macht das Element zum Raster, die Kinder werden automatisch auf die Zellen verteilt."
    - "`grid-template-columns` legt die Spalten fest. Zeilen entstehen automatisch nach Bedarf."
    - "`1fr` heißt: ein Anteil am Platz, der nach festen Größen und Abständen übrig bleibt."
    - "`repeat(3, 1fr)` ist die Kurzform für `1fr 1fr 1fr`. Bei 12 Spalten spart das viel Tipparbeit."
  mistake: "Prozentwerte zusammen mit `gap` verwenden: `33.33% 33.33% 33.33%` plus Abstände wird zu breit. `fr` rechnet die Abstände automatisch heraus."
  when: "`repeat()` ab drei gleichen Spalten. Ausgeschrieben, wenn die Spalten verschieden sind, z.B. `16rem 1fr` für Sidebar und Inhalt."
  question: "Wie breit sind die Spalten bei `grid-template-columns: 200px 1fr 1fr` in einem 800px breiten Grid ohne gap?"
  answer: "200px, 300px und 300px. Erst wird die feste Spalte abgezogen, die übrigen 600px werden auf zwei Anteile verteilt."
links:
  - text: "grid-template-columns"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/grid-template-columns"
  - text: "repeat()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/repeat"
  - text: "Grid-Grundlagen"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_grid_layout/Basic_concepts_of_grid_layout"
---
