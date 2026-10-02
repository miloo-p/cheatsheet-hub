---
title: "Optionen gruppieren: `<fieldset>`"
description: "Zusammengehörige Felder, vor allem Radio-Buttons, mit einer gemeinsamen Überschrift versehen."
code:
  short: |-
    <fieldset>
      <legend>Versandart</legend>
      <label><input type="radio" name="shipping" value="standard" checked> Standard</label>
      <label><input type="radio" name="shipping" value="express"> Express</label>
    </fieldset>
  long: |-
    <div role="radiogroup" aria-labelledby="shipping-label">
      <p id="shipping-label">Versandart</p>
      <label><input type="radio" name="shipping" value="standard" checked> Standard</label>
      <label><input type="radio" name="shipping" value="express"> Express</label>
    </div>
explain:
  picture: "`<fieldset>` ist der Rahmen um eine Frage auf einem Fragebogen, `<legend>` die Frage selbst. Ohne sie stehen nur lose Antworten da: „Standard“, „Express“, aber wofür?"
  steps:
    - "`<fieldset>` gruppiert Felder, `<legend>` beschriftet die Gruppe."
    - "Screenreader lesen die Legende vor, sobald man in die Gruppe springt: „Versandart, Standard, Optionsfeld“."
    - "Radio-Buttons mit demselben `name` gehören zusammen. Nur einer kann ausgewählt sein, und mit den Pfeiltasten wechselt man zwischen ihnen."
    - "Beim Absenden geht der `value` des ausgewählten Buttons unter dem `name` ans Backend: `shipping=express`."
  mistake: "Radio-Buttons unterschiedliche `name`-Attribute geben. Dann lassen sich mehrere gleichzeitig auswählen. Oder den `value` vergessen: Dann kommt beim Server nur `on` an."
  when: "`<fieldset>` immer bei Radio-Gruppen und zusammengehörigen Checkboxen. Ein `disabled` auf dem Fieldset deaktiviert alle Felder darin auf einmal."
  question: "Was steht in `req.body.shipping`, wenn „Express“ gewählt und das Formular abgeschickt wurde?"
  answer: "`\"express\"`, also der `value` des gewählten Radio-Buttons."
links:
  - text: "<fieldset>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/fieldset"
  - text: "<legend>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/legend"
  - text: "type=\"radio\""
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/input/radio"
---
