---
title: "Promises mit `.then`"
description: "Ein Platzhalter für einen Wert, der später kommt. Jedes `.then` bekommt das Ergebnis des vorherigen."
code:
  short: |-
    fetch("/api/users")
      .then(res => res.json())
      .then(setUsers)
      .catch(console.error);
  long: |-
    fetch("/api/users")
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        setUsers(data);
      })
      .catch(function (error) {
        console.error(error);
      });
explain:
  picture: "Ein Promise ist ein Abholschein: `fetch` gibt dir sofort den Schein, die Ware kommt später. `.then` heißt: Wenn die Ware da ist, mach Folgendes damit."
  steps:
    - "`fetch` startet den Request und gibt sofort ein Promise zurück. Der restliche Code läuft weiter, ohne zu warten."
    - "Kommt die Antwort, ruft JavaScript die Funktion im ersten `.then` mit dem Response-Objekt auf."
    - "`response.json()` liest den Body und gibt wieder ein Promise zurück. Das nächste `.then` wartet darauf."
    - "Tritt irgendwo ein Fehler auf, springt die Kette direkt zum `.catch`."
  mistake: "Das `return` in einem `.then` vergessen. Dann bekommt das nächste `.then` `undefined` statt der Daten. Und: Code unterhalb der Kette läuft vor den Callbacks, nicht danach."
  when: "`.then(setUsers)` funktioniert in der Kurzform, weil `setUsers` selbst eine Funktion ist, die die Daten als Argument nimmt. Man übergibt sie direkt, statt sie in eine weitere Funktion zu verpacken."
  question: "In welcher Reihenfolge erscheinen die Logs: `console.log(\"A\"); fetch(url).then(() => console.log(\"B\")); console.log(\"C\");`?"
  answer: "A, C, B. Der Callback in `.then` läuft erst, wenn die Antwort da ist, und das ist immer nach dem restlichen synchronen Code."
links:
  - text: "Promises verwenden"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Guide/Using_promises"
  - text: "Promise"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Promise"
---
