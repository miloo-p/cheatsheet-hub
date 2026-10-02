---
title: "`Promise.all`: parallel laden"
description: "Mehrere Requests gleichzeitig starten und auf alle warten. Scheitert einer, scheitert alles."
code:
  short: |-
    const [users, posts] = await Promise.all([
      fetch("/api/users").then(r => r.json()),
      fetch("/api/posts").then(r => r.json()),
    ]);
  long: |-
    const usersPromise = fetch("/api/users").then(function (r) {
      return r.json();
    });
    const postsPromise = fetch("/api/posts").then(function (r) {
      return r.json();
    });

    const results = await Promise.all([usersPromise, postsPromise]);
    const users = results[0];
    const posts = results[1];
explain:
  picture: "Statt erst zum Bäcker und dann zum Metzger zu gehen, schickst du zwei Leute gleichzeitig los und wartest, bis beide zurück sind."
  steps:
    - "Beide `fetch`-Aufrufe starten sofort, noch bevor `await` wartet."
    - "`Promise.all` bekommt ein Array von Promises und gibt ein einziges Promise zurück."
    - "Es ist erfüllt, wenn alle fertig sind. Die Ergebnisse stehen in derselben Reihenfolge wie die Eingabe, egal wer zuerst fertig war."
    - "Schlägt eines fehl, schlägt sofort das ganze `Promise.all` fehl."
  mistake: "Versehentlich nacheinander laden: `const a = await fetch(...); const b = await fetch(...);` dauert doppelt so lange, obwohl die Requests unabhängig sind. Ist ein Teilergebnis optional, ist `Promise.allSettled` die bessere Wahl."
  when: "Die Kurzform mit Array-Destructuring ist Standard. Die ausführliche Form zeigt, dass das Ergebnis einfach ein Array ist."
  question: "Request A dauert 2 Sekunden, B dauert 3. Wie lange dauert es mit zwei `await` nacheinander, und wie lange mit `Promise.all`?"
  answer: "Nacheinander 5 Sekunden. Mit `Promise.all` etwa 3 Sekunden, also so lange wie der langsamste Request."
links:
  - text: "Promise.all()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Promise/all"
  - text: "Promise.allSettled()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled"
---
