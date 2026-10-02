---
title: "Übergänge: `transition`"
description: "Weiche Übergänge zwischen zwei Zuständen, z.B. beim Hover."
code:
  short: |-
    .button {
      transition: background-color 200ms ease-out, transform 200ms ease-out;
    }
    .button:hover {
      background-color: var(--brand-dark);
      transform: translateY(-2px);
    }
  long: |-
    .button {
      transition-property: background-color, transform;
      transition-duration: 200ms, 200ms;
      transition-timing-function: ease-out, ease-out;
      transition-delay: 0s, 0s;
    }
    .button:hover {
      background-color: var(--brand-dark);
      transform: translateY(-2px);
    }
explain:
  picture: "Ohne `transition` springt das Licht wie bei einem Kippschalter von aus auf an. Mit `transition` ist es ein Dimmer, der in festgelegter Zeit hochfährt."
  steps:
    - "Die `transition` steht auf dem Grundzustand, nicht auf `:hover`. So gilt sie für Hin- und Rückweg."
    - "`transition-property` legt fest, welche Eigenschaften weich wechseln."
    - "`duration` ist die Dauer, `timing-function` die Kurve. `ease-out` startet schnell und bremst sanft ab."
    - "In der Kurzform steht jede Eigenschaft mit ihren Werten, mehrere werden mit Komma getrennt."
  mistake: "`transition: all` benutzen. Dann animiert auch, was nicht animieren soll, z.B. Layout-Änderungen, und das kann ruckeln. Besser gezielt `transform`, `opacity` und Farben animieren, die laufen am flüssigsten."
  when: "Die Kurzform pro Eigenschaft ist üblich. Einzeleigenschaften, wenn du z.B. nur die Dauer in einer Variante änderst."
  question: "Was passiert, wenn die `transition` nur in `.button:hover` steht?"
  answer: "Beim Hineinfahren gibt es einen weichen Übergang, beim Verlassen springt der Button sofort zurück, weil die Regel dann nicht mehr gilt."
links:
  - text: "transition"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/transition"
  - text: "CSS-Übergänge verwenden"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_transitions/Using_CSS_transitions"
---
