---
title: "Zentrieren"
description: "Ein Element horizontal und vertikal in die Mitte setzen."
code:
  short: |-
    .hero {
      display: grid;
      place-items: center;
      min-height: 60vh;
    }
  long: |-
    .hero {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 60vh;
    }
explain:
  picture: "Flexbox hat zwei Achsen wie ein Kreuz: Die Hauptachse läuft in Leserichtung, die Querachse quer dazu. Zentrieren heißt, auf beiden Achsen in die Mitte zu rücken."
  steps:
    - "`display: flex` macht die Kinder zu Flex-Items, die in einer Reihe liegen."
    - "`justify-content: center` zentriert auf der Hauptachse, bei `row` also horizontal."
    - "`align-items: center` zentriert auf der Querachse, bei `row` also vertikal."
    - "`place-items: center` im Grid ist die Kurzform für `align-items` und `justify-items` zusammen. Ein Grid mit einem Kind braucht nur diese eine Zeile."
  mistake: "Vertikales Zentrieren ohne Höhe erwarten. Ist der Container nur so hoch wie sein Inhalt, gibt es keinen Platz zum Zentrieren. Darum hier `min-height`."
  when: "Grid mit `place-items` für ein einzelnes zentriertes Element. Flexbox, wenn mehrere Elemente in einer Reihe zentriert und verteilt werden sollen."
  question: "Was ändert sich in der Flex-Variante, wenn du `flex-direction: column` ergänzt?"
  answer: "Die Achsen tauschen: `justify-content` wirkt dann vertikal, `align-items` horizontal. Das Element bleibt trotzdem mittig, weil beide auf `center` stehen."
links:
  - text: "Flexbox-Grundlagen"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox"
  - text: "place-items"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/place-items"
  - text: "justify-content"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/justify-content"
  - text: "align-items"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/align-items"
---
