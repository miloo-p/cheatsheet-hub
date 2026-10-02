---
title: "Über alle Spalten: `1 / -1`"
description: "Ein Element über mehrere oder alle Spalten strecken, egal wie viele Spalten es gibt."
code:
  short: |-
    .featured {
      grid-column: 1 / -1;
    }
    .wide {
      grid-column: span 2;
    }
  long: |-
    .featured {
      grid-column-start: 1;
      grid-column-end: -1;
    }
    .wide {
      grid-column-start: auto;
      grid-column-end: span 2;
    }
preview:
  height: 200
  html: |-
    <div class="grid"><div class="featured">.featured: 1 / -1</div><div class="wide">.wide: span 2</div><div>3</div><div>4</div><div>5</div><div>6</div></div>
  css: |-
    .featured {
      grid-column: 1 / -1;
    }
    .wide {
      grid-column: span 2;
    }

    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .grid > div { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 10px; font: 600 12px ui-monospace, monospace; }
    .grid > .featured, .grid > .wide { background: var(--brand); color: var(--on-brand); border: 0; }
explain:
  picture: "Gitterlinien sind wie Hausnummern, die man von beiden Enden der Straße zählen kann: von vorne 1, 2, 3, von hinten -1, -2, -3. `1 / -1` heißt: von der ersten bis zur letzten Linie."
  steps:
    - "Ein Grid mit drei Spalten hat vier senkrechte Linien, nummeriert von 1 bis 4."
    - "Negative Zahlen zählen von hinten: `-1` ist immer die letzte Linie."
    - "`grid-column: 1 / -1` spannt das Element daher über alle Spalten, auch wenn `auto-fill` die Spaltenzahl ändert."
    - "`span 2` heißt: zwei Spalten breit, beginnend dort, wo das Element automatisch landen würde."
  mistake: "`grid-column: 1 / 3` schreiben und erwarten, dass das bei vier Spalten immer noch die ganze Breite ist. Feste Liniennummern passen sich nicht an. Und `-1` zählt nur Linien, die im Template definiert sind, nicht automatisch erzeugte Zeilen."
  when: "Die Kurzform `grid-column` fast immer. Die Einzeleigenschaften nur, wenn du gezielt Start oder Ende änderst."
  question: "Über wie viele Spalten erstreckt sich `grid-column: 2 / 4`?"
  answer: "Über zwei: von Linie 2 bis Linie 4, also die zweite und dritte Spalte."
links:
  - text: "grid-column"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/grid-column"
  - text: "Linienbasierte Platzierung"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_grid_layout/Grid_layout_using_line-based_placement"
---
