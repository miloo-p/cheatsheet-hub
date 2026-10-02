---
title: "Box Model: `box-sizing`"
description: "Mit `border-box` zählen Padding und Rahmen zur angegebenen Breite. Ohne musst du selbst rechnen."
code:
  short: |-
    *, *::before, *::after {
      box-sizing: border-box;
    }

    .card {
      width: 300px;
      padding: 20px;
      border: 1px solid #ccc;
    }
  long: |-
    /* Standard: box-sizing: content-box */
    .card {
      width: 258px; /* 300 - 2 × 20 Padding - 2 × 1 Rahmen */
      padding: 20px;
      border: 1px solid #ccc;
    }
preview:
  height: 210
  html: |-
    <div class="ruler">300px</div>
    <div class="card">border-box: außen genau 300px</div>
    <div class="card legacy">content-box: 300 + 40 + 2 = 342px</div>
  css: |-
    *, *::before, *::after {
      box-sizing: border-box;
    }

    .card {
      width: 300px;
      padding: 20px;
      border: 1px solid #ccc;
    }

    /* zum Vergleich: der alte Standard */
    .card.legacy { box-sizing: content-box; border-color: var(--accent2); }

    .card { background: var(--surface); border-radius: 6px; margin-bottom: 8px; }
    .ruler { width: 300px; border-bottom: 2px solid var(--brand); color: var(--brand);
             font: 11px ui-monospace, monospace; text-align: center; margin-bottom: 6px; }
explain:
  picture: "Stell dir einen Bilderrahmen vor. Bei `content-box` gibst du die Größe des Bildes an, und Passepartout und Rahmen kommen außen dazu. Bei `border-box` gibst du die Außenmaße des ganzen Rahmens an, und das Bild passt sich innen an."
  steps:
    - "Jedes Element besteht von innen nach außen aus Inhalt, Padding, Rahmen (border) und Außenabstand (margin)."
    - "Standard ist `content-box`: `width` gilt nur für den Inhalt. Padding und Rahmen kommen obendrauf, aus 300px werden 342px."
    - "Mit `border-box` gilt `width` für Inhalt, Padding und Rahmen zusammen. Die Box ist genau 300px breit."
    - "Margin zählt in beiden Fällen nicht zur Breite."
  mistake: "Zwei Spalten mit `width: 50%` und Padding nebeneinandersetzen. Mit `content-box` sind sie zusammen breiter als 100%, und die zweite rutscht in die nächste Zeile."
  when: "Die globale `border-box`-Regel gehört an den Anfang fast jedes Stylesheets, die meisten CSS-Resets enthalten sie. Die Rechnung aus der ausführlichen Variante musst du verstehen, aber nicht benutzen."
  question: "Wie breit ist `.box { width: 200px; padding: 10px; border: 5px solid; }` mit `content-box`?"
  answer: "230px: 200 Inhalt + 2 × 10 Padding + 2 × 5 Rahmen. Mit `border-box` wären es genau 200px."
links:
  - text: "box-sizing"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/box-sizing"
  - text: "Das Box-Modell"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_box_model/Introduction_to_the_CSS_box_model"
---
