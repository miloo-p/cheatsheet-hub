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
preview:
  height: 220
  html: |-
    <div class="row">
      <figure><img class="thumb" alt="" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Crect width='200' height='200' fill='%23177258'/%3E%3Ccircle cx='100' cy='100' r='70' fill='%23f0c35a'/%3E%3Ccircle cx='100' cy='100' r='30' fill='%23a8452a'/%3E%3C/svg%3E"><figcaption>quadratisches Bild, 16:9 zugeschnitten</figcaption></figure>
      <figure><img class="thumb" alt="" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='100'%3E%3Crect width='400' height='100' fill='%232b5fae'/%3E%3Ccircle cx='200' cy='50' r='40' fill='%23f0c35a'/%3E%3C/svg%3E"><figcaption>Panorama, ebenfalls 16:9</figcaption></figure>
    </div>
  css: |-
    .thumb {
      width: 100%;
      aspect-ratio: 16 / 9;
      object-fit: cover;
    }

    .row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
    figure { margin: 0; }
    .thumb { display: block; border-radius: 8px; }
    figcaption { font-size: 12px; color: var(--muted); margin-top: 4px; }
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
