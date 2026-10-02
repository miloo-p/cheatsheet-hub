---
title: "Boolesche Attribute"
description: "Manche Attribute sind Schalter: Allein ihre Anwesenheit bedeutet „an“."
code:
  short: |-
    <input type="checkbox" checked>
    <input type="email" required>
    <button disabled>Speichern</button>
  long: |-
    <input type="checkbox" checked="checked">
    <input type="email" required="required">
    <button disabled="disabled">Speichern</button>
explain:
  picture: "Ein boolesches Attribut ist ein Lichtschalter, kein Dimmer. Es gibt nur an und aus, und an ist es, sobald es dasteht."
  steps:
    - "Attribute wie `checked`, `required`, `disabled`, `hidden` oder `open` brauchen keinen Wert."
    - "Steht das Attribut im Tag, gilt es als eingeschaltet."
    - "Die Schreibweise mit wiederholtem Namen stammt aus XHTML und ist weiterhin gültig."
    - "Zum Ausschalten muss das Attribut ganz verschwinden."
  mistake: "`disabled=\"false\"` schreiben und erwarten, dass der Button aktiv ist. Er ist trotzdem deaktiviert, weil das Attribut vorhanden ist. Per JavaScript schaltest du es mit `button.disabled = false` oder `removeAttribute(\"disabled\")` aus."
  when: "Immer die kurze Form. In JSX schreibst du dagegen `disabled={false}`, und React entfernt das Attribut dann selbst."
  question: "Ist `<input required=\"no\">` ein Pflichtfeld?"
  answer: "Ja. Der Wert ist egal, nur die Anwesenheit des Attributs zählt."
links:
  - text: "disabled"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Attributes/disabled"
  - text: "required"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Attributes/required"
---
