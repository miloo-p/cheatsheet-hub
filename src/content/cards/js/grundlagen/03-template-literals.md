---
title: "Template Literals"
description: "Backticks mit `${}` statt Strings mit `+` zusammenzukleben."
code:
  short: "const msg = `Hallo ${name}, du hast ${cart.length} Artikel.`;"
  long: "const msg = \"Hallo \" + name + \", du hast \" + cart.length + \" Artikel.\";"
explain:
  picture: "Ein Template Literal ist ein Lückentext. Der Text steht fest, und in die `${}`-Lücken setzt JavaScript zur Laufzeit die Werte ein."
  steps:
    - "Backticks statt Anführungszeichen markieren den Lückentext."
    - "In `${}` steht ein beliebiger Ausdruck: Variable, Rechnung, Funktionsaufruf oder Ternär."
    - "Das Ergebnis wird automatisch in Text umgewandelt und eingesetzt."
    - "Zeilenumbrüche im Template bleiben erhalten, ohne `\\n`."
  mistake: "Normale Anführungszeichen benutzen: `\"Hallo ${name}\"` gibt wörtlich das Dollarzeichen aus. Und beim Verketten mit `+`: `\"Summe: \" + 1 + 2` ergibt `\"Summe: 12\"`, weil von links nach rechts zu Text verkettet wird."
  when: "Template Literals, sobald eine Variable im Text vorkommt. Die `+`-Variante solltest du lesen können, weil sie in älterem Code überall steht."
  question: "Was ergibt `\"Summe: \" + 1 + 2` und was ein Template mit `Summe: ${1 + 2}`?"
  answer: "Das erste ergibt `Summe: 12`, das Template rechnet zuerst und ergibt `Summe: 3`."
links:
  - text: "Template Literals"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Template_literals"
---
