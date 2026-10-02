---
title: "Optionale und `readonly` Felder"
description: "`?` markiert Felder, die fehlen dürfen. `readonly` verbietet das Überschreiben nach dem Erstellen."
code:
  short: |-
    interface Todo {
      readonly id: number;
      title: string;
      dueDate?: string;
    }

    const label = todo.dueDate?.slice(0, 10) ?? "kein Datum";
  long: |-
    interface Todo {
      readonly id: number;
      title: string;
      dueDate?: string;
    }

    let label: string;
    if (todo.dueDate !== undefined) {
      label = todo.dueDate.slice(0, 10);
    } else {
      label = "kein Datum";
    }
explain:
  picture: "`readonly` ist ein Feld mit dem Stempel „nicht ändern“, wie eine Kundennummer. `?` ist ein Feld, das auf dem Formular leer bleiben darf."
  steps:
    - "`dueDate?: string` heißt: Das Feld kann fehlen, beim Lesen ist es `string | undefined`."
    - "Vor der Benutzung erzwingt TypeScript eine Prüfung. Nach `!== undefined` weiß es, dass ein `string` vorliegt (Narrowing)."
    - "`readonly id` erlaubt das Setzen beim Erstellen, aber `todo.id = 5` danach ist ein Fehler."
    - "`readonly` gilt nur beim Kompilieren. Im laufenden JavaScript ließe sich der Wert trotzdem ändern."
  mistake: "Annehmen, `readonly` mache das Objekt komplett unveränderlich. Es schützt nur die Eigenschaft selbst: Bei `readonly tags: string[]` ist `todo.tags.push(\"x\")` weiterhin erlaubt. Dafür bräuchte es `readonly string[]`."
  when: "Optional Chaining für schnelles Lesen. Die if-Variante, wenn im vorhandenen Fall mehr passieren soll als ein einzelner Ausdruck."
  question: "Ist `todo.dueDate.length` ohne Prüfung erlaubt?"
  answer: "Nein. `dueDate` könnte `undefined` sein, darum meldet TypeScript „possibly undefined“. Erst prüfen oder `?.` benutzen."
links:
  - text: "Optionale Felder"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#optional-properties"
  - text: "readonly"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#readonly-properties"
  - text: "Narrowing"
    url: "https://www.typescriptlang.org/docs/handbook/2/narrowing.html"
---
