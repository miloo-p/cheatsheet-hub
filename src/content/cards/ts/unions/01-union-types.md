---
title: "Union Types"
description: "Ein Wert kann einer von mehreren Typen sein. Vor der Verwendung engst du ihn per Prüfung ein (Narrowing)."
code:
  short: |-
    function formatId(id: string | number) {
      return typeof id === "number" ? id.toFixed(0) : id.toUpperCase();
    }
  long: |-
    type Id = string | number;

    function formatId(id: Id): string {
      if (typeof id === "number") {
        return id.toFixed(0);     // hier: number
      }
      return id.toUpperCase();    // hier: string
    }
explain:
  picture: "Eine Union ist ein Paket mit dem Aufkleber „Buch ODER DVD“. Bevor du es benutzt, schaust du hinein. Danach weißt du genau, was du in der Hand hast."
  steps:
    - "Auf `string | number` darfst du nur benutzen, was beide Typen können, z.B. `toString()`."
    - "`typeof id === \"number\"` ist eine Prüfung, die TypeScript versteht."
    - "Im `if`-Zweig ist `id` daher eine `number`, und `toFixed` ist erlaubt."
    - "Nach dem `return` weiß TypeScript: Im Rest der Funktion kann `id` nur noch ein `string` sein."
  mistake: "Direkt `id.toUpperCase()` aufrufen. TypeScript meldet, dass es `toUpperCase` auf `number` nicht gibt. Die Lösung ist eine Prüfung, kein `as string`."
  when: "Ternär bei zwei kurzen Fällen. `if` mit frühem `return`, sobald pro Fall mehr passiert. Einen Alias wie `Id`, wenn die Union mehrfach vorkommt."
  question: "Welchen Typ hat `id` im `else`-Zweig von `if (typeof id === \"string\")` bei `string | number | boolean`?"
  answer: "`number | boolean`. TypeScript zieht nur den geprüften Typ ab."
links:
  - text: "Union Types"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types"
  - text: "typeof Type Guards"
    url: "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#typeof-type-guards"
  - text: "Type Aliases"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases"
---
