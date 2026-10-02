---
title: "Event Delegation"
description: "Ein Listener auf dem Eltern-Element statt einer pro Button. Welcher geklickt wurde, verrät `event.target`."
code:
  short: |-
    list.addEventListener("click", e => {
      const btn = e.target.closest("button[data-id]");
      if (btn) deleteTodo(btn.dataset.id);
    });
  long: |-
    function handleListClick(event) {
      const button = event.target.closest("button[data-id]");
      if (button === null) {
        return;
      }
      const id = button.getAttribute("data-id");
      deleteTodo(id);
    }

    list.addEventListener("click", handleListClick);
explain:
  picture: "Statt jedem Tisch im Restaurant einen eigenen Kellner zu geben, steht ein Kellner im Raum und schaut, von welchem Tisch gerufen wurde."
  steps:
    - "Ein Klick auf einen Button steigt durch alle Eltern-Elemente nach oben bis zum Dokument (Event Bubbling)."
    - "Darum bekommt der Listener auf der Liste auch Klicks auf ihre Kinder mit."
    - "`event.target` ist das Element, das tatsächlich geklickt wurde, eventuell nur ein Icon im Button."
    - "`closest(\"button[data-id]\")` sucht von dort aus nach oben den passenden Button oder gibt `null` zurück."
    - "`dataset.id` liest das Attribut `data-id` aus."
  mistake: "`event.target` direkt benutzen, ohne `closest`. Klickt jemand auf ein `<span>` im Button, ist das Ziel der Span und `dataset.id` ist `undefined`."
  when: "Delegation lohnt sich bei Listen, die sich ändern: Neue Elemente funktionieren automatisch, ohne neue Listener. In React übernimmt das Framework das intern für dich."
  question: "Warum funktioniert Delegation auch für Listenelemente, die erst später hinzukommen?"
  answer: "Weil der Listener am Eltern-Element hängt, das schon existiert. Neue Kinder schicken ihre Klicks per Bubbling automatisch dorthin."
links:
  - text: "Event Bubbling"
    url: "https://developer.mozilla.org/de/docs/Learn_web_development/Core/Scripting/Event_bubbling"
  - text: "Element.closest()"
    url: "https://developer.mozilla.org/de/docs/Web/API/Element/closest"
  - text: "dataset"
    url: "https://developer.mozilla.org/de/docs/Web/API/HTMLElement/dataset"
---
