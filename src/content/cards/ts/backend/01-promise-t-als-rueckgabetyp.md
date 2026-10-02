---
title: "`Promise<T>` als Rückgabetyp"
description: "Eine `async`-Funktion gibt immer ein Promise zurück. Der Typ beschreibt, was beim `await` herauskommt."
code:
  short: |-
    async function getUser(id: number) {
      const res = await fetch(`/api/users/${id}`);
      return (await res.json()) as User;
    }
  long: |-
    async function getUser(id: number): Promise<User> {
      const res: Response = await fetch("/api/users/" + id);
      if (!res.ok) {
        throw new Error("HTTP " + res.status);
      }
      const user: User = await res.json();
      return user;
    }
explain:
  picture: "`Promise<User>` ist ein Abholschein mit Aufdruck: „Hier bekommst du später einen User.“"
  steps:
    - "`async` macht aus jedem Rückgabewert automatisch ein Promise. Aus `User` wird `Promise<User>`."
    - "`res.json()` liefert `Promise<any>`. TypeScript weiß nicht, was der Server schickt."
    - "Mit `as User` oder der Annotation `const user: User` legst du den Typ fest. Beides ist eine Behauptung, keine Prüfung."
    - "Wer `await getUser(1)` schreibt, bekommt ab dann einen typisierten `User`."
  mistake: "Den Rückgabetyp als `User` statt `Promise<User>` angeben. TypeScript meldet einen Fehler, weil eine `async`-Funktion immer ein Promise zurückgibt."
  when: "Expliziter Rückgabetyp `Promise<User>` bei allen API-Funktionen. Er dokumentiert, was der Aufrufer bekommt, und die ausführliche Variante prüft zusätzlich `res.ok`, was die kurze vergisst."
  question: "Welchen Typ hat `const u = getUser(1)` ohne `await`?"
  answer: "`Promise<User>`. Erst mit `await` bekommst du den `User` selbst."
links:
  - text: "Funktionen, die Promises zurückgeben"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#functions-which-return-promises"
  - text: "Rückgabetypen"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#return-type-annotations"
---
