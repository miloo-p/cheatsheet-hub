---
title: "Kurzformen: `border`, `background`, `font`"
description: "Mehrere zusammengehörige Eigenschaften in einer Zeile."
code:
  short: |-
    .card {
      border: 1px solid #dde1e8;
      background: #fff url("dots.svg") no-repeat right top;
      font: 600 1rem/1.5 "IBM Plex Sans", sans-serif;
    }
  long: |-
    .card {
      border-width: 1px;
      border-style: solid;
      border-color: #dde1e8;

      background-color: #fff;
      background-image: url("dots.svg");
      background-repeat: no-repeat;
      background-position: right top;

      font-weight: 600;
      font-size: 1rem;
      line-height: 1.5;
      font-family: "IBM Plex Sans", sans-serif;
    }
explain:
  picture: "Eine Kurzschreibweise ist ein Bestellformular mit Sammelfeld: Du füllst eine Zeile aus, und das System verteilt die Angaben auf die einzelnen Felder."
  steps:
    - "`border` braucht Breite, Stil und Farbe. Ohne Stil wie `solid` ist kein Rahmen zu sehen."
    - "Bei `background` ist die Reihenfolge weitgehend frei. Der Browser erkennt an den Werten, was Farbe, Bild oder Position ist."
    - "`font` ist strenger: Schriftgröße und Schriftfamilie sind Pflicht und stehen am Ende, die Zeilenhöhe folgt mit Schrägstrich auf die Größe."
    - "Alles, was du in einer Kurzform weglässt, wird auf den Standardwert zurückgesetzt."
  mistake: "`background: url(...)` schreiben, nachdem vorher `background-color` gesetzt war. Die Kurzform setzt die Farbe dabei auf transparent zurück. Dasselbe passiert bei `font`, das unter anderem die Zeilenhöhe zurücksetzt."
  when: "`border` fast immer als Kurzform. Bei `background` und `font` sind Einzeleigenschaften oft sicherer und lesbarer, besonders wenn du nur einen Teil ändern willst."
  question: "Warum ist bei `border: 2px red;` kein Rahmen zu sehen?"
  answer: "Der Stil fehlt. Der Standardwert von `border-style` ist `none`, also wird nichts gezeichnet. Richtig ist z.B. `border: 2px solid red;`."
links:
  - text: "border"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/border"
  - text: "background"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/background"
  - text: "font"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/font"
  - text: "Kurzschreibweisen"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/Shorthand_properties"
---
