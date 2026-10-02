---
title: "Validierung im Browser"
description: "HTML-Attribute prüfen Eingaben schon vor dem Absenden, ohne eine Zeile JavaScript."
code:
  short: |-
    <input type="text" name="username" required minlength="3" maxlength="20"
           pattern="[a-z0-9_]+" title="Nur Kleinbuchstaben, Ziffern und _">
  long: |-
    <input type="text" name="username" id="username">
    <span class="error" id="username-error"></span>

    <script>
      const input = document.getElementById("username");
      const error = document.getElementById("username-error");
      input.form.addEventListener("submit", e => {
        const v = input.value;
        let msg = "";
        if (!v) msg = "Bitte ausfüllen";
        else if (v.length < 3 || v.length > 20) msg = "3 bis 20 Zeichen";
        else if (!/^[a-z0-9_]+$/.test(v)) msg = "Nur a-z, 0-9 und _";
        if (msg) { e.preventDefault(); error.textContent = msg; }
      });
    </script>
explain:
  picture: "Die Browser-Validierung ist der Türsteher vor dem Club: Er weist offensichtlich falsche Gäste ab. Die Ausweiskontrolle an der Kasse, also das Backend, ersetzt er aber nicht."
  steps:
    - "`required` verlangt einen Wert, `minlength` und `maxlength` begrenzen die Länge."
    - "`pattern` prüft gegen einen regulären Ausdruck. Er muss den ganzen Wert treffen, `^` und `$` sind automatisch dabei."
    - "Ist etwas ungültig, verhindert der Browser das Absenden und zeigt eine Meldung am Feld."
    - "Im CSS markierst du ungültige Felder mit `:invalid` oder `:user-invalid`. `:user-invalid` greift erst, nachdem jemand mit dem Feld interagiert hat."
  mistake: "Sich auf die Browser-Validierung verlassen. Jeder kann sie in den Entwicklertools abschalten oder direkt einen Request an deine API schicken. Prüfen muss immer auch das Backend."
  when: "HTML-Attribute für alle einfachen Regeln. JavaScript zusätzlich für Regeln, die HTML nicht kann, z.B. dass zwei Passwortfelder übereinstimmen (mit `setCustomValidity`)."
  question: "Wie schaltest du die Browser-Meldungen für ein Formular ab, um eigene Fehlermeldungen zu zeigen?"
  answer: "Mit `novalidate` auf dem `<form>`. Die Attribute bleiben trotzdem nützlich, weil du sie per JavaScript mit `checkValidity()` und `validity` abfragen kannst."
links:
  - text: "Formularvalidierung"
    url: "https://developer.mozilla.org/de/docs/Learn_web_development/Extensions/Forms/Form_validation"
  - text: "required"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Attributes/required"
  - text: "pattern"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Attributes/pattern"
---
