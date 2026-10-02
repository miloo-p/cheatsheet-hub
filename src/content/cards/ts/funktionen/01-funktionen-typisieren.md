---
title: "Funktionen typisieren"
description: "Parameter brauchen immer Typen. Den Rückgabetyp leitet TypeScript ab, explizit ist er aber eine gute Dokumentation."
code:
  short: |-
    const add = (a: number, b: number) => a + b;

    const formatPrice = (cents: number) =>
      `${(cents / 100).toFixed(2)} €`;
  long: |-
    function add(a: number, b: number): number {
      return a + b;
    }

    type Formatter = (cents: number) => string;

    const formatPrice: Formatter = function (cents) {
      return (cents / 100).toFixed(2) + " €";
    };
explain:
  picture: "Eine Funktionssignatur ist wie ein Steckdosenformat: Sie legt fest, welcher Stecker hineinpasst (Parameter) und was herauskommt (Rückgabe)."
  steps:
    - "Parameter ohne Typ werden zu `any`. Mit `noImplicitAny` (Teil von `strict`) ist das ein Fehler."
    - "Den Rückgabetyp leitet TypeScript aus den `return`-Anweisungen ab."
    - "Ein expliziter Rückgabetyp wird geprüft: Gibst du versehentlich etwas anderes zurück, meldet TypeScript den Fehler direkt in der Funktion statt erst beim Aufrufer."
    - "Ein Funktionstyp wie `Formatter` beschreibt die ganze Signatur. Weist du eine Funktion zu, bekommen ihre Parameter die Typen automatisch."
  mistake: "Einen Zweig ohne `return` vergessen. Ohne Rückgabetyp wird daraus still `string | undefined`, und der Fehler taucht erst weit entfernt beim Aufrufer auf. Mit `: string` meldet TypeScript ihn sofort an der richtigen Stelle."
  when: "Kurz für kleine, lokale Hilfsfunktionen. Expliziter Rückgabetyp bei exportierten Funktionen, Services im Backend und allem, was andere benutzen."
  question: "Braucht `n` in `[1, 2].map(n => n * 2)` eine Annotation?"
  answer: "Nein. TypeScript weiß aus dem Array, dass `n` eine `number` ist (kontextuelle Typisierung). Annotieren musst du nur Parameter von Funktionen, die du selbst deklarierst."
links:
  - text: "Funktionen"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#functions"
  - text: "Funktionstypen"
    url: "https://www.typescriptlang.org/docs/handbook/2/functions.html#function-type-expressions"
  - text: "Kontextuelle Typisierung"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#anonymous-functions"
---
