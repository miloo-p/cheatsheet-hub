---
title: "`unknown` statt `any`"
description: "`any` schaltet die Prüfung ab. `unknown` heißt: Typ noch unbekannt, erst prüfen, dann benutzen."
code:
  short: |-
    const data = JSON.parse(text) as User; // ungeprüft!
    console.log(data.name);
  long: |-
    const data: unknown = JSON.parse(text);

    if (typeof data === "object" && data !== null && "name" in data) {
      console.log(data.name);
    }
explain:
  picture: "`any` ist ein Paket ohne Kontrolle, es geht einfach durch. `unknown` ist ein Paket, das am Zoll festgehalten wird, bis du nachgesehen hast, was drin ist."
  steps:
    - "`JSON.parse` gibt `any` zurück. TypeScript weiß nicht, was im Text stand."
    - "`as User` ist eine Behauptung: Du sagst dem Compiler „vertrau mir“. Geprüft wird dabei nichts."
    - "Mit `unknown` verlangt TypeScript eine Prüfung, bevor du auf Eigenschaften zugreifst."
    - "Jede Prüfung (`typeof`, `!== null`, `in`) engt den Typ weiter ein, bis der Zugriff sicher ist."
  mistake: "`as` benutzen, um rote Unterstreichungen loszuwerden. Der Fehler verschwindet aus dem Editor, aber nicht aus dem Programm: Fehlt `name` wirklich, stürzt es zur Laufzeit ab."
  when: "`as` nur, wenn du es wirklich besser weißt als der Compiler. Für Daten von außen (API, JSON, Formulare) `unknown` plus Prüfung, im Projekt am besten mit einer Bibliothek wie Zod (siehe Karte „Daten von außen prüfen“)."
  question: "Was passiert zur Laufzeit bei `const u = JSON.parse(\"{}\") as User; u.name.toUpperCase()`?"
  answer: "Ein TypeError, weil `u.name` `undefined` ist. `as` hat nichts geprüft, sondern nur den Compiler beruhigt."
links:
  - text: "any"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#any"
  - text: "unknown"
    url: "https://www.typescriptlang.org/docs/handbook/2/functions.html#unknown"
  - text: "Type Assertions (as)"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions"
---
