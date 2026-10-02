---
title: "`const` vs `let`"
description: "Standard ist `const`. `let` brauchst du nur, wenn die Variable später einen neuen Wert bekommt, wie in der ausführlichen Variante."
code:
  short: "const label = count > 0 ? \"voll\" : \"leer\";"
  long: |-
    let label;
    if (count > 0) {
      label = "voll";
    } else {
      label = "leer";
    }
explain:
  picture: "Stell dir eine Variable wie ein Etikett vor, das an einem Wert klebt. `const` heißt: Das Etikett wird nie umgeklebt. `let` heißt: Es darf später an einen anderen Wert wandern."
  steps:
    - "Die Kurzform nutzt den ternären Operator `bedingung ? wennJa : wennNein`. Er ist ein Ausdruck und liefert also direkt einen Wert."
    - "Weil der Wert sofort feststeht, kann `label` eine `const` sein."
    - "In der ausführlichen Form ist `if/else` eine Anweisung, kein Ausdruck. Deshalb wird `label` erst leer angelegt und später befüllt. Dafür braucht es `let`."
  mistake: "`const` macht Arrays und Objekte nicht unveränderlich: `const list = []; list.push(1)` ist erlaubt, nur `list = [...]` nicht. Und `var` ignoriert Blöcke, deshalb nicht mehr verwenden."
  when: "Ternär für einfache Entweder-oder-Werte. Sobald es mehr als zwei Fälle oder mehrere Anweisungen pro Fall gibt, ist `if/else` lesbarer. Verschachtelte Ternäre vermeiden."
  question: "Warum funktioniert `const label; if (x) label = \"a\";` nicht?"
  answer: "`const` muss bei der Deklaration sofort einen Wert bekommen und kann danach nicht neu zugewiesen werden. Hier brauchst du `let` oder einen Ternär."
links:
  - text: "const"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/const"
  - text: "let"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/let"
  - text: "Bedingter Operator ? :"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Conditional_operator"
---
