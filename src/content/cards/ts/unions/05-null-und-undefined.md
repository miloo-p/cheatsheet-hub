---
title: "`null` und `undefined`"
description: "Mit `strict` zwingt TypeScript dich, `null` und `undefined` zu behandeln. Das `!` schaltet diese Prüfung an einer Stelle ab."
code:
  short: |-
    const input = document.querySelector<HTMLInputElement>("#email")!;
    input.value = "";

    const name = user?.name ?? "Gast";
  long: |-
    const input = document.querySelector<HTMLInputElement>("#email");
    if (input === null) {
      throw new Error("#email fehlt im HTML");
    }
    input.value = "";

    let name: string;
    if (user !== undefined && user.name !== undefined) {
      name = user.name;
    } else {
      name = "Gast";
    }
explain:
  picture: "`!` ist ein Versprechen an den Compiler: „Da ist ganz sicher etwas.“ Hältst du es nicht, stürzt das Programm zur Laufzeit trotzdem ab."
  steps:
    - "`querySelector` gibt `HTMLInputElement | null` zurück, weil das Element fehlen könnte."
    - "Das `!` am Ende (Non-null Assertion) entfernt `null` aus dem Typ, ohne etwas zu prüfen."
    - "Die ausführliche Variante prüft wirklich und wirft einen Fehler mit klarer Meldung."
    - "Nach der Prüfung weiß TypeScript, dass `input` nicht `null` ist."
  mistake: "`!` überall verteilen, um Fehlermeldungen loszuwerden. Dann hast du im Grunde wieder JavaScript ohne Prüfung, und „Cannot read properties of null“ kommt zurück."
  when: "`?.` und `??` für Werte, die legitim fehlen dürfen. `!` nur, wenn du es wirklich garantieren kannst. Eine echte Prüfung, wenn ein Fehlen ein Fehler im Programm wäre."
  question: "Was ist der Unterschied zwischen `user?.name` und `user!.name`?"
  answer: "`user?.name` prüft zur Laufzeit und ergibt `undefined`, wenn `user` fehlt. `user!.name` prüft nichts und stürzt ab, wenn `user` fehlt. Es beruhigt nur den Compiler."
links:
  - text: "null und undefined"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#null-and-undefined"
  - text: "Non-null Assertion (!)"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#non-null-assertion-operator-postfix-"
  - text: "strictNullChecks"
    url: "https://www.typescriptlang.org/tsconfig/#strictNullChecks"
---
