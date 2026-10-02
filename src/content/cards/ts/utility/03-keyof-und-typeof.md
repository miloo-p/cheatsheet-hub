---
title: "`keyof` und `typeof`"
description: "Typen aus vorhandenen Werten ableiten, statt sie doppelt zu pflegen."
code:
  short: |-
    const ROLES = { admin: "Administrator", user: "Benutzer" } as const;

    type Role = keyof typeof ROLES;   // "admin" | "user"
  long: |-
    type Role = "admin" | "user";

    const ROLES: Record<Role, string> = {
      admin: "Administrator",
      user: "Benutzer",
    };
explain:
  picture: "`typeof` macht vom Objekt eine Blaupause, `keyof` liest daraus die Liste der Feldnamen ab."
  steps:
    - "`typeof ROLES` liefert im Typ-Kontext den Typ des Objekts mit all seinen Feldern."
    - "`keyof` davor macht daraus die Union der Keys: `\"admin\" | \"user\"`."
    - "Kommt im Objekt eine Rolle dazu, ist sie automatisch im Typ enthalten."
    - "Die ausführliche Variante geht den umgekehrten Weg: erst der Typ, dann das Objekt, das ihn erfüllen muss."
  mistake: "`typeof` in TypeScript mit `typeof` in JavaScript verwechseln. In einer Bedingung wie `typeof x === \"string\"` ist es der JavaScript-Operator zur Laufzeit. Nach `type X =` ist es der TypeScript-Operator, der einen Typ liefert."
  when: "Wert zuerst, wenn das Objekt die Quelle der Wahrheit ist, z.B. bei Konfigurationen. Typ zuerst, wenn der Typ von außen vorgegeben ist, z.B. durch die API oder die Datenbank."
  question: "Welchen Typ hat `keyof User`, wenn `User` die Felder `id` und `name` hat?"
  answer: "`\"id\" | \"name\"`."
links:
  - text: "keyof"
    url: "https://www.typescriptlang.org/docs/handbook/2/keyof-types.html"
  - text: "typeof"
    url: "https://www.typescriptlang.org/docs/handbook/2/typeof-types.html"
---
