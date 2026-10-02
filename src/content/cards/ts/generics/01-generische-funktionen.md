---
title: "Generische Funktionen"
description: "Ein Typ-Parameter `<T>` ist ein Platzhalter, den TypeScript bei jedem Aufruf mit dem passenden Typ füllt."
code:
  short: |-
    function first<T>(items: T[]) {
      return items[0];
    }

    const n = first([1, 2, 3]);    // number
    const s = first(["a", "b"]);   // string
  long: |-
    function first<T>(items: T[]): T | undefined {
      return items[0];
    }

    const n = first<number>([1, 2, 3]);
    const s = first<string>(["a", "b"]);
explain:
  picture: "Generics sind wie eine Ausstechform: Die Form bleibt gleich, aber welchen Teig du hineindrückst, entscheidet der Aufrufer. Heraus kommt immer das Material, das hineinging."
  steps:
    - "`<T>` deklariert einen Typ-Platzhalter, wie ein Parameter, nur für Typen."
    - "`items: T[]` heißt: ein Array von irgendwas, aber alle Elemente vom selben Typ."
    - "Beim Aufruf mit `[1, 2, 3]` erkennt TypeScript `T = number` und setzt es überall ein."
    - "Dadurch ist der Rückgabetyp `number` statt `any`. Die Information geht nicht verloren."
  mistake: "`any` statt Generics benutzen: `function first(items: any[]): any`. Das funktioniert, aber das Ergebnis ist ungeprüft, und `first([1, 2]).toUpperCase()` fällt nicht mehr auf."
  when: "Den Typ meist ableiten lassen. Explizit `<number>` angeben, wenn TypeScript nichts ableiten kann, z.B. bei `useState<User | null>(null)` oder einem leeren Array."
  question: "Warum ist `T | undefined` als Rückgabetyp in der ausführlichen Variante ehrlicher?"
  answer: "Weil `items[0]` bei einem leeren Array `undefined` ist. Ohne `| undefined` behauptet der Typ, es komme immer ein `T` zurück."
links:
  - text: "Generics"
    url: "https://www.typescriptlang.org/docs/handbook/2/generics.html"
  - text: "Typ-Variablen"
    url: "https://www.typescriptlang.org/docs/handbook/2/generics.html#working-with-generic-type-variables"
---
