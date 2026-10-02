---
title: "Optional Chaining `?.` und `??`"
description: "`?.` bricht bei `null/undefined` ab statt zu crashen. `??` setzt einen Standardwert nur bei `null/undefined`, nicht bei `0`."
code:
  short: |-
    const city = user?.address?.city;
    const qty = input ?? 1;
    user.onSave?.();
  long: |-
    let city = undefined;
    if (user && user.address) {
      city = user.address.city;
    }

    let qty;
    if (input === null || input === undefined) {
      qty = 1;
    } else {
      qty = input;
    }

    if (typeof user.onSave === "function") {
      user.onSave();
    }
explain:
  picture: "`?.` ist ein vorsichtiger Schritt im Dunkeln: Bevor du weitergehst, prüfst du, ob da Boden ist. Fehlt er, bleibst du stehen und bekommst `undefined` statt eines Absturzes."
  steps:
    - "Ohne `?.` wirft `user.address.city` einen TypeError (Cannot read properties of undefined), wenn `address` fehlt."
    - "`user?.address?.city` prüft vor jedem Punkt, ob links davon `null` oder `undefined` steht. Wenn ja, ist der ganze Ausdruck sofort `undefined`."
    - "`a ?? b` liefert `a`, außer `a` ist `null` oder `undefined`. Dann kommt `b`."
    - "`fn?.()` ruft die Funktion nur auf, wenn es sie gibt. Praktisch für optionale Callback-Props."
  mistake: "`??` mit `||` verwechseln. `input || 1` ersetzt auch `0` und `\"\"` durch 1, weil `||` auf falsy prüft. Bei Mengen, Preisen und Indizes fast immer `??` nehmen."
  when: "`?.` bei Daten, die unvollständig sein können, z.B. aus APIs. Nicht überall verstreuen: Wenn ein Wert immer da sein muss, soll ein Fehler ruhig sichtbar werden."
  question: "Was ergibt `0 ?? 5`, und was ergibt `0 || 5`?"
  answer: "`0 ?? 5` ergibt 0, weil 0 weder null noch undefined ist. `0 || 5` ergibt 5, weil 0 falsy ist."
links:
  - text: "Optional Chaining ?."
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Optional_chaining"
  - text: "Nullish Coalescing ??"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing"
---
