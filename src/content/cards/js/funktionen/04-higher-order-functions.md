---
title: "Higher-Order Functions"
description: "Funktionen, die eine Funktion zurückgeben oder annehmen. Doppelte Pfeile `f => n =>` bedeuten: Funktion gibt Funktion zurück."
code:
  short: |-
    const multiplier = factor => n => n * factor;
    const double = multiplier(2);
    double(5); // 10
  long: |-
    function multiplier(factor) {
      function multiply(n) {
        return n * factor;
      }
      return multiply;
    }
    const double = multiplier(2);
    double(5); // 10
explain:
  picture: "Eine Higher-Order Function ist eine Funktionsfabrik: Du gibst eine Einstellung hinein, z.B. Faktor 2, und bekommst eine fertig konfigurierte Funktion heraus."
  steps:
    - "`multiplier(2)` wird aufgerufen, `factor` ist 2."
    - "Zurück kommt keine Zahl, sondern eine neue Funktion, die `factor` per Closure kennt."
    - "`double(5)` ruft diese neue Funktion auf: 5 mal 2 ergibt 10."
    - "In der Kurzform steht jeder Pfeil für eine Funktion. `factor => n => ...` heißt: Nimm factor und gib eine Funktion zurück, die n nimmt."
  mistake: "`multiplier(2, 5)` aufrufen und 10 erwarten. Das zweite Argument wird ignoriert, und das Ergebnis ist eine Funktion. Richtig ist `multiplier(2)(5)`."
  when: "Doppelte Pfeile siehst du oft in Event-Handlern (`id => () => remove(id)`) und in Express-Middleware. Wenn es dich verwirrt, schreib es zuerst ausführlich hin."
  question: "Welche Higher-Order Functions benutzt du schon ständig, ohne sie so zu nennen?"
  answer: "`map`, `filter`, `find`, `reduce`, `some`, `every`, `forEach` und `sort` nehmen alle eine Funktion als Argument. Ebenso `addEventListener` und `setTimeout`."
links:
  - text: "Callback-Funktion"
    url: "https://developer.mozilla.org/de/docs/Glossary/Callback_function"
  - text: "First-Class Functions"
    url: "https://developer.mozilla.org/de/docs/Glossary/First-class_Function"
---
