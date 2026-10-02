---
title: "Selektoren bündeln: `:is()` und `:where()`"
description: "Gemeinsame Teile von Selektoren zusammenfassen, statt sie zu wiederholen."
code:
  short: |-
    .nav :is(a, button):hover {
      color: var(--brand);
    }
  long: |-
    .nav a:hover,
    .nav button:hover {
      color: var(--brand);
    }
explain:
  picture: "`:is()` ist ein Oder-Platzhalter in einer Adresse: „In der Nav, ein Link oder ein Button, im Hover-Zustand.“"
  steps:
    - "`:is(a, button)` trifft jedes Element, das zu einem der Selektoren in der Klammer passt."
    - "Die kurze und die ausführliche Variante treffen genau dieselben Elemente."
    - "Die Spezifität von `:is()` entspricht dem stärksten Selektor in der Klammer."
    - "`:where()` funktioniert gleich, hat aber immer die Spezifität 0. Seine Regeln lassen sich leicht überschreiben, was für Basis-Styles praktisch ist."
  mistake: "Spezifität unterschätzen: `:is(#main, .content) p` hat die Spezifität einer ID, auch wenn das Element nur über `.content` getroffen wird. Spätere Regeln mit Klassen kommen dagegen nicht mehr an."
  when: "`:is()` bei langen, sich wiederholenden Selektorlisten. `:where()` für Basis-Styles, die bewusst schwach sein sollen. Zwei, drei ausgeschriebene Selektoren sind oft genauso lesbar."
  question: "Welche Regel gewinnt: `:where(.card) p { color: red }` oder ein späteres `p { color: blue }`?"
  answer: "Blau. `:where()` zählt 0, also haben beide Regeln dieselbe Spezifität wie ein einfacher Element-Selektor, und die spätere gewinnt. Mit `:is()` gewänne Rot, weil die Klasse dann zählt."
links:
  - text: ":is()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/:is"
  - text: ":where()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/:where"
  - text: "Spezifität"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/Specificity"
---
