---
title: "Pseudo-Elemente: `::before` und `::after`"
description: "Dekorative Elemente per CSS erzeugen, ohne zusätzliches HTML."
code:
  short: |-
    <!-- HTML -->
    <label class="required">E-Mail</label>

    /* CSS */
    .required::after {
      content: " *";
      color: crimson;
    }
  long: |-
    <!-- HTML -->
    <label>E-Mail <span class="star">*</span></label>

    /* CSS */
    .star {
      color: crimson;
    }
lang:
  short: "html"
  long: "html"
preview:
  height: 120
  html: |-
    <label class="required" for="mail">E-Mail</label>
    <input id="mail" type="email" placeholder="du@beispiel.de">
    <p class="hint">Das Sternchen steht nicht im HTML, ::after fügt es an.</p>
  css: |-
    .required::after {
      content: " *";
      color: crimson;
    }

    label { display: block; font-weight: 600; margin-bottom: 4px; }
    input { font: inherit; padding: 6px 8px; border: 1px solid var(--line); border-radius: 6px; width: 100%; max-width: 280px; background: var(--surface); color: var(--fg); }
explain:
  picture: "Pseudo-Elemente sind unsichtbare Haken am Anfang und am Ende eines Elements. Mit `content` hängst du etwas daran auf."
  steps:
    - "`::before` erzeugt ein Kind ganz am Anfang des Inhalts, `::after` ganz am Ende."
    - "Ohne `content` wird gar nichts angezeigt. Für reine Deko-Formen reicht `content: \"\"`."
    - "Pseudo-Elemente sind standardmäßig `inline`. Für Breite und Höhe brauchen sie `display: block` oder `position: absolute`."
    - "Die ausführliche Variante braucht dafür in jedem Label ein zusätzliches `<span>`."
  mistake: "Wichtige Inhalte per `content` einfügen. Screenreader lesen sie nicht zuverlässig vor, und man kann sie nicht markieren. Außerdem funktionieren Pseudo-Elemente nicht auf `<img>` und `<input>`."
  when: "Pseudo-Elemente für Deko: Pfeile, Icons, Trennlinien, Pflichtfeld-Sternchen. Echtes HTML für alles, was Bedeutung trägt."
  question: "Warum erscheint bei `.box::before { width: 20px; height: 20px; background: red; }` nichts?"
  answer: "Es fehlt `content`. Ohne `content: \"\"` entsteht das Pseudo-Element gar nicht. Außerdem braucht es `display: block` oder `inline-block`, damit Breite und Höhe greifen."
links:
  - text: "::before"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/::before"
  - text: "::after"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/::after"
  - text: "content"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/content"
---
