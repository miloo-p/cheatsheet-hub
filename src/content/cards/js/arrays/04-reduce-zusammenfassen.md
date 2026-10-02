---
title: "`reduce`: zusammenfassen"
description: "Macht aus einem Array einen einzelnen Wert. `acc` ist das Zwischenergebnis, der zweite Parameter der Startwert."
code:
  short: |-
    const total = cart.reduce((sum, item) => sum + item.price * item.qty, 0);

    const byCat = products.reduce((acc, p) => {
      (acc[p.category] ??= []).push(p);
      return acc;
    }, {});
  long: |-
    let total = 0;
    for (const item of cart) {
      total = total + item.price * item.qty;
    }

    const byCat = {};
    for (const product of products) {
      const key = product.category;
      if (byCat[key] === undefined) {
        byCat[key] = [];
      }
      byCat[key].push(product);
    }
explain:
  picture: "`reduce` ist ein Schneeball, der einen Hang hinunterrollt. Er startet klein mit dem Startwert und nimmt bei jedem Element etwas auf, bis am Ende ein einziger Ball übrig ist."
  steps:
    - "Der Startwert (hier `0` oder `{}`) wird zum ersten `acc`, dem Akkumulator."
    - "Für jedes Element wird deine Funktion mit `(acc, element)` aufgerufen."
    - "Was du zurückgibst, ist das `acc` für das nächste Element."
    - "Nach dem letzten Element ist `acc` das Ergebnis."
    - "`??=` in der Kurzform heißt: Nur zuweisen, wenn links `null` oder `undefined` steht. So wird pro Kategorie genau einmal ein leeres Array angelegt."
  mistake: "Den Startwert vergessen. Dann wird das erste Element zum Startwert, was bei Objekten (z.B. Warenkorb-Items) falsche Ergebnisse liefert. Oder `return acc` vergessen, dann ist `acc` im nächsten Schritt `undefined`."
  when: "Für Summen ist `reduce` kurz und klar. Für Gruppierungen ist die Schleife oft lesbarer, und das ist völlig in Ordnung. `reduce` ist kein Pflichtprogramm."
  question: "Was ergibt `[1, 2, 3].reduce((acc, n) => acc + n, 10)`?"
  answer: "16. Start bei 10, dann 11, 13, 16."
links:
  - text: "reduce()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce"
  - text: "Nullish-Zuweisung ??="
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment"
---
