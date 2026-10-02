---
title: "Links: neue Tabs und Sprungmarken"
description: "Externe Links in neuen Tabs öffnen und zu Stellen auf derselben Seite springen."
code:
  short: |-
    <a href="https://developer.mozilla.org" target="_blank">MDN</a>

    <a href="#kontakt">Zum Kontakt</a>
    <section id="kontakt">...</section>
  long: |-
    <a href="https://developer.mozilla.org" target="_blank"
       rel="noopener noreferrer">MDN</a>

    <a href="#" onclick="document.getElementById('kontakt').scrollIntoView(); return false;">
      Zum Kontakt
    </a>
    <section id="kontakt">...</section>
explain:
  picture: "Ein Anker wie `#kontakt` ist ein Lesezeichen im Buch: Der Link schlägt die Seite genau an dieser Stelle auf, und die Adresse merkt sich die Stelle."
  steps:
    - "`target=\"_blank\"` öffnet den Link in einem neuen Tab."
    - "Früher konnte die neue Seite über `window.opener` die alte Seite manipulieren. Darum schrieb man `rel=\"noopener\"` dazu."
    - "Moderne Browser setzen `noopener` bei `target=\"_blank\"` automatisch. `noreferrer` verhindert zusätzlich, dass die Zielseite erfährt, woher der Besuch kam."
    - "`href=\"#kontakt\"` springt zum Element mit `id=\"kontakt\"`. Das funktioniert ohne JavaScript, mit Zurück-Button und als teilbarer Link."
  mistake: "Sprungmarken mit JavaScript nachbauen. Dann funktionieren Zurück-Button, Lesezeichen und Teilen nicht. Ebenfalls häufig: Linktexte wie „hier klicken“. Screenreader-Nutzer lassen sich oft alle Links auflisten, und dann steht dort zehnmal „hier“."
  when: "Die Kurzform reicht in aktuellen Browsern. `rel=\"noopener noreferrer\"` schadet nicht und ist bei fremden Seiten ein gutes Sicherheitsnetz. Für sanftes Scrollen genügt im CSS `scroll-behavior: smooth`."
  question: "Wie verhinderst du, dass das Sprungziel unter einem Sticky-Header verschwindet?"
  answer: "Mit `scroll-margin-top` im CSS auf dem Ziel, z.B. `section { scroll-margin-top: 5rem; }`."
links:
  - text: "<a>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/a"
  - text: "rel=\"noopener\""
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Attributes/rel/noopener"
  - text: "scroll-margin-top"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/scroll-margin-top"
---
