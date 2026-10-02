---
title: "Nachschlage-Objekte: `Record`"
description: "Für Objekte, die wie Tabellen benutzt werden: beliebig viele Keys mit gleichem Werttyp."
code:
  short: |-
    const stock: Record<string, number> = { apple: 5, pear: 0 };

    type Lang = "de" | "en";
    const labels: Record<Lang, string> = { de: "Speichern", en: "Save" };
  long: |-
    const stock: { [product: string]: number } = { apple: 5, pear: 0 };

    const labels: { de: string; en: string } = {
      de: "Speichern",
      en: "Save",
    };
explain:
  picture: "Ein `Record` ist ein Wörterbuch: Links steht ein Stichwort, rechts immer dieselbe Art von Eintrag."
  steps:
    - "`Record<string, number>` heißt: Jeder String-Key hat einen Zahlenwert."
    - "Die Index-Signatur `{ [product: string]: number }` beschreibt dasselbe. Der Name `product` ist nur Dokumentation."
    - "Mit einer Union als Key-Typ wie `Record<Lang, string>` müssen alle Keys vorhanden sein. Fehlt `en`, meldet TypeScript einen Fehler."
    - "So vergisst du bei einer neuen Sprache oder einem neuen Status keine Übersetzung."
  mistake: "Annehmen, jeder Key existiere: `stock[\"banana\"]` hat laut TypeScript den Typ `number`, ist zur Laufzeit aber `undefined`. Die Option `noUncheckedIndexedAccess` macht daraus `number | undefined` und erzwingt eine Prüfung."
  when: "`Record` ist kürzer und gängiger. Die Index-Signatur brauchst du, wenn das Objekt zusätzlich feste Felder haben soll."
  question: "Was passiert, wenn du in `labels` ein Feld `fr` ergänzt, ohne `Lang` zu ändern?"
  answer: "Ein Fehler: `fr` ist kein erlaubter Key, weil `Lang` nur `\"de\"` und `\"en\"` enthält."
links:
  - text: "Record"
    url: "https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type"
  - text: "Index-Signaturen"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures"
  - text: "noUncheckedIndexedAccess"
    url: "https://www.typescriptlang.org/tsconfig/#noUncheckedIndexedAccess"
---
