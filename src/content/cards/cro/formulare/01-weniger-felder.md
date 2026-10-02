---
title: "Weniger Felder"
description: "Laut Baymard kommt ein guter Checkout mit 7 bis 8 Formularfeldern aus. Der Durchschnitt liegt bei fast 15."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <input name="anrede">       <input name="titel">
    <input name="vorname">      <input name="nachname">
    <input name="firma">        <input name="strasse">
    <input name="hausnummer">   <input name="adresszusatz">
    <input name="plz">          <input name="ort">
    <input name="land">         <input name="telefon">
    <input name="email">        <input name="email2">
    <input name="geburtsdatum">
  long: |-
    <input name="name" autocomplete="name">
    <input name="email" type="email" autocomplete="email">
    <input name="street" autocomplete="street-address">
    <input name="zip" autocomplete="postal-code" inputmode="numeric">
    <input name="city" autocomplete="address-level2">

    <details>
      <summary>Firma oder Adresszusatz hinzufügen</summary>
      <input name="company" autocomplete="organization">
      <input name="addressLine2" autocomplete="address-line2">
    </details>
explain:
  picture: "Jedes Formularfeld ist eine kleine Hürde auf einem Hindernislauf. Zehn Hürden schaffen die meisten noch, aber bei jeder fällt jemand. Die beste Hürde ist die, die gar nicht erst aufgestellt wird."
  steps:
    - "Für jedes Feld fragen: Brauchen wir es wirklich für diese Bestellung? Geburtsdatum, Anrede und Telefon oft nicht."
    - "Doppelte Eingaben wie E-Mail-Wiederholung sind meist überflüssig. Ein sichtbarer Wert zum Prüfen reicht."
    - "Ein Namensfeld statt Vor- und Nachname spart ein Feld, solange das Backend nicht zwingend getrennte Werte braucht."
    - "Selten nötige Felder wie Firma oder Adresszusatz werden hinter einem Link oder `<details>` versteckt."
    - "Die Land-Auswahl lässt sich oft aus der Sprache oder IP vorbelegen, die Stadt aus der Postleitzahl."
  mistake: "Felder nur im Frontend entfernen, aber im Backend weiterhin als Pflicht validieren. Dann scheitert die Bestellung an einem Feld, das niemand ausfüllen konnte. Frontend- und Backend-Validierung müssen zusammenpassen."
  when: "Abschlussrate des Formulars und Abbruch pro Feld. Viele Analytics-Tools können Formular-Analysen, oder du trackst `field_focus` und `field_error` selbst."
  question: "Warum ist ein Feld „E-Mail wiederholen“ meist überflüssig?"
  answer: "Weil die meisten die Adresse einfach kopieren oder vom Browser ausfüllen lassen. Fehler fängt eine klare Anzeige der Adresse vor dem Absenden besser ab."
links:
  - text: "Checkout-Felder (Baymard, EN)"
    url: "https://baymard.com/lists/cart-abandonment-rate"
  - text: "autocomplete (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Attributes/autocomplete"
---
