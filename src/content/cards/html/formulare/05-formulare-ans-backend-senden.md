---
title: "Formulare ans Backend senden"
description: "Ein Formular kann Daten ganz ohne JavaScript an den Server schicken. Mit `fetch` bleibt die Seite dabei stehen."
code:
  short: |-
    <form action="/api/todos" method="post">
      <input name="title" required>
      <button>Anlegen</button>
    </form>
  long: |-
    <form id="todo-form">
      <input name="title" required>
      <button>Anlegen</button>
    </form>

    <script>
      document.getElementById("todo-form").addEventListener("submit", async e => {
        e.preventDefault();
        const data = Object.fromEntries(new FormData(e.target));
        await fetch("/api/todos", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        });
      });
    </script>
explain:
  picture: "Ein natives Formular ist ein Brief per Post: Er wird abgeschickt, und als Antwort kommt eine ganz neue Seite. `fetch` ist eine Chatnachricht: Sie geht raus, und die Seite bleibt, wie sie ist."
  steps:
    - "`action` ist die Zieladresse, `method` die HTTP-Methode. Formulare können nur `get` und `post`."
    - "Beim Absenden sammelt der Browser alle Felder mit `name` und schickt sie URL-kodiert, z.B. `title=Einkaufen`. Felder ohne `name` werden ignoriert."
    - "Im Express-Backend brauchst du dafür `express.urlencoded()`, damit `req.body.title` gefüllt ist."
    - "Die `fetch`-Variante verhindert mit `preventDefault()` das Neuladen, liest die Felder mit `FormData` und schickt JSON. Dafür braucht das Backend `express.json()`."
  mistake: "Das `name`-Attribut am Input vergessen. Das Feld wird dann nicht mitgeschickt, und `req.body.title` ist `undefined`, obwohl im Browser alles ausgefüllt war."
  when: "Native Formulare für einfache Seiten und als robuste Grundlage. `fetch` in Single-Page-Apps wie React, wo die Seite nicht neu laden soll."
  question: "Welcher Express-Parser wird für das native Formular gebraucht und welcher für die `fetch`-Variante?"
  answer: "Für das native Formular `express.urlencoded()`, für JSON per `fetch` `express.json()`."
links:
  - text: "<form>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/form"
  - text: "FormData"
    url: "https://developer.mozilla.org/de/docs/Web/API/FormData"
  - text: "express.urlencoded (EN)"
    url: "https://expressjs.com/en/api.html#express.urlencoded"
---
