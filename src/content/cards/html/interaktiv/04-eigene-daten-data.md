---
title: "Eigene Daten: `data-*`"
description: "Eigene Daten direkt am Element speichern, z.B. die Datenbank-ID für einen Löschen-Button."
code:
  short: |-
    <li data-id="42" data-status="done">Einkaufen</li>

    <script>
      const li = document.querySelector("li");
      li.dataset.id;      // "42"
      li.dataset.status;  // "done"
    </script>
  long: |-
    <li class="todo todo-42 status-done">
      Einkaufen
      <input type="hidden" class="todo-id" value="42">
    </li>

    <script>
      const li = document.querySelector("li");
      li.querySelector(".todo-id").value;     // "42"
      li.classList.contains("status-done");   // true
    </script>
explain:
  picture: "`data-`-Attribute sind Etiketten, die du an ein Element klebst. Wer die Seite benutzt, sieht sie nicht, aber JavaScript und CSS können sie lesen."
  steps:
    - "Jedes Attribut, das mit `data-` beginnt, ist erlaubt und frei benennbar."
    - "In JavaScript liest du es über `element.dataset`. Aus `data-user-id` wird dabei `dataset.userId` in camelCase."
    - "Werte sind immer Strings. `\"42\"` musst du für Berechnungen mit `Number()` umwandeln."
    - "Auch CSS kann darauf reagieren, z.B. `[data-status=\"done\"] { text-decoration: line-through; }`."
  mistake: "Vertrauliche Daten in `data-`-Attribute schreiben. Jeder kann sie im Quelltext lesen und in den Entwicklertools ändern. Eine ID aus `data-id` muss das Backend deshalb immer gegen die Rechte des Nutzers prüfen."
  when: "`data-`-Attribute für Werte, die JavaScript oder CSS zu einem Element brauchen. Versteckte Inputs nur in Formularen, deren Wert mitgeschickt werden soll."
  question: "Wie heißt `data-created-at` in `dataset`?"
  answer: "`dataset.createdAt`. Bindestriche werden zu camelCase."
links:
  - text: "data-*"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Global_attributes/data-*"
  - text: "dataset"
    url: "https://developer.mozilla.org/de/docs/Web/API/HTMLElement/dataset"
---
