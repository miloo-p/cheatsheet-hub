---
title: "Shorthand und dynamische Keys"
description: "Heißen Variable und Key gleich, reicht der Name einmal. `[ ]` im Objekt berechnet den Key. Klassiker im Formular-Handler."
code:
  short: |-
    const user = { name, age };

    const handleChange = e =>
      setForm({ ...form, [e.target.name]: e.target.value });
  long: |-
    const user = { name: name, age: age };

    function handleChange(event) {
      const field = event.target.name;
      const value = event.target.value;
      const newForm = Object.assign({}, form);
      newForm[field] = value;
      setForm(newForm);
    }
explain:
  picture: "Shorthand spart eine Wiederholung: Heißen Feld und Variable gleich, reicht der Name einmal. Eckige Klammern sind ein Platzhalter für einen Feldnamen, der erst zur Laufzeit feststeht."
  steps:
    - "`{ name, age }` wird intern zu `{ name: name, age: age }`."
    - "Im Formular hat jedes Input ein `name`-Attribut, z.B. `email`."
    - "`[e.target.name]` setzt den Wert dieses Attributs als Schlüssel ein. So reicht ein einziger Handler für alle Felder."
    - "Der Spread davor übernimmt alle anderen Formularfelder unverändert."
  mistake: "Die eckigen Klammern vergessen: `{ field: value }` legt wörtlich ein Feld namens `field` an, statt den Inhalt der Variable zu nehmen."
  when: "Ein generischer `handleChange` mit dynamischem Key spart bei großen Formularen viel doppelten Code."
  question: "Was ist der Unterschied zwischen `{ [key]: \"Berlin\" }` und `{ key: \"Berlin\" }`, wenn `key = \"city\"`?"
  answer: "Das erste ergibt `{ city: \"Berlin\" }`, das zweite `{ key: \"Berlin\" }`. Nur die eckigen Klammern werten die Variable aus."
links:
  - text: "Objekt-Initialisierer (Shorthand, berechnete Keys)"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Object_initializer"
---
