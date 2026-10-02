---
title: "Sichtbarer Fokus: `:focus-visible`"
description: "Wer mit der Tastatur navigiert, braucht einen sichtbaren Fokus. `:focus-visible` zeigt ihn nur, wenn er wirklich gebraucht wird."
code:
  short: |-
    .button:focus-visible {
      outline: 2px solid var(--brand);
      outline-offset: 2px;
    }
  long: |-
    .button:focus {
      outline: 2px solid var(--brand);
      outline-offset: 2px;
    }
    .button:focus:not(:focus-visible) {
      outline: none;
    }
preview:
  height: 120
  html: |-
    <div class="row"><button class="button">Erster</button> <button class="button">Zweiter</button></div>
    <p class="hint">Klicken: kein Rahmen. In die Vorschau klicken und mit Tab wechseln: Rahmen.</p>
  css: |-
    .button:focus-visible {
      outline: 2px solid var(--brand);
      outline-offset: 2px;
    }

    .button { background: var(--surface); color: var(--fg); border: 1px solid var(--line); border-radius: 6px; padding: 8px 16px; }
    .row { display: flex; gap: 12px; }
explain:
  picture: "Der Fokusring ist der Mauszeiger für Menschen, die mit der Tastatur navigieren. Ohne ihn ist die Seite für sie wie eine Maus ohne Zeiger."
  steps:
    - "`:focus` greift immer, wenn ein Element fokussiert ist, auch nach einem Mausklick."
    - "Viele finden den Ring nach einem Klick störend und entfernen ihn komplett. Das schadet allen, die mit der Tastatur arbeiten."
    - "`:focus-visible` greift nur, wenn der Browser einen sichtbaren Fokus für sinnvoll hält, typischerweise bei Navigation mit Tab."
    - "Die ausführliche Variante baut dasselbe Verhalten mit `:focus` und `:not()` nach. So wurde es gemacht, bevor alle Browser `:focus-visible` konnten."
  mistake: "`outline: none` global setzen, ohne Ersatz. Dann sieht niemand mit Tastatur mehr, wo er sich auf der Seite befindet."
  when: "Heute einfach `:focus-visible`, alle aktuellen Browser unterstützen es. Die ausführliche Variante brauchst du nur, um älteren Code zu verstehen."
  question: "Wie prüfst du schnell, ob deine Seite einen sichtbaren Fokus hat?"
  answer: "Klick in die Adresszeile und drück mehrmals Tab. Bei jedem Schritt muss erkennbar sein, welches Element gerade aktiv ist."
links:
  - text: ":focus-visible"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/:focus-visible"
  - text: ":focus"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/:focus"
  - text: "outline"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/outline"
---
