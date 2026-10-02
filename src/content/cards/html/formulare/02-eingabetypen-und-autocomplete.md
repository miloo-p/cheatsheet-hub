---
title: "Eingabetypen und `autocomplete`"
description: "Der richtige `type` bringt passende Tastatur, Prüfung und Bedienelemente mit. `autocomplete` lässt den Browser ausfüllen."
code:
  short: |-
    <input type="email" name="email" autocomplete="email">
    <input type="tel" name="phone" autocomplete="tel">
    <input type="date" name="birthday" autocomplete="bday">
    <input type="password" name="password" autocomplete="new-password">
  long: |-
    <input type="text" name="email" class="js-email">
    <input type="text" name="phone" class="js-phone">
    <input type="text" name="birthday" class="js-datepicker">
    <input type="password" name="password">
    <!-- dazu: eigene Prüfung, eigener Datepicker, eigene Tastaturlogik -->
explain:
  picture: "Der Eingabetyp ist wie ein vorgedrucktes Papierformular: Beim Datum steht TT.MM.JJJJ schon da, bei der Telefonnummer gibt es Kästchen für Ziffern. Wer alles als Freitext anbietet, muss hinterher alles selbst prüfen."
  steps:
    - "`type=\"email\"` prüft das Format und zeigt auf dem Handy eine Tastatur mit @."
    - "`type=\"tel\"` öffnet ein Ziffernfeld, `type=\"date\"` den Datumswähler des Systems."
    - "`autocomplete` sagt dem Browser, welche gespeicherten Daten passen. `new-password` löst den Passwortgenerator aus, `current-password` das Ausfüllen beim Login."
    - "Der `name` bestimmt, unter welchem Schlüssel der Wert beim Absenden ans Backend geht."
  mistake: "`type=\"number\"` für Postleitzahlen, Telefon- oder Kartennummern benutzen. Führende Nullen gehen verloren, und das Mausrad verändert den Wert. Für Ziffernfolgen ohne Rechenbedeutung besser `type=\"text\"` mit `inputmode=\"numeric\"`."
  when: "Immer den passenden `type` und wo möglich `autocomplete`. Eigene Datepicker nur, wenn das Design es zwingend verlangt."
  question: "Welches `autocomplete` gehört an das Passwortfeld im Login-Formular?"
  answer: "`current-password`. `new-password` ist für Registrierung und Passwortänderung."
links:
  - text: "<input>-Typen"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/input"
  - text: "autocomplete"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Attributes/autocomplete"
  - text: "type=\"email\""
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/input/email"
---
