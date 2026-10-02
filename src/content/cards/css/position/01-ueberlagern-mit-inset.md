---
title: "Überlagern mit `inset`"
description: "Ein Element exakt über ein anderes legen, z.B. ein Overlay über ein Bild."
code:
  short: |-
    .card { position: relative; }

    .card .overlay {
      position: absolute;
      inset: 0;
    }
  long: |-
    .card {
      position: relative;
    }
    .card .overlay {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
    }
preview:
  height: 170
  html: |-
    <div class="card">
      <div class="photo"></div>
      <div class="overlay"><b>Bildunterschrift</b><span>liegt genau über der Karte</span></div>
    </div>
  css: |-
    .card { position: relative; }

    .card .overlay {
      position: absolute;
      inset: 0;
    }

    .card { max-width: 320px; border-radius: 10px; overflow: hidden; }
    .photo { height: 140px; background: linear-gradient(135deg, #177258, #6fd3ad 60%, #f0c35a); }
    .overlay { display: flex; flex-direction: column; justify-content: flex-end; padding: 12px; color: #fff;
               background: linear-gradient(to top, rgb(0 0 0 / .6), transparent 60%); }
    .overlay span { font-size: 12px; opacity: .85; }
explain:
  picture: "`position: relative` beim Elternelement schlägt einen Nagel ein. `position: absolute` beim Kind hängt es an diesem Nagel auf, statt am Rand der ganzen Seite."
  steps:
    - "`position: absolute` nimmt das Element aus dem normalen Fluss. Die anderen Elemente verhalten sich, als gäbe es es nicht."
    - "Positioniert wird relativ zum nächsten Vorfahren, dessen `position` nicht `static` ist. Darum `position: relative` auf `.card`."
    - "`top`, `right`, `bottom` und `left` auf 0 ziehen das Element an alle vier Kanten, es füllt die Karte komplett aus."
    - "`inset: 0` ist die Kurzform dafür und folgt derselben Reihenfolge wie `margin`."
  mistake: "`position: relative` beim Elternelement vergessen. Dann orientiert sich das Overlay am nächsthöheren positionierten Element, oft an der ganzen Seite, und bedeckt plötzlich alles."
  when: "`inset` ist kürzer und läuft in allen aktuellen Browsern. Einzelwerte, wenn du nur an einer Ecke positionierst, z.B. ein Badge mit `top: 0.5rem; right: 0.5rem`."
  question: "Was bedeutet `inset: 1rem 2rem`?"
  answer: "Oben und unten 1rem, rechts und links 2rem Abstand zum Bezugselement, wie bei `margin`."
links:
  - text: "inset"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/inset"
  - text: "position"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/position"
---
