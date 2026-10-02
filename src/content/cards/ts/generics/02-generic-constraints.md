---
title: "Generic Constraints"
description: "Mit `extends` legst du fest, was ein Typ-Parameter mindestens können muss."
code:
  short: |-
    function findById<T extends { id: number }>(items: T[], id: number) {
      return items.find(item => item.id === id);
    }
  long: |-
    interface HasId {
      id: number;
    }

    function findById<T extends HasId>(items: T[], id: number): T | undefined {
      return items.find(function (item: T): boolean {
        return item.id === id;
      });
    }
explain:
  picture: "Eine Einschränkung ist wie eine Stellenausschreibung: Bewerben darf sich jeder, aber eine ID ist Pflicht."
  steps:
    - "Ohne Einschränkung weiß TypeScript nichts über `T`. `item.id` wäre ein Fehler."
    - "`T extends HasId` heißt: `T` darf jeder Typ sein, der mindestens `id: number` hat."
    - "Darum ist `item.id` in der Funktion erlaubt."
    - "Der Rückgabetyp bleibt trotzdem der genaue Typ: Übergibst du `Todo[]`, kommt `Todo | undefined` zurück und nicht nur `HasId`."
  mistake: "Den Parameter direkt als `HasId[]` typisieren statt generisch. Dann kommt `HasId | undefined` zurück, und `result.title` ist ein Fehler, obwohl es ein Todo war."
  when: "Constraints immer dann, wenn deine generische Funktion auf bestimmte Felder zugreift. Typisch für Hilfsfunktionen in Repositories und Services."
  question: "Darf man `findById([\"a\", \"b\"], 1)` aufrufen?"
  answer: "Nein. Strings haben kein Feld `id: number`, also erfüllen sie die Einschränkung nicht."
links:
  - text: "Generic Constraints"
    url: "https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints"
---
