---
title: "Listen"
description: "Aufzählungen als echte Listen auszeichnen. Nummerierung und Ansage übernimmt der Browser."
code:
  short: |-
    <ol>
      <li>Repository klonen</li>
      <li><code>npm install</code> ausführen</li>
      <li>Server starten</li>
    </ol>
  long: |-
    <div class="steps">
      <p>1. Repository klonen</p>
      <p>2. <code>npm install</code> ausführen</p>
      <p>3. Server starten</p>
    </div>
explain:
  picture: "Eine echte Liste ist ein Einkaufszettel, den der Screenreader mit „Liste, 3 Einträge“ ankündigt. Absätze mit Nummern davor sind lose Zettel ohne Zusammenhang."
  steps:
    - "`<ol>` ist eine geordnete Liste, die Reihenfolge zählt. `<ul>` ist eine ungeordnete Liste."
    - "Jeder Eintrag steht in einem `<li>`."
    - "Die Nummerierung erzeugt der Browser. Fügst du einen Schritt ein, zählt er automatisch neu."
    - "Screenreader sagen die Anzahl der Einträge an, und man kann von Liste zu Liste springen."
  mistake: "Text oder ein `<div>` direkt in eine `<ul>` schreiben. Erlaubte Kinder sind nur `<li>` (plus `<script>` und `<template>`). Auch Navigationsmenüs sind typischerweise eine `<ul>` in `<nav>`."
  when: "Immer echte Listen. Das Aussehen, z.B. ohne Aufzählungspunkte, regelst du mit `list-style: none` im CSS."
  question: "Wie lässt du eine `<ol>` bei 5 statt bei 1 beginnen?"
  answer: "Mit dem Attribut `start`, also `<ol start=\"5\">`."
links:
  - text: "<ol>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/ol"
  - text: "<ul>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/ul"
  - text: "<li>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/li"
---
