---
title: "Arrow Functions"
description: "Ohne `{}` wird der Ausdruck automatisch zurückgegeben (implizites return). Ein Objekt muss dann in `()`. Arrow Functions haben kein eigenes `this`."
code:
  short: |-
    const add = (a, b) => a + b;
    const square = n => n * n;
    const makeUser = name => ({ name });
  long: |-
    function add(a, b) {
      return a + b;
    }
    function square(n) {
      return n * n;
    }
    function makeUser(name) {
      return { name: name };
    }
explain:
  picture: "Eine Arrow Function ist eine Funktion in Kurzschrift: links vom Pfeil die Eingabe, rechts das Ergebnis. Lies `(a, b) => a + b` als: a und b werden zu a + b."
  steps:
    - "Ohne geschweifte Klammern nach dem Pfeil wird der Ausdruck automatisch zurückgegeben (implizites return)."
    - "Mit geschweiften Klammern ist es ein normaler Funktionskörper. Dann musst du `return` wieder selbst schreiben."
    - "Bei genau einem Parameter dürfen die runden Klammern weg: `n => n * n`."
    - "Soll direkt ein Objekt zurückkommen, braucht es runde Klammern drumherum. Sonst hält JavaScript `{}` für den Funktionskörper."
  mistake: "`x => { x * 2 }` gibt `undefined` zurück, weil mit den geschweiften Klammern das implizite return wegfällt. Außerdem: Als Methode in einem Objekt zeigt `this` in einer Arrow Function nicht auf das Objekt."
  when: "Arrow Functions für kurze Callbacks und React-Komponenten. `function` für Methoden, die `this` brauchen, und für Funktionen, die schon vor ihrer Definition aufgerufen werden (Hoisting)."
  question: "Was gibt `const f = () => { name: \"Lea\" }; f()` zurück?"
  answer: "`undefined`. Die geschweiften Klammern sind ein Funktionskörper ohne `return`. Richtig wäre `() => ({ name: \"Lea\" })`."
links:
  - text: "Pfeilfunktionen"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Functions/Arrow_functions"
  - text: "Funktionen (Leitfaden)"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Guide/Functions"
---
