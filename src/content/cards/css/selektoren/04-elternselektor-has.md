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
preview:
  height: 200
  html: |-
    <div class="grid">
      <div class="card"><img alt="" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='120'%3E%3Cdefs%3E%3ClinearGradient id='g'%3E%3Cstop offset='0' stop-color='%23177258'/%3E%3Cstop offset='1' stop-color='%236fd3ad'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='300' height='120' fill='url(%23g)'/%3E%3C/svg%3E"><h3>Mit Bild</h3><p>Kein Abstand oben.</p></div>
      <div class="card"><h3>Ohne Bild</h3><p>Normales Padding oben.</p></div>
    </div>
  css: |-
    .card:has(img) {
      padding-top: 0;
    }

    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; align-items: start; }
    .card { padding: 16px; background: var(--surface); border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
    .card img { display: block; width: calc(100% + 32px); margin: 0 -16px 10px; height: 70px; object-fit: cover; }
    h3 { margin: 0 0 4px; font-size: 15px; }
    p { margin: 0; color: var(--muted); font-size: 13px; }
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
