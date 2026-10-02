---
title: "Named vs. Default Export"
description: "Named Exports gibt es beliebig viele, Import mit gleichem Namen in `{}`. Default nur einen pro Datei, Name beim Import frei wählbar."
code:
  short: |-
    // utils.js
    export const formatPrice = p => `${p.toFixed(2)} €`;
    export default function api() { ... }

    // app.js
    import api, { formatPrice } from "./utils.js";
  long: |-
    // utils.js
    function formatPrice(price) {
      return price.toFixed(2) + " €";
    }
    function api() { ... }

    export { formatPrice };
    export default api;

    // app.js
    import api from "./utils.js";
    import { formatPrice } from "./utils.js";
explain:
  picture: "Eine Datei ist ein Laden. Named Exports sind die Artikel im Regal, jeder mit festem Namen. Der Default Export ist das Hauptprodukt im Schaufenster, das du beim Mitnehmen beliebig nennen darfst."
  steps:
    - "`export` vor einer Deklaration exportiert sie direkt unter ihrem Namen."
    - "Alternativ definierst du erst alles und exportierst am Ende gesammelt mit `export { ... }`."
    - "Named Imports in `{}` müssen exakt so heißen wie der Export, oder du benennst sie mit `as` um."
    - "Der Default Import steht ohne Klammern, und der Name ist frei wählbar."
  mistake: "Die Klammern verwechseln: `import { api } from ...` findet keinen Default Export, und `import formatPrice from ...` bekommt den Default statt der benannten Funktion. In Node mit ES-Modulen muss außerdem die Endung `.js` im Pfad stehen."
  when: "Viele Teams bevorzugen Named Exports, weil die Namen beim Umbenennen und in der Autovervollständigung stabil bleiben. React-Komponenten werden oft per Default exportiert. Wichtig ist, im Projekt einheitlich zu bleiben."
  question: "Wie viele Default Exports darf eine Datei haben?"
  answer: "Genau einen. Named Exports beliebig viele."
links:
  - text: "JavaScript-Module"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Guide/Modules"
  - text: "export"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/export"
  - text: "import"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/import"
---
