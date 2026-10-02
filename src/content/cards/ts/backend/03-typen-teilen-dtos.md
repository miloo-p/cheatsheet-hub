---
title: "Typen teilen: DTOs"
description: "Frontend und Backend nutzen dieselben Typen. Ändert sich das API-Format, zeigen beide Seiten sofort Fehler."
code:
  short: |-
    // shared/types.ts
    export interface User { id: number; name: string; email: string; }
    export type CreateUserDto = Omit<User, "id">;

    // im Frontend und im Backend
    import type { User, CreateUserDto } from "../shared/types";
  long: |-
    // shared/types.ts
    export interface User {
      id: number;
      name: string;
      email: string;
    }

    export interface CreateUserDto {
      name: string;
      email: string;
    }

    // im Frontend und im Backend
    import { type User, type CreateUserDto } from "../shared/types";
explain:
  picture: "Ein gemeinsamer Typ ist ein Vertrag, den beide Seiten unterschreiben. Ändert eine Seite den Vertrag, sieht die andere es sofort."
  steps:
    - "Die Typen liegen in einem Ordner, auf den beide Projekte zugreifen, z.B. in einem Monorepo."
    - "Ein DTO (Data Transfer Object) beschreibt, was über die Leitung geht. Beim Anlegen gibt es noch keine `id`, die vergibt die Datenbank."
    - "`Omit<User, \"id\">` leitet das DTO vom User ab, statt die Felder doppelt zu schreiben."
    - "`import type` importiert nur Typen. Der Import verschwindet beim Kompilieren komplett, es landet kein Code im Bundle."
  mistake: "Typen im Frontend einfach abtippen. Benennt das Backend ein Feld um, z.B. `name` in `fullName`, kompiliert das Frontend weiter, zeigt aber `undefined` an."
  when: "`Omit` hält das DTO automatisch synchron. Ein ausgeschriebenes DTO ist sinnvoll, wenn sich Eingabe und gespeichertes Objekt bewusst unterscheiden, z.B. Klartext-Passwort beim Registrieren und Hash in der Datenbank."
  question: "Warum hat `CreateUserDto` keine `id`?"
  answer: "Weil der Client beim Anlegen noch keine ID kennt. Die vergibt der Server oder die Datenbank."
links:
  - text: "Typ-Importe (import type)"
    url: "https://www.typescriptlang.org/docs/handbook/2/modules.html#typescript-specific-es-module-syntax"
  - text: "Omit"
    url: "https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys"
---
