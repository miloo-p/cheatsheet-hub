---
title: "Relative Einheiten: `rem` und `em`"
description: "`rem` und `em` passen sich an die Schriftgröße an. So wächst das Layout mit, wenn jemand die Schrift im Browser größer stellt."
code:
  short: |-
    .button {
      font-size: 1rem;
      padding: 0.5em 1em;
    }
    .button.large { font-size: 1.25rem; }
  long: |-
    .button {
      font-size: 16px;
      padding: 8px 16px;
    }
    .button.large {
      font-size: 20px;
      padding: 10px 20px;
    }
explain:
  picture: "`px` ist ein Lineal mit festen Strichen. `rem` und `em` sind wie ein Gummiband, das sich mit der Schriftgröße mitdehnt."
  steps:
    - "`rem` bezieht sich auf die Schriftgröße des `<html>`-Elements, standardmäßig 16px. `1rem` ist also 16px."
    - "`em` bezieht sich auf die Schriftgröße des Elements selbst. Beim großen Button ist `1em` deshalb 20px."
    - "Darum wächst das Padding in der kurzen Variante automatisch mit. Die ausführliche Variante muss jeden Wert einzeln anpassen."
    - "Stellt jemand die Standardschrift im Browser auf 20px, wächst bei `rem` und `em` alles mit, bei `px` nicht."
  mistake: "`em` für Schriftgrößen in verschachtelten Elementen benutzen. `font-size: 1.2em` in einer Liste in einer Liste wird mit jeder Ebene größer, weil es sich auf das Elternelement bezieht. Für Schriftgrößen ist `rem` berechenbarer."
  when: "`rem` für Schriftgrößen und Layoutabstände, `em` für Abstände, die zur Schrift des Elements passen sollen (Button-Padding, Icons). `px` für Rahmen und feine Details."
  question: "Wie groß ist `2rem`, wenn `html { font-size: 20px; }` gesetzt ist?"
  answer: "40px. `rem` bezieht sich immer auf die Schriftgröße des `<html>`-Elements."
links:
  - text: "Werte und Einheiten"
    url: "https://developer.mozilla.org/de/docs/Learn_web_development/Core/Styling_basics/Values_and_units"
  - text: "length"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/length"
---
