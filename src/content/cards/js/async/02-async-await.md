---
title: "`async` / `await`"
description: "Hier ist `await` die kurze Form: Es macht dasselbe wie die `.then`-Kette, liest sich aber wie normaler Code."
code:
  short: |-
    const loadUser = async id => {
      try {
        const res = await fetch(`/api/users/${id}`);
        return await res.json();
      } catch (err) {
        console.error(err);
        return null;
      }
    };
  long: |-
    function loadUser(id) {
      return fetch("/api/users/" + id)
        .then(function (response) {
          return response.json();
        })
        .catch(function (error) {
          console.error(error);
          return null;
        });
    }
explain:
  picture: "`await` heißt: Ich warte hier, bis der Abholschein eingelöst ist. Das gilt aber nur innerhalb dieser einen Funktion, der Rest der App läuft weiter."
  steps:
    - "`async` vor einer Funktion bedeutet: Sie gibt immer ein Promise zurück."
    - "`await` pausiert nur diese Funktion, bis das Promise erfüllt ist, und liefert dann den Wert."
    - "Wird das Promise abgelehnt, wirft `await` einen Fehler, den `try/catch` auffängt."
    - "Wer `loadUser` aufruft, braucht selbst wieder `await` oder `.then`, um an den Wert zu kommen."
  mistake: "`await` vergessen: `const data = res.json()` ist dann ein Promise und keine Daten. Oder `await` außerhalb einer `async`-Funktion benutzen. Das geht nur auf oberster Ebene in ES-Modulen."
  when: "`async/await` ist heute Standard, weil es sich wie normaler Code von oben nach unten liest. Die `.then`-Version musst du trotzdem lesen können."
  question: "Was bekommst du zurück, wenn du `loadUser(1)` ohne `await` aufrufst?"
  answer: "Ein Promise. Eine `async`-Funktion gibt immer ein Promise zurück, auch wenn darin `return null` steht."
links:
  - text: "async function"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/async_function"
  - text: "await"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/await"
  - text: "try...catch"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/try...catch"
---
