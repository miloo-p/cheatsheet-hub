---
title: "Fließende Größen: `clamp()`"
description: "Schriftgrößen und Abstände, die mit dem Bildschirm wachsen, aber Grenzen einhalten."
code:
  short: |-
    h1 {
      font-size: clamp(1.75rem, 1rem + 3vw, 3rem);
    }
  long: |-
    h1 {
      font-size: 1.75rem;
    }
    @media (width >= 40rem) {
      h1 { font-size: 2.25rem; }
    }
    @media (width >= 64rem) {
      h1 { font-size: 3rem; }
    }
preview:
  height: 150
  sizes: [375, 768, 1280]
  html: |-
    <h1>Fließende Überschrift</h1>
    <p class="hint">Breite umschalten: Die Schrift wächst stufenlos zwischen 1.75rem und 3rem.</p>
  css: |-
    h1 {
      font-size: clamp(1.75rem, 1rem + 3vw, 3rem);
    }

    h1 { margin: 8px 0; line-height: 1.1; }
explain:
  picture: "`clamp()` ist ein Thermostat mit Unter- und Obergrenze: Dazwischen regelt es frei, aber es wird nie kälter als das Minimum und nie wärmer als das Maximum."
  steps:
    - "`clamp(MIN, WUNSCH, MAX)` nimmt den Wunschwert, solange er zwischen den Grenzen liegt."
    - "Der Wunschwert `1rem + 3vw` wächst mit der Fensterbreite, weil `1vw` ein Prozent der Viewport-Breite ist."
    - "Auf dem Handy greift das Minimum 1.75rem, auf großen Bildschirmen das Maximum 3rem."
    - "Die Media-Query-Variante springt in Stufen, `clamp()` wächst stufenlos."
  mistake: "Nur `vw` als Wunschwert nehmen, z.B. `clamp(1rem, 4vw, 3rem)`. Reine `vw`-Werte reagieren schlecht auf Browser-Zoom. Ein `rem`-Anteil wie in `1rem + 3vw` hält die Schrift zoombar."
  when: "`clamp()` für Überschriften, Abschnittsabstände und Container-Padding. Media Queries, wenn sich nicht nur Größen, sondern das Layout ändert."
  question: "Welchen Wert ergibt `clamp(10px, 50px, 30px)`?"
  answer: "30px. Der Wunschwert 50px liegt über dem Maximum, also greift die Obergrenze."
links:
  - text: "clamp()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/clamp"
  - text: "min()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/min"
  - text: "max()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/max"
---
