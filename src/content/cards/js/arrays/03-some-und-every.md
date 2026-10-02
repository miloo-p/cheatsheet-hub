---
title: "`some` und `every`"
description: "Geben einen Boolean zurück: Trifft es auf mindestens eins zu, oder auf alle?"
code:
  short: |-
    const anyOpen = todos.some(t => !t.done);
    const allDone = todos.every(t => t.done);
  long: |-
    let anyOpen = false;
    for (const todo of todos) {
      if (todo.done === false) {
        anyOpen = true;
        break;
      }
    }

    let allDone = true;
    for (const todo of todos) {
      if (todo.done === false) {
        allDone = false;
        break;
      }
    }
explain:
  picture: "`some` fragt: Gibt es mindestens einen? `every` fragt: Sind es wirklich alle? Beide antworten nur mit Ja oder Nein."
  steps:
    - "`some` geht die Elemente durch und stoppt beim ersten `true`. Das Ergebnis ist dann `true`."
    - "`every` stoppt beim ersten `false`. Das Ergebnis ist dann `false`."
    - "Läuft die Schleife ohne Abbruch durch, ist `some` `false` und `every` `true`."
  mistake: "Leere Arrays: `[].every(...)` ist `true`, `[].some(...)` ist `false`. Das überrascht, ist aber logisch: Bei null Elementen gibt es keins, das die Bedingung verletzt."
  when: "Ideal für UI-Zustände wie `disabled={!items.some(i => i.selected)}`. Viel klarer als `filter(...).length > 0`."
  question: "Wie drückst du mit `some` aus, dass kein Todo erledigt ist?"
  answer: "`!todos.some(t => t.done)`. Gleichwertig ist `todos.every(t => !t.done)`."
links:
  - text: "some()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/some"
  - text: "every()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/every"
---
