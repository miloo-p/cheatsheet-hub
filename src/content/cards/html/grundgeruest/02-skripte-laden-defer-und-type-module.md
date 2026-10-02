---
title: "Skripte laden: `defer` und `type=\"module\"`"
description: "Skripte so einbinden, dass sie die Seite nicht blockieren und das HTML schon da ist, wenn sie laufen."
code:
  short: |-
    <head>
      <script src="app.js" defer></script>
      <!-- oder als ES-Modul, automatisch verzögert -->
      <script type="module" src="main.js"></script>
    </head>
  long: |-
    <body>
      ...
      <!-- ganz unten, damit das HTML vorher eingelesen ist -->
      <script src="app.js"></script>
      <script>
        document.addEventListener("DOMContentLoaded", function () {
          init();
        });
      </script>
    </body>
explain:
  picture: "Ohne `defer` hält der Browser beim Lesen des HTML an jedem Skript an, wie jemand, der mitten im Satz aufsteht, um ein Buch zu holen. Mit `defer` wird das Buch nebenbei geholt und erst gelesen, wenn die Seite fertig ist."
  steps:
    - "Ein normales `<script>` stoppt das Einlesen des HTML, bis das Skript geladen und ausgeführt ist."
    - "Steht es im `<head>`, existieren die Elemente im `<body>` noch nicht. `document.querySelector` findet dann nichts."
    - "`defer` lädt das Skript parallel und führt es erst aus, wenn das HTML komplett eingelesen ist, in der Reihenfolge der Skripte."
    - "`type=\"module\"` verhält sich automatisch wie `defer` und erlaubt `import` und `export`. Vite erzeugt genau das."
    - "Die ausführliche Variante erreicht dasselbe mit Skripten am Ende des `<body>` und dem Event `DOMContentLoaded`."
  mistake: "Ein Skript ohne `defer` in den `<head>` setzen und sich wundern, warum `document.querySelector(\"#app\")` `null` liefert. Das Element gibt es zu diesem Zeitpunkt noch nicht."
  when: "`defer` oder `type=\"module\"` im `<head>`. Skripte am Ende des Body sind der klassische Weg, der genauso funktioniert, aber später mit dem Laden beginnt."
  question: "Was ist der Unterschied zwischen `defer` und `async`?"
  answer: "Beide laden parallel. `defer` wartet mit dem Ausführen, bis das HTML fertig ist, und hält die Reihenfolge ein. `async` führt sofort nach dem Laden aus, in beliebiger Reihenfolge. Das passt für unabhängige Skripte wie Statistik-Tools."
links:
  - text: "<script>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/script"
  - text: "JavaScript-Module"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Guide/Modules"
  - text: "DOMContentLoaded"
    url: "https://developer.mozilla.org/de/docs/Web/API/Document/DOMContentLoaded_event"
---
