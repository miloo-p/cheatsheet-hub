---
title: "Typinferenz und Basistypen"
description: "TypeScript erkennt den Typ meist selbst aus dem Wert (Inferenz). Annotieren musst du nur dort, wo es nichts abzuleiten gibt."
code:
  short: |-
    let name = "Lea";        // string
    let age = 31;            // number
    let isAdmin = false;     // boolean
    const scores = [3, 5];   // number[]
  long: |-
    let name: string = "Lea";
    let age: number = 31;
    let isAdmin: boolean = false;
    const scores: number[] = [3, 5];
    // gleichwertig: Array<number>
explain:
  picture: "TypeScript ist wie ein aufmerksamer Kollege, der beim Lesen mitdenkt: Steht da `= \"Lea\"`, ist klar, dass das Text ist. Das muss niemand extra dazuschreiben."
  steps:
    - "Beim Zuweisen schaut TypeScript auf den Wert rechts und merkt sich den passenden Typ."
    - "Ab dann prüft es jede Verwendung: `age = \"alt\"` wird rot markiert, weil `age` eine `number` ist."
    - "Bei `const` wird der Typ sogar genauer: `const role = \"admin\"` hat den Typ `\"admin\"`, nicht nur `string`."
    - "Alle Typen verschwinden beim Kompilieren. Im ausgeführten JavaScript gibt es sie nicht mehr."
  mistake: "Ein leeres Array ohne Typ anlegen: Bei `const ids = []` kann TypeScript nichts ableiten, und der Typ wird `any[]` oder `never[]`. Hier immer annotieren: `const ids: number[] = []`."
  when: "Bei Variablen mit Startwert die Inferenz arbeiten lassen. Explizit annotieren, wenn es keinen Startwert gibt, der Startwert leer ist oder der Typ breiter sein soll als der erste Wert."
  question: "Welchen Typ hat `x` bei `let x;` ohne Wert und ohne Annotation?"
  answer: "TypeScript behandelt `x` zunächst als `any` und kann nichts prüfen. Darum Variablen ohne Startwert immer annotieren, z.B. `let x: string;`."
links:
  - text: "Typ-Annotationen"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-annotations-on-variables"
  - text: "Typinferenz"
    url: "https://www.typescriptlang.org/docs/handbook/type-inference.html"
  - text: "Arrays"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays"
---
