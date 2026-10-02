---
title: "Elternselektor: `:has()`"
description: "Ein Element anhand seines Inhalts stylen. Früher ging das nur mit JavaScript."
code:
  short: |-
    .card:has(img) {
      padding-top: 0;
    }
  long: |-
    /* CSS */
    .card.has-image {
      padding-top: 0;
    }

    // JavaScript
    document.querySelectorAll(".card").forEach(card => {
      if (card.querySelector("img")) card.classList.add("has-image");
    });
explain:
  picture: "`:has()` ist der Elternselektor, auf den CSS jahrzehntelang gewartet hat: Er schaut ins Element hinein und fragt, ob etwas Bestimmtes darin steckt."
  steps:
    - "Selektoren gingen bisher nur von oben nach unten, vom Eltern- zum Kindelement."
    - "`.card:has(img)` dreht das um: Gestylt wird die Karte, aber nur, wenn sie ein Bild enthält."
    - "In der Klammer darf ein beliebiger Selektor stehen, auch mit Zuständen. `.field:has(input:invalid)` markiert ein ganzes Formularfeld, sobald die Eingabe ungültig ist."
    - "Die JavaScript-Variante muss nach jeder Änderung erneut laufen. `:has()` reagiert automatisch."
  mistake: "`:has()` mit einem Nachfahren-Selektor verwechseln. `.card img` stylt das Bild, `.card:has(img)` stylt die Karte."
  when: "Alle aktuellen Browser unterstützen `:has()`. JavaScript brauchst du dafür nur noch, wenn sehr alte Browser unterstützt werden müssen."
  question: "Wie stylst du ein `<form>`, sobald irgendeine Checkbox darin angehakt ist?"
  answer: "Mit `form:has(input[type=\"checkbox\"]:checked) { ... }`."
links:
  - text: ":has()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/:has"
  - text: "Pseudoklassen"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/Pseudo-classes"
---
