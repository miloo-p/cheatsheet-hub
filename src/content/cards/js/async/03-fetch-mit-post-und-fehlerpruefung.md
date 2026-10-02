---
title: "`fetch` mit POST und Fehlerprüfung"
description: "`fetch` wirft bei 404 oder 500 keinen Fehler. `res.ok` musst du selbst prüfen."
code:
  short: |-
    const res = await fetch("/api/todos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title }),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const todo = await res.json();
  long: |-
    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: title }),
    };
    const response = await fetch("/api/todos", options);

    if (response.ok === false) {
      throw new Error("HTTP " + response.status);
    }

    const todo = await response.json();
explain:
  picture: "Ein POST-Request ist ein Brief: `method` ist die Versandart, `headers` steht auf dem Umschlag (z.B. „Inhalt ist JSON“), und `body` ist der Brief selbst, der als Text verschickt wird."
  steps:
    - "`JSON.stringify` wandelt das Objekt in einen JSON-String um, weil HTTP nur Text überträgt."
    - "Der `Content-Type`-Header sagt deinem Backend, z.B. `express.json()`, wie es den Body lesen soll."
    - "`fetch` gilt als erfolgreich, sobald überhaupt eine Antwort kommt, egal mit welchem Status."
    - "Darum `res.ok` prüfen. Es ist nur bei Status 200 bis 299 `true`."
    - "Erst danach den Body mit `res.json()` lesen."
  mistake: "Das Objekt ohne `JSON.stringify` als `body` übergeben, dann kommt beim Server `[object Object]` an. Oder den Header vergessen, dann ist `req.body` im Backend leer. Diesen Fehler kannst du jetzt von beiden Seiten aus debuggen."
  when: "Ein separates `options`-Objekt hilft, wenn du Optionen wiederverwenden oder loggen willst. In echten Projekten lohnt sich eine kleine Helferfunktion wie `api(url, data)`."
  question: "Dein Backend antwortet mit Status 404. Landet `fetch` im `catch`?"
  answer: "Nein. `fetch` wirft nur bei Netzwerkfehlern, z.B. wenn der Server nicht erreichbar ist oder CORS blockt. Ein 404 ist eine gültige Antwort, deshalb die Prüfung von `res.ok`."
links:
  - text: "Verwenden der Fetch API"
    url: "https://developer.mozilla.org/de/docs/Web/API/Fetch_API/Using_Fetch"
  - text: "Response.ok"
    url: "https://developer.mozilla.org/de/docs/Web/API/Response/ok"
  - text: "JSON.stringify()"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify"
---
