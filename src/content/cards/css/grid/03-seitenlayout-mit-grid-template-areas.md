---
title: "Seitenlayout mit `grid-template-areas`"
description: "Das Seitenlayout als lesbare Skizze im CSS, statt mit Liniennummern."
code:
  short: |-
    .page {
      display: grid;
      grid-template-columns: 16rem 1fr;
      grid-template-areas:
        "header  header"
        "sidebar main"
        "footer  footer";
    }
    .page > header { grid-area: header; }
    .page > aside  { grid-area: sidebar; }
    .page > main   { grid-area: main; }
    .page > footer { grid-area: footer; }
  long: |-
    .page {
      display: grid;
      grid-template-columns: 16rem 1fr;
    }
    .page > header { grid-column: 1 / 3; grid-row: 1; }
    .page > aside  { grid-column: 1;     grid-row: 2; }
    .page > main   { grid-column: 2;     grid-row: 2; }
    .page > footer { grid-column: 1 / 3; grid-row: 3; }
explain:
  picture: "`grid-template-areas` ist ein Grundriss in ASCII-Art: Du zeichnest im CSS auf, welcher Raum wo liegt."
  steps:
    - "Jeder String in `grid-template-areas` ist eine Zeile, jedes Wort darin eine Zelle."
    - "Steht ein Name mehrfach nebeneinander, erstreckt sich der Bereich über diese Zellen."
    - "Mit `grid-area: header` legst du ein Element in den gleichnamigen Bereich."
    - "Die ausführliche Variante beschreibt dasselbe über Gitterlinien: `1 / 3` heißt von Linie 1 bis Linie 3, also über zwei Spalten."
  mistake: "Nicht rechteckige Bereiche zeichnen, z.B. ein L aus `sidebar`. Dann ist die ganze Eigenschaft ungültig, und der Browser ignoriert sie ohne Fehlermeldung."
  when: "Areas für Seitenlayouts, besonders responsiv: In einer Media Query zeichnest du einfach einen neuen Grundriss. Liniennummern für einzelne Elemente, die etwas überspannen sollen."
  question: "Wie sieht der Grundriss fürs Handy aus, wenn alles untereinander stehen soll?"
  answer: "`grid-template-columns: 1fr;` und `grid-template-areas: \"header\" \"main\" \"sidebar\" \"footer\";`. Die Elemente selbst musst du nicht anfassen."
links:
  - text: "Grid Template Areas"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_grid_layout/Grid_template_areas"
  - text: "grid-area"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/grid-area"
---
