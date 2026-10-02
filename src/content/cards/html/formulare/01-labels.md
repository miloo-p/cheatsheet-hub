---
title: "Labels"
description: "Jedes Eingabefeld braucht eine Beschriftung, die technisch mit ihm verbunden ist."
code:
  short: |-
    <label>
      E-Mail
      <input type="email" name="email">
    </label>
  long: |-
    <label for="email">E-Mail</label>
    <input type="email" id="email" name="email">
explain:
  picture: "Ein Label ist das Namensschild am Eingabefeld. Ohne Verbindung hängt das Schild irgendwo daneben, und niemand weiß sicher, zu welchem Feld es gehört."
  steps:
    - "In der kurzen Variante umschließt das `<label>` das Feld. Die Verbindung entsteht automatisch."
    - "In der ausführlichen Variante verbindet `for` das Label mit der `id` des Feldes. So können beide getrennt im Layout stehen."
    - "Ein Klick auf das Label setzt den Fokus ins Feld. Bei Checkboxen wird die Klickfläche dadurch viel größer."
    - "Screenreader lesen das Label vor, sobald das Feld fokussiert ist."
  mistake: "`placeholder` statt Label benutzen. Der Platzhalter verschwindet beim Tippen, hat oft zu wenig Kontrast und wird nicht von allen Screenreadern als Beschriftung gelesen. Und in React heißt `for` übrigens `htmlFor`."
  when: "Beide Varianten sind gleichwertig. Die Variante mit `for` und `id` ist flexibler im Layout und in Formular-Bibliotheken üblich, das Umschließen spart IDs."
  question: "Was passiert, wenn zwei Felder auf derselben Seite `id=\"email\"` haben?"
  answer: "IDs müssen eindeutig sein. Das zweite Label zeigt dann auf das erste Feld. In wiederverwendbaren React-Komponenten erzeugst du eindeutige IDs mit `useId()`."
links:
  - text: "<label>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/label"
  - text: "<input>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/input"
---
