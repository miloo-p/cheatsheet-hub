---
title: "Truthy / Falsy und `===`"
description: "Falsy sind nur `false, 0, \"\", null, undefined, NaN` (plus Exoten wie `-0` und `0n`). Die Kurzform nutzt das aus, die ausführliche prüft explizit. Immer `===` statt `==`."
code:
  short: |-
    if (items.length) { render(items); }
    if (!name) { showError("Name fehlt"); }
  long: |-
    if (items.length > 0) {
      render(items);
    }
    if (name === "" || name === null || name === undefined) {
      showError("Name fehlt");
    }
explain:
  picture: "In jedem `if` fragt JavaScript insgeheim: Fühlt sich dieser Wert wie Ja oder wie Nein an? Nur eine Handvoll Werte fühlt sich wie Nein an, alles andere zählt als Ja."
  steps:
    - "`items.length` ist eine Zahl. `0` ist falsy, jede andere Zahl truthy. `if (items.length)` bedeutet also dasselbe wie `items.length > 0`."
    - "`!name` dreht den Wahrheitswert um: wahr, wenn `name` falsy ist, also leer, `null` oder `undefined`."
    - "`==` wandelt vor dem Vergleich Typen um (`0 == \"\"` ist `true`). `===` vergleicht Wert und Typ ohne Überraschungen."
  mistake: "Leere Arrays und Objekte sind truthy, `if ([])` ist immer wahr. Bei Arrays deshalb `.length` prüfen. Umgekehrt schlägt `if (!count)` auch bei `count = 0` an, obwohl 0 ein gültiger Wert sein kann."
  when: "Kurzform für die Frage, ob überhaupt etwas da ist. Ausführlich, wenn `0` oder `\"\"` gültige Werte sind und nicht als fehlend gelten dürfen."
  question: "Ist `if ({})` wahr oder falsch? Und `if (\"0\")`?"
  answer: "Beide sind wahr. Ein leeres Objekt ist trotzdem ein Objekt, und `\"0\"` ist ein nicht-leerer String."
links:
  - text: "Truthy"
    url: "https://developer.mozilla.org/de/docs/Glossary/Truthy"
  - text: "Falsy"
    url: "https://developer.mozilla.org/de/docs/Glossary/Falsy"
  - text: "Strikte Gleichheit ==="
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Strict_equality"
  - text: "Gleichheitsvergleiche"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness"
---
