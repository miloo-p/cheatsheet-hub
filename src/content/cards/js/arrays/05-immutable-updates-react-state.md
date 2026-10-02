---
title: "Immutable Updates (React State)"
description: "State nie direkt ändern, sondern immer ein neues Array erzeugen. Sonst merkt React die Änderung nicht."
code:
  short: |-
    // hinzufügen
    setTodos([...todos, newTodo]);

    // ein Element ändern
    setTodos(todos.map(t =>
      t.id === id ? { ...t, done: !t.done } : t
    ));
  long: |-
    // hinzufügen
    const withNew = todos.slice(); // Kopie
    withNew.push(newTodo);
    setTodos(withNew);

    // ein Element ändern
    const updated = todos.map(function (todo) {
      if (todo.id === id) {
        const copy = Object.assign({}, todo);
        copy.done = !todo.done;
        return copy;
      }
      return todo;
    });
    setTodos(updated);
explain:
  picture: "React prüft State wie ein Postbote, der nur auf die Hausnummer schaut und nicht in die Wohnung. Stellst du nur die Möbel um (Mutation), merkt er nichts. Erst eine neue Adresse, also ein neues Array oder Objekt, löst ein Re-Render aus."
  steps:
    - "`[...todos, newTodo]` erzeugt ein neues Array mit allen alten Elementen plus dem neuen."
    - "`map` erzeugt ebenfalls ein neues Array. Nur das betroffene Element wird durch eine Kopie ersetzt, die anderen werden unverändert übernommen."
    - "`{ ...t, done: !t.done }` kopiert das Todo und überschreibt ein Feld."
    - "React vergleicht alte und neue Referenz, sieht den Unterschied und rendert neu."
  mistake: "`todos.push(newTodo); setTodos(todos);` Das Array ist dasselbe Objekt, also passiert im UI nichts. Genauso bei `todo.done = true` direkt am State. Vorsicht auch bei `sort()` und `reverse()`, die das Original verändern."
  when: "Spread ist in React der Standard. Die ausführliche Form zeigt, was dabei eigentlich passiert: erst kopieren, dann die Kopie ändern."
  question: "Warum funktioniert `const copy = todos; copy.push(x); setTodos(copy);` nicht?"
  answer: "`copy = todos` kopiert nicht das Array, sondern nur den Verweis. Beide Namen zeigen auf dasselbe Array, also sieht React keine neue Referenz."
links:
  - text: "Spread-Syntax"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Spread_syntax"
  - text: "Arrays im State aktualisieren (EN)"
    url: "https://react.dev/learn/updating-arrays-in-state"
---
