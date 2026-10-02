---
title: "Über Objekte iterieren"
description: "`Object.entries` macht aus einem Objekt ein Array aus `[key, value]`-Paaren."
code:
  short: |-
    const scores = { anna: 3, ben: 5 };
    const lines = Object.entries(scores)
      .map(([name, s]) => `${name}: ${s}`);
  long: |-
    const scores = { anna: 3, ben: 5 };
    const lines = [];
    for (const name in scores) {
      const score = scores[name];
      lines.push(name + ": " + score);
    }
explain:
  picture: "Objekte sind keine Listen, darum kannst du nicht direkt `map` darauf aufrufen. `Object.entries` legt das Objekt wie eine Tabelle aus: jede Zeile ein Paar aus Schlüssel und Wert."
  steps:
    - "`Object.entries(scores)` ergibt `[[\"anna\", 3], [\"ben\", 5]]`."
    - "Auf diesem Array funktioniert `map` wie gewohnt."
    - "`([name, s]) => ...` packt jedes Paar per Array-Destructuring in zwei Variablen aus."
    - "`for...in` läuft direkt über die Schlüssel eines Objekts. Den Wert holst du dir mit `scores[name]`."
  mistake: "`for...in` und `for...of` verwechseln. `for...in` liefert Schlüssel (bei Arrays die Indizes als Strings), `for...of` liefert Werte und funktioniert nicht auf normalen Objekten."
  when: "`Object.entries` plus `map`, wenn ein neues Array entstehen soll, z.B. JSX. `for...in` für einfache Durchläufe ohne Ergebnis-Array."
  question: "Was passiert bei `for (const x of { a: 1 })`?"
  answer: "Ein TypeError, weil ein normales Objekt nicht iterierbar ist. Du brauchst `Object.entries`, `Object.keys` oder `for...in`."
links:
  - text: "Object.entries()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Object/entries"
  - text: "for...in"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/for...in"
  - text: "for...of"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/for...of"
---
