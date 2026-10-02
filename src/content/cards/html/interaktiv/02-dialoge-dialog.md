---
title: "Dialoge: `<dialog>`"
description: "Modale Dialoge mit eingebauter Tastatur- und Fokussteuerung."
code:
  short: |-
    <button onclick="document.getElementById('confirm').showModal()">Löschen</button>

    <dialog id="confirm">
      <p>Wirklich löschen?</p>
      <form method="dialog">
        <button value="cancel">Abbrechen</button>
        <button value="ok">Löschen</button>
      </form>
    </dialog>
  long: |-
    <button id="open">Löschen</button>

    <div class="overlay" hidden>
      <div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-text">
        <p id="modal-text">Wirklich löschen?</p>
        <button class="cancel">Abbrechen</button>
        <button class="ok">Löschen</button>
      </div>
    </div>

    <script>
      // Öffnen, Schließen, Escape-Taste, Fokus in den Dialog setzen,
      // Fokus im Dialog halten, Hintergrund sperren, Fokus zurückgeben ...
      // schnell 40 Zeilen JavaScript
    </script>
explain:
  picture: "Ein modaler Dialog ist ein Behördenschalter, an dem du stehen bleibst, bis dein Anliegen erledigt ist. `<dialog>` baut den Schalter samt Absperrband auf. Beim Nachbau musst du jedes Band selbst spannen."
  steps:
    - "`showModal()` öffnet den Dialog in der obersten Ebene über allem anderen. Der Rest der Seite ist gesperrt."
    - "Der Fokus springt in den Dialog, Escape schließt ihn, und danach kehrt der Fokus zum auslösenden Button zurück."
    - "`<form method=\"dialog\">` schließt den Dialog beim Klick auf einen Button. Dessen `value` steht danach in `dialog.returnValue`."
    - "Der abgedunkelte Hintergrund lässt sich per CSS mit `::backdrop` gestalten."
  mistake: "Das Attribut `open` direkt setzen statt `showModal()` aufzurufen. Dann ist der Dialog zwar sichtbar, aber nicht modal: kein Hintergrund, keine Sperre, kein Escape."
  when: "`<dialog>` für Bestätigungen, Formulare im Overlay und Hinweise. Neuere Browser öffnen ihn sogar ganz ohne JavaScript über die Attribute `command` und `commandfor` am Button."
  question: "Wie findest du nach dem Schließen heraus, welcher Button geklickt wurde?"
  answer: "Über `dialog.returnValue`. Es enthält den `value` des Buttons aus dem `<form method=\"dialog\">`, hier also `\"ok\"` oder `\"cancel\"`."
links:
  - text: "<dialog>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/dialog"
  - text: "::backdrop"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/::backdrop"
---
