---
title: "`map`: transformieren"
description: "Neues Array mit gleicher Länge, jedes Element umgewandelt. In React: Daten zu JSX."
code:
  short: |-
    const names = users.map(u => u.name);

    // React
    users.map(u => <li key={u.id}>{u.name}</li>)
  long: |-
    const names = [];
    for (let i = 0; i < users.length; i++) {
      names.push(users[i].name);
    }

    // oder mit map, aber ausgeschrieben
    const names2 = users.map(function (user) {
      return user.name;
    });
lang:
  short: "jsx"
explain:
  picture: "`map` ist ein Fließband: Jedes Element läuft einmal durch dieselbe Maschine, deine Funktion. Am Ende liegt ein neues Band mit genauso vielen umgewandelten Teilen."
  steps:
    - "`map` legt intern ein neues, leeres Array an."
    - "Für jedes Element ruft es deine Funktion auf, mit dem Element und dessen Index."
    - "Was deine Funktion zurückgibt, landet an derselben Position im neuen Array."
    - "Das Original bleibt unverändert."
  mistake: "In `map` nichts zurückgeben, z.B. durch geschweifte Klammern ohne `return`. Dann ist das neue Array voller `undefined`. Außerdem `map` nur für Nebenwirkungen wie Loggen zu benutzen. Dafür gibt es `forEach`."
  when: "`map` immer, wenn aus N Elementen N neue werden. Die Schleife brauchst du nur, wenn du unterwegs abbrechen willst."
  question: "Wie viele Elemente hat das Ergebnis von `[1, 2, 3, 4].map(n => n > 2)`?"
  answer: "Vier: `[false, false, true, true]`. `map` sortiert nie aus, die Länge bleibt immer gleich. Zum Aussortieren nimmst du `filter`."
links:
  - text: "Array.prototype.map()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/map"
---
