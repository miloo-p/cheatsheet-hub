---
title: "`Partial` und `Required`"
description: "`Partial<T>` macht alle Felder optional. Ideal für PATCH-Requests, bei denen nur ein Teil geändert wird."
code:
  short: |-
    function updateUser(id: number, changes: Partial<User>) { ... }

    updateUser(1, { age: 32 });
  long: |-
    interface UserUpdate {
      name?: string;
      age?: number;
      email?: string;
    }

    function updateUser(id: number, changes: UserUpdate): void { ... }

    updateUser(1, { age: 32 });
explain:
  picture: "`Partial` ist ein Änderungsformular, auf dem du nur die Felder ausfüllst, die sich ändern sollen."
  steps:
    - "`Partial<User>` erzeugt einen neuen Typ, in dem jedes Feld von `User` ein `?` bekommt."
    - "Das Original-Interface bleibt unverändert."
    - "Kommt in `User` ein neues Feld dazu, ist es automatisch auch in `Partial<User>` enthalten."
    - "Das Gegenstück `Required<T>` entfernt alle `?` und macht jedes Feld zur Pflicht."
  mistake: "Das von Hand geschriebene `UserUpdate` nicht pflegen. Bekommt `User` ein neues Feld `city`, fehlt es in `UserUpdate`, und niemand merkt es. Mit `Partial<User>` kann das nicht passieren."
  when: "Fast immer die Utility-Type-Variante. Ein eigenes Interface nur, wenn bewusst nicht alle Felder änderbar sein sollen. Dann aber besser `Partial<Omit<User, \"id\">>`."
  question: "Ist `{}` ein gültiger Wert für `Partial<User>`?"
  answer: "Ja, weil alle Felder optional sind. Wenn ein leerer Update-Request nicht erlaubt sein soll, musst du das zusätzlich zur Laufzeit prüfen."
links:
  - text: "Partial"
    url: "https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype"
  - text: "Required"
    url: "https://www.typescriptlang.org/docs/handbook/utility-types.html#requiredtype"
---
