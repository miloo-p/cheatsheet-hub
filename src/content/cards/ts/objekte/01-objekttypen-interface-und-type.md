---
title: "Objekttypen: `interface` und `type`"
description: "Objekttypen kannst du direkt hinschreiben oder einmal benennen und wiederverwenden."
code:
  short: |-
    function printUser(user: { name: string; age: number }) {
      console.log(`${user.name} (${user.age})`);
    }
  long: |-
    interface User {
      name: string;
      age: number;
    }
    // oder: type User = { name: string; age: number };

    function printUser(user: User): void {
      console.log(user.name + " (" + user.age + ")");
    }
explain:
  picture: "Ein Interface ist ein Steckbrief: Wer als `User` durchgehen will, muss mindestens diese Felder mit diesen Typen haben."
  steps:
    - "Ein Inline-Typ gilt nur an dieser einen Stelle."
    - "`interface` oder `type` geben der Form einen Namen, den du überall importieren kannst."
    - "TypeScript vergleicht nach Struktur, nicht nach Namen: Jedes Objekt mit `name` und `age` passt, egal wo es herkommt."
    - "Für Objekte sind `interface` und `type` fast austauschbar. `type` kann zusätzlich Unions benennen, ein `interface` kann nachträglich erweitert werden."
  mistake: "Ein Objekt-Literal mit Extra-Feldern direkt übergeben: `printUser({ name: \"Lea\", age: 31, admin: true })` ist ein Fehler (Excess Property Check). Bei einer Variable mit Extra-Feldern prüft TypeScript das nicht."
  when: "Inline für einmalige, kleine Typen. Sobald ein Typ zweimal vorkommt oder Frontend und Backend ihn teilen, benennen. Viele Teams nehmen `interface` für Objekte und `type` für alles andere."
  question: "Darf man ein Objekt `{ name: \"Lea\", age: 31, city: \"Köln\" }` aus einer Variable an `printUser` übergeben?"
  answer: "Ja. Es hat alle geforderten Felder, und Extra-Felder sind bei Variablen erlaubt. Nur direkt hingeschriebene Objekt-Literale werden auf Extra-Felder geprüft."
links:
  - text: "Objekttypen"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#object-types"
  - text: "Interfaces"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#interfaces"
  - text: "type vs. interface"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces"
  - text: "Excess Property Checks"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#excess-property-checks"
---
