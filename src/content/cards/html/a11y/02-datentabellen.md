---
title: "Datentabellen"
description: "Tabellarische Daten gehören in eine echte Tabelle, mit Kopfzellen und Beschriftung."
code:
  short: |-
    <table>
      <caption>Bestellungen im Oktober</caption>
      <thead>
        <tr><th scope="col">Datum</th><th scope="col">Betrag</th></tr>
      </thead>
      <tbody>
        <tr><td>01.10.</td><td>49,90 €</td></tr>
      </tbody>
    </table>
  long: |-
    <div class="table" role="table" aria-label="Bestellungen im Oktober">
      <div class="row" role="row">
        <div role="columnheader">Datum</div>
        <div role="columnheader">Betrag</div>
      </div>
      <div class="row" role="row">
        <div role="cell">01.10.</div>
        <div role="cell">49,90 €</div>
      </div>
    </div>
explain:
  picture: "Eine Tabelle ist ein Koordinatensystem. Mit `<th>` weiß ein Screenreader bei jeder Zelle, zu welcher Spalte sie gehört: „Betrag: 49,90 €“. Ohne Kopfzellen hört man nur Zahlen ohne Bedeutung."
  steps:
    - "`<caption>` ist der Titel der Tabelle."
    - "`<thead>` enthält die Kopfzeile, `<tbody>` die Daten."
    - "`<th scope=\"col\">` markiert eine Spaltenüberschrift. Für Zeilenüberschriften gibt es `scope=\"row\"`."
    - "Die div-Variante braucht für jede Zelle eine ARIA-Rolle, um dieselbe Struktur zu beschreiben."
  mistake: "Tabellen für das Seitenlayout benutzen, wie in den 2000ern. Und umgekehrt: echte Daten als div-Raster bauen, nur weil es sich leichter stylen lässt. Tabellen lassen sich heute gut mit CSS gestalten, auf schmalen Bildschirmen z.B. in einem Wrapper mit `overflow-x: auto`."
  when: "`<table>` immer für Daten mit Zeilen und Spalten. Für Layout CSS Grid."
  question: "Links in einer Tabelle stehen die Produktnamen als Zeilenüberschriften. Wie zeichnest du sie aus?"
  answer: "Als `<th scope=\"row\">` statt `<td>` in der ersten Zelle jeder Zeile."
links:
  - text: "<table>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/table"
  - text: "<th>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/th"
  - text: "<caption>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/caption"
---
