---
title: "Spread: Objekte kopieren"
description: "Kopie erstellen und gezielt Felder überschreiben oder entfernen. Nur eine flache Kopie."
code:
  short: |-
    const updated = { ...user, age: 30 };

    const { password, ...safeUser } = user;
  long: |-
    const updated = Object.assign({}, user);
    updated.age = 30;

    const safeUser = Object.assign({}, user);
    delete safeUser.password;
explain:
  picture: "Spread schüttet den Inhalt eines Objekts in ein neues Objekt. Was danach kommt, überschreibt gleichnamige Felder, wie eine neue Schicht Farbe."
  steps:
    - "`{ ...user }` legt ein neues Objekt an und kopiert alle Felder von `user` hinein."
    - "`age: 30` dahinter überschreibt das kopierte `age`. Die Reihenfolge entscheidet."
    - "`{ password, ...safeUser } = user` zieht `password` heraus und packt den Rest in `safeUser`."
    - "`Object.assign({}, user)` macht dasselbe wie Spread, ist nur älter und länger."
  mistake: "Spread kopiert nur flach. Verschachtelte Objekte wie `user.address` werden nicht kopiert, sondern geteilt. Änderst du `copy.address.city`, änderst du auch das Original."
  when: "Spread ist der Standard. `delete` wie in der ausführlichen Form nur an einer Kopie benutzen, nie am Original oder am State."
  question: "Was ist `x.age` bei `const x = { age: 30, ...user }`, wenn `user.age` 25 ist?"
  answer: "25. Der Spread steht hinter `age: 30` und überschreibt den Wert."
links:
  - text: "Spread-Syntax"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Spread_syntax"
  - text: "Object.assign()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Object/assign"
  - text: "Objekte im State aktualisieren (EN)"
    url: "https://react.dev/learn/updating-objects-in-state"
---
