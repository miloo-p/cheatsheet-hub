---
title: "`margin` und `padding` kurz"
description: "Ein bis vier Werte statt vier einzelner Eigenschaften. Die Reihenfolge läuft im Uhrzeigersinn."
code:
  short: |-
    .button {
      padding: 8px 16px;
      margin: 0 auto 24px;
    }
  long: |-
    .button {
      padding-top: 8px;
      padding-right: 16px;
      padding-bottom: 8px;
      padding-left: 16px;

      margin-top: 0;
      margin-right: auto;
      margin-bottom: 24px;
      margin-left: auto;
    }
explain:
  picture: "Die Werte laufen im Uhrzeigersinn, wie ein Zeiger, der oben bei 12 Uhr startet: oben, rechts, unten, links. Merkhilfe: TRBL, ausgesprochen „Trouble“."
  steps:
    - "Vier Werte: oben, rechts, unten, links."
    - "Drei Werte: oben, dann links und rechts gemeinsam, dann unten."
    - "Zwei Werte: oben und unten gemeinsam, dann links und rechts gemeinsam."
    - "Ein Wert: alle vier Seiten gleich."
    - "Fehlende Werte übernimmt die gegenüberliegende Seite. Darum gilt bei `0 auto 24px` das `auto` für links und rechts."
  mistake: "Eine Kurzschreibweise nach einer Einzeleigenschaft setzen: Steht `padding: 8px` hinter `padding-left: 32px`, überschreibt es auch die linke Seite wieder mit 8px. Kurzschreibweisen setzen immer alle Teilwerte."
  when: "Die Kurzform fast immer. Einzeleigenschaften, wenn du gezielt nur eine Seite ändern willst, z.B. in einem Hover-Zustand oder einer Media Query."
  question: "Was bedeutet `margin: 10px 20px 30px`?"
  answer: "Oben 10px, links und rechts 20px, unten 30px."
links:
  - text: "margin"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/margin"
  - text: "padding"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/padding"
  - text: "Kurzschreibweisen"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/Shorthand_properties"
---
