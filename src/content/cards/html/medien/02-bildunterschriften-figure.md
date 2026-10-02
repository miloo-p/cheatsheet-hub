---
title: "Bildunterschriften: `<figure>`"
description: "Bild und Bildunterschrift als zusammengehörige Einheit auszeichnen."
code:
  short: |-
    <figure>
      <img src="chart.png" alt="Umsatz steigt von 2 auf 5 Mio. Euro">
      <figcaption>Umsatzentwicklung 2022 bis 2025</figcaption>
    </figure>
  long: |-
    <div class="figure">
      <img src="chart.png" alt="Umsatz steigt von 2 auf 5 Mio. Euro"
           aria-describedby="caption-1">
      <p class="caption" id="caption-1">Umsatzentwicklung 2022 bis 2025</p>
    </div>
explain:
  picture: "`<figure>` ist der Kasten im Schulbuch, in dem Abbildung und „Abb. 3: …“ zusammenstehen. Wird der Kasten verschoben, wandert die Unterschrift mit."
  steps:
    - "`<figure>` umschließt einen in sich geschlossenen Inhalt: Bild, Diagramm, Code-Beispiel oder Zitat."
    - "`<figcaption>` ist die Beschriftung und wird automatisch mit der Figur verknüpft."
    - "Die ausführliche Variante muss diese Verbindung per `aria-describedby` und `id` selbst herstellen."
    - "`alt` und `<figcaption>` haben verschiedene Aufgaben: `alt` ersetzt das Bild, die Bildunterschrift ergänzt es."
  mistake: "Denselben Text in `alt` und `<figcaption>` schreiben. Dann hört ein Screenreader-Nutzer alles doppelt. `alt` beschreibt den Bildinhalt, die Bildunterschrift liefert den Kontext."
  when: "`<figure>` immer, wenn ein Bild eine sichtbare Unterschrift hat. Für Bilder ohne Unterschrift reicht `<img>`."
  question: "Darf `<figure>` auch Code statt eines Bildes enthalten?"
  answer: "Ja. `<figure>` kann jeden eigenständigen Inhalt enthalten, z.B. `<pre><code>` mit der Unterschrift „Beispiel 2: Express-Route“."
links:
  - text: "<figure>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/figure"
  - text: "<figcaption>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/figcaption"
---
