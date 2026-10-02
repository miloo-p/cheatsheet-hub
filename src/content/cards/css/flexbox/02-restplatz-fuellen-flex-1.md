---
title: "Restplatz füllen: `flex: 1`"
description: "Ein Element füllt den restlichen Platz. `flex` fasst drei Eigenschaften zusammen."
code:
  short: |-
    .layout  { display: flex; }
    .sidebar { width: 16rem; }
    .main    { flex: 1; }
  long: |-
    .layout {
      display: flex;
    }
    .sidebar {
      width: 16rem;
    }
    .main {
      flex-grow: 1;
      flex-shrink: 1;
      flex-basis: 0%;
    }
explain:
  picture: "`flex-grow` ist der Hunger eines Elements nach freiem Platz. Wer `1` hat, nimmt sich, was übrig ist. Haben zwei Elemente je `1`, teilen sie fair."
  steps:
    - "`flex-basis` ist die Ausgangsgröße, bevor verteilt wird. Bei `flex: 1` ist sie `0`."
    - "`flex-grow: 1` heißt: Nimm dir einen Anteil vom freien Platz."
    - "`flex-shrink: 1` heißt: Wenn es eng wird, darfst du schrumpfen."
    - "Die Sidebar wächst nicht und behält ihre 16rem, `.main` bekommt den Rest."
  mistake: "Sich wundern, dass lange Wörter oder Code-Blöcke ein Flex-Item trotz `flex: 1` breiter machen. Flex-Items schrumpfen standardmäßig nicht unter die Breite ihres Inhalts. Abhilfe: `min-width: 0` auf dem Item."
  when: "Die Kurzform `flex: 1` ist Standard. Einzeleigenschaften, wenn du nur einen Teil steuern willst, z.B. `flex-shrink: 0` für ein Icon, das nie gestaucht werden soll."
  question: "Zwei Elemente haben `flex: 1` und `flex: 2`. Wie wird der Platz verteilt?"
  answer: "Im Verhältnis 1 zu 2: Das erste bekommt ein Drittel, das zweite zwei Drittel."
links:
  - text: "flex"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/flex"
  - text: "flex-grow"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/flex-grow"
  - text: "flex-basis"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/flex-basis"
---
