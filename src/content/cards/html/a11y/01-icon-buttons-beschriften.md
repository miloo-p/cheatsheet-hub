---
title: "Icon-Buttons beschriften"
description: "Buttons, die nur ein Icon zeigen, brauchen trotzdem einen Namen für Screenreader."
code:
  short: |-
    <button type="button" aria-label="Schließen">
      <svg aria-hidden="true">...</svg>
    </button>
  long: |-
    <button type="button">
      <svg aria-hidden="true">...</svg>
      <span class="visually-hidden">Schließen</span>
    </button>

    <style>
      .visually-hidden {
        position: absolute;
        width: 1px;
        height: 1px;
        overflow: hidden;
        clip-path: inset(50%);
        white-space: nowrap;
      }
    </style>
explain:
  picture: "Ein Icon-Button ohne Beschriftung ist eine Tür mit Bild statt Schild. Wer das Bild nicht sieht, hört nur „Schaltfläche“ und weiß nicht, was dahinter liegt."
  steps:
    - "Ohne Text liest der Screenreader nur „Schaltfläche“ vor."
    - "`aria-label` gibt dem Button einen unsichtbaren Namen."
    - "`aria-hidden=\"true\"` am Icon verhindert, dass das SVG zusätzlich vorgelesen wird."
    - "Die ausführliche Variante versteckt echten Text nur optisch, nicht für Screenreader. Vorteil: Übersetzungstools erfassen ihn zuverlässig."
  mistake: "`display: none` oder `hidden` zum Verstecken des Textes benutzen. Dann ist er auch für Screenreader weg. Genau dafür gibt es die Klasse `visually-hidden`."
  when: "`aria-label` für einzelne Icon-Buttons. Die Klasse `visually-hidden`, wenn die Seite übersetzt wird oder du sie ohnehin hast. In Tailwind heißt sie `sr-only`."
  question: "Was hört ein Screenreader-Nutzer bei `<button><svg>...</svg></button>` ohne Beschriftung?"
  answer: "Nur „Schaltfläche“, im schlimmsten Fall noch einen Dateinamen. Die Funktion bleibt unklar."
links:
  - text: "aria-label"
    url: "https://developer.mozilla.org/de/docs/Web/Accessibility/ARIA/Attributes/aria-label"
  - text: "aria-hidden"
    url: "https://developer.mozilla.org/de/docs/Web/Accessibility/ARIA/Attributes/aria-hidden"
---
