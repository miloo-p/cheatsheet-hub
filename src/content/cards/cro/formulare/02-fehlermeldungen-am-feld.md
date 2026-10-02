---
title: "Fehlermeldungen am Feld"
description: "Fehler sofort und am richtigen Ort zeigen, mit einer Anleitung zur Lösung."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <form onsubmit="if (!valid()) { alert('Fehler im Formular!'); return false; }">
      <input name="email">
      <input name="zip">
      <button>Weiter</button>
    </form>
  long: |-
    <label for="zip">Postleitzahl</label>
    <input id="zip" name="zip" inputmode="numeric" pattern="[0-9]{5}" required
           aria-describedby="zip-error">
    <p id="zip-error" class="error" hidden>
      Bitte eine 5-stellige Postleitzahl eingeben, z.B. 10115.
    </p>

    <script>
      zip.addEventListener("blur", () => {
        const ok = zip.checkValidity();
        document.getElementById("zip-error").hidden = ok;
        zip.setAttribute("aria-invalid", String(!ok));
      });
    </script>
explain:
  picture: "Eine gute Fehlermeldung ist wie ein Navi, das sagt: „Hier links abbiegen.“ Eine schlechte ist ein Warnton ohne Erklärung, und man weiß nicht einmal, welche Abzweigung falsch war."
  steps:
    - "Fehler direkt am betroffenen Feld zeigen, nicht oben im Formular oder als `alert`."
    - "Der Text sagt, was erwartet wird und gibt ein Beispiel, statt nur „ungültig“ zu melden."
    - "Geprüft wird beim Verlassen des Feldes (`blur`), nicht bei jedem Tastendruck. Sonst erscheint der Fehler schon, während man noch tippt."
    - "`aria-describedby` verknüpft die Meldung mit dem Feld, sodass Screenreader sie vorlesen. `aria-invalid` markiert das Feld als fehlerhaft."
    - "Bereits eingegebene Daten bleiben nach einem Fehler erhalten. Ein leeres Formular nach dem Absenden ist einer der häufigsten Abbruchgründe."
  mistake: "Fehler nur über Farbe anzeigen, z.B. einen roten Rahmen. Wer Farben schlecht unterscheiden kann oder einen Screenreader nutzt, sieht den Fehler nicht. Es braucht immer auch Text."
  when: "Anzahl der Fehler pro Feld als Event (`form_error` mit Feldname). Felder mit vielen Fehlern sind Kandidaten für bessere Hinweise, ein anderes Eingabeformat oder ganz zum Streichen."
  question: "Wann sollte die Fehlermeldung wieder verschwinden?"
  answer: "Sobald die Eingabe korrekt ist, also beim nächsten `input`- oder `blur`-Event mit gültigem Wert. Nicht erst beim erneuten Absenden."
links:
  - text: "Formularvalidierung (MDN)"
    url: "https://developer.mozilla.org/de/docs/Learn_web_development/Extensions/Forms/Form_validation"
  - text: "HTML-Spickzettel: Formulare"
    url: "/html/#formulare"
---
