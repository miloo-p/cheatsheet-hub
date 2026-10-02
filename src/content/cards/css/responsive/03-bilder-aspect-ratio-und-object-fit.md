---
title: "Bilder: `aspect-ratio` und `object-fit`"
description: "Bilder in einem festen Seitenverhältnis anzeigen, ohne sie zu verzerren."
code:
  short: |-
    .thumb {
      width: 100%;
      aspect-ratio: 16 / 9;
      object-fit: cover;
    }
  long: |-
    /* HTML: <div class="thumb"><img src="..."></div> */
    .thumb {
      position: relative;
      padding-top: 56.25%; /* 9 / 16 = 0.5625 */
    }
    .thumb img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
explain:
  picture: "`object-fit: cover` ist wie ein Foto, das im Bilderrahmen so weit vergrößert wird, bis kein Rand mehr frei bleibt. Was übersteht, wird abgeschnitten, aber nichts wird gestaucht."
  steps:
    - "`aspect-ratio: 16 / 9` berechnet die Höhe aus der Breite."
    - "Ohne `object-fit` würde das Bild auf genau diese Fläche gestreckt und verzerrt."
    - "`object-fit: cover` füllt die Fläche und schneidet den Überstand ab. `contain` zeigt dagegen das ganze Bild, mit freien Rändern."
    - "Die ausführliche Variante ist der alte Padding-Trick: Prozentwerte bei `padding-top` beziehen sich auf die Breite, deshalb ergibt 56.25% genau 16:9."
  mistake: "Bildern im HTML keine `width` und `height` geben. Dann weiß der Browser vor dem Laden nicht, wie viel Platz er reservieren soll, und die Seite springt, sobald das Bild erscheint (Layout Shift)."
  when: "`aspect-ratio` heute immer. Den Padding-Trick musst du nur in älterem Code erkennen."
  question: "Welches Seitenverhältnis ergibt `padding-top: 100%`?"
  answer: "1:1, also ein Quadrat, weil das Padding 100% der Breite beträgt."
links:
  - text: "aspect-ratio"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/aspect-ratio"
  - text: "object-fit"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/object-fit"
---
