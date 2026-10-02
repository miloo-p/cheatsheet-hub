---
title: "Daten von außen prüfen"
description: "Typen existieren nur beim Programmieren. Daten von außen müssen zur Laufzeit geprüft werden, sonst lügt der Typ."
code:
  short: |-
    import { z } from "zod";

    const UserSchema = z.object({ id: z.number(), name: z.string() });
    type User = z.infer<typeof UserSchema>;

    const user = UserSchema.parse(await res.json());
  long: |-
    interface User { id: number; name: string; }

    function isUser(value: unknown): value is User {
      return (
        typeof value === "object" && value !== null &&
        "id" in value && typeof value.id === "number" &&
        "name" in value && typeof value.name === "string"
      );
    }

    const data: unknown = await res.json();
    if (!isUser(data)) {
      throw new Error("Ungültige Antwort");
    }
    const user = data; // ab hier: User
explain:
  picture: "TypeScript ist die Gästeliste, die Laufzeitprüfung ist der Türsteher. Eine Liste allein hält niemanden auf, erst der Türsteher kontrolliert wirklich."
  steps:
    - "Was vom Server, aus einem Formular oder aus `localStorage` kommt, ist für TypeScript unbekannt."
    - "Die ausführliche Variante prüft jedes Feld von Hand und meldet das Ergebnis per Type Guard."
    - "Zod beschreibt die Form einmal als Schema. `parse` prüft zur Laufzeit und wirft einen Fehler, wenn etwas nicht passt."
    - "`z.infer` leitet den TypeScript-Typ aus dem Schema ab. So gibt es nur eine Quelle der Wahrheit."
  mistake: "Im Backend `req.body as CreateUserDto` schreiben und glauben, die Eingabe sei damit geprüft. Jeder kann beliebiges JSON schicken. Gerade im Backend ist Validierung Pflicht."
  when: "Für eine einzelne kleine Prüfung reicht ein Type Guard. Sobald es mehrere Endpunkte gibt, lohnt sich eine Bibliothek wie Zod, im Frontend wie im Backend."
  question: "Warum reicht `const user: User = await res.json()` nicht als Prüfung?"
  answer: "Weil `res.json()` `any` liefert und `any` zu jedem Typ passt. TypeScript prüft hier nichts, der Typ ist nur eine Behauptung."
links:
  - text: "Type Predicates"
    url: "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates"
  - text: "unknown"
    url: "https://www.typescriptlang.org/docs/handbook/2/functions.html#unknown"
  - text: "Zod"
    url: "https://zod.dev"
---
