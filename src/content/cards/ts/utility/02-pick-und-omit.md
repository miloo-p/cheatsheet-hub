---
title: "`Pick` und `Omit`"
description: "Aus einem bestehenden Typ Felder herausnehmen (`Omit`) oder nur bestimmte behalten (`Pick`)."
code:
  short: |-
    type PublicUser = Omit<User, "password">;
    type UserPreview = Pick<User, "id" | "name">;
  long: |-
    interface PublicUser {
      id: number;
      name: string;
      email: string;
    }

    interface UserPreview {
      id: number;
      name: string;
    }
explain:
  picture: "`Pick` ist eine Schere, die nur die markierten Felder ausschneidet. `Omit` ist ein Rotstift, der einzelne Felder durchstreicht."
  steps:
    - "Die Feldnamen gibst du als Literal-Union an: `\"id\" | \"name\"`."
    - "`Pick<User, \"id\" | \"name\">` baut einen Typ nur aus diesen Feldern."
    - "`Omit<User, \"password\">` baut einen Typ aus allen Feldern außer `password`."
    - "Beide bleiben mit `User` verbunden. Ändert sich ein Feldtyp in `User`, ändert er sich überall."
  mistake: "Annehmen, `Omit` entferne das Feld auch zur Laufzeit. Typen verschwinden beim Kompilieren: Gibst du im Backend ein komplettes User-Objekt mit Passwort zurück, wird es trotzdem verschickt. Das Feld musst du selbst entfernen, z.B. per Destructuring."
  when: "`Omit` für „alles außer sensiblen oder generierten Feldern“, `Pick` für kleine Vorschau-Typen. Ausgeschriebene Interfaces nur, wenn der Typ wirklich eigenständig ist."
  question: "Welche Felder hat `Omit<User, \"id\" | \"password\">`, wenn `User` die Felder `id`, `name`, `email` und `password` hat?"
  answer: "`name` und `email`."
links:
  - text: "Pick"
    url: "https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys"
  - text: "Omit"
    url: "https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys"
---
