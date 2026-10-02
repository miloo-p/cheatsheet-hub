---
title: "Aufklappen: `<details>`"
description: "Ein Akkordeon zum Auf- und Zuklappen, ganz ohne JavaScript. Die Erklärungen auf diesen Spickzetteln funktionieren genau so."
code:
  short: |-
    <details>
      <summary>Was kostet der Versand?</summary>
      <p>Ab 30 € ist der Versand kostenlos.</p>
    </details>
  long: |-
    <button class="faq-toggle" aria-expanded="false" aria-controls="faq-1">
      Was kostet der Versand?
    </button>
    <div id="faq-1" hidden>
      <p>Ab 30 € ist der Versand kostenlos.</p>
    </div>

    <script>
      document.querySelector(".faq-toggle").addEventListener("click", e => {
        const btn = e.currentTarget;
        const open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", String(!open));
        document.getElementById("faq-1").hidden = open;
      });
    </script>
explain:
  picture: "`<details>` ist eine Schublade mit Griff: `<summary>` ist der Griff, der Rest ist der Inhalt. Aufziehen, zuschieben, fertig."
  steps:
    - "`<summary>` ist immer sichtbar und lässt sich per Klick, Enter oder Leertaste bedienen."
    - "Der restliche Inhalt erscheint nur, wenn das Attribut `open` gesetzt ist. Der Browser schaltet es beim Klicken selbst um."
    - "Screenreader melden den Zustand „erweitert“ oder „reduziert“ automatisch."
    - "Haben mehrere `<details>` denselben `name`, ist immer nur eins offen, wie bei einem klassischen Akkordeon. Die ausführliche Variante baut all das mit `aria-expanded` und JavaScript nach."
  mistake: "Links oder Buttons in `<summary>` legen. Klicks darauf lösen dann auch das Auf- und Zuklappen aus, und Screenreader kommen durcheinander."
  when: "`<details>` für FAQs, Erklärungen und optionale Zusatzinfos. Einen eigenen Nachbau nur, wenn sich Optik oder Verhalten damit wirklich nicht umsetzen lassen."
  question: "Wie entfernst du das Dreieck vor der `<summary>`?"
  answer: "Mit `summary { list-style: none; }` und für Safari zusätzlich `summary::-webkit-details-marker { display: none; }`."
links:
  - text: "<details>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/details"
  - text: "<summary>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/summary"
---
