---
title: "Umbrechende Reihen: `flex-wrap`"
description: "Elemente nebeneinander, die bei wenig Platz automatisch in die nächste Zeile umbrechen."
code:
  short: |-
    .cards {
      display: flex;
      flex-flow: row wrap;
      gap: 1rem;
    }
    .card { flex: 1 1 16rem; }
  long: |-
    .cards {
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      row-gap: 1rem;
      column-gap: 1rem;
    }
    .card {
      flex-grow: 1;
      flex-shrink: 1;
      flex-basis: 16rem;
    }
explain:
  picture: "Wie Bücher im Regal: Passt keins mehr in die Reihe, kommt das nächste aufs Brett darunter. `flex-grow` sorgt dafür, dass die Bücher einer Reihe die Lücke am Ende auffüllen."
  steps:
    - "`flex-wrap: wrap` erlaubt Umbrüche. Ohne werden alle Items in eine Zeile gequetscht."
    - "`flex-basis: 16rem` ist die Wunschbreite jedes Elements."
    - "Passen nicht mehr alle mit 16rem in die Zeile, bricht das letzte um."
    - "`flex-grow: 1` lässt die Elemente jeder Zeile wachsen, bis die Zeile voll ist."
  mistake: "Die letzte Zeile sieht anders aus: Bleibt eine einzelne Karte übrig, wächst sie über die ganze Breite. Sollen alle Karten gleich breit sein, ist Grid mit `auto-fill` die bessere Wahl (siehe Grid)."
  when: "Flexbox mit Umbruch für Elemente unterschiedlicher Breite, z.B. Tags oder Buttons. Für gleichmäßige Kartenraster Grid."
  question: "Welche zwei Eigenschaften fasst `flex-flow` zusammen?"
  answer: "`flex-direction` und `flex-wrap`."
links:
  - text: "flex-wrap"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/flex-wrap"
  - text: "flex-flow"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/flex-flow"
  - text: "flex-basis"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/flex-basis"
---
