---
title: "`filter` und `find`"
description: "`filter` gibt alle Treffer als Array, `find` den ersten Treffer oder `undefined`."
code:
  short: |-
    const open = todos.filter(t => !t.done);
    const todo = todos.find(t => t.id === id);
  long: |-
    const open = [];
    for (const todo of todos) {
      if (todo.done === false) {
        open.push(todo);
      }
    }

    let found = undefined;
    for (const todo of todos) {
      if (todo.id === id) {
        found = todo;
        break;
      }
    }
explain:
  picture: "`filter` ist ein Sieb: Alles, was die Prüfung besteht, fällt in das neue Array. `find` ist ein Suchtrupp, der beim ersten Treffer aufhört und genau dieses eine Element meldet."
  steps:
    - "Deine Funktion bekommt jedes Element und gibt `true` oder `false` zurück (oder truthy/falsy)."
    - "`filter` sammelt alle Elemente mit `true` in einem neuen Array. Das kann auch leer sein."
    - "`find` gibt das erste Element mit `true` zurück und hört sofort auf. Findet es nichts, kommt `undefined`."
  mistake: "Das Ergebnis von `find` ungeprüft benutzen: `todos.find(...).title` stürzt ab, wenn nichts gefunden wurde. Und `filter(...)[0]` statt `find` schreiben, was unnötig das ganze Array durchläuft."
  when: "Die Methoden sind fast immer besser lesbar. Die Schleife zeigt, warum `find` schneller sein kann: wegen des `break`."
  question: "Was gibt `filter` zurück, wenn nichts passt? Und was gibt `find` zurück?"
  answer: "`filter` gibt ein leeres Array `[]` zurück, `find` gibt `undefined` zurück."
links:
  - text: "filter()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/filter"
  - text: "find()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/find"
  - text: "findIndex()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex"
---
