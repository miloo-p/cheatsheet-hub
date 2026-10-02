---
title: "Typen erweitern: `extends` und `&`"
description: "Bestehende Typen um Felder ergänzen, statt alles doppelt zu schreiben."
code:
  short: "type Admin = User & { permissions: string[] };"
  long: |-
    interface Admin extends User {
      permissions: string[];
    }
explain:
  picture: "Wie eine Weiterbildung, die auf einer Ausbildung aufbaut: Ein Admin kann alles, was ein User kann, plus Rechte vergeben."
  steps:
    - "`interface Admin extends User` übernimmt alle Felder von `User` und fügt neue hinzu."
    - "`User & { ... }` (Intersection) bildet einen Typ, der beide Teile gleichzeitig erfüllen muss. Das Ergebnis ist hier dasselbe."
    - "Überall, wo ein `User` erwartet wird, darf ein `Admin` übergeben werden, weil er alle User-Felder hat."
  mistake: "Bei Konflikten verhalten sich beide unterschiedlich. Haben beide Teile ein Feld `id` mit verschiedenen Typen, meldet `extends` sofort einen Fehler, während `&` still den unmöglichen Typ `never` für `id` erzeugt."
  when: "`extends` bei Interfaces, weil die Fehlermeldungen klarer sind. `&` mit `type`, z.B. um schnell ein Feld an einen vorhandenen Typ zu hängen."
  question: "Darf man einen `Admin` an eine Funktion übergeben, die einen `User` erwartet? Und umgekehrt?"
  answer: "Admin an User: ja, er hat alle nötigen Felder. User an Admin: nein, ihm fehlt `permissions`."
links:
  - text: "Typen erweitern"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#extending-types"
  - text: "Intersection Types"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types"
  - text: "extends vs. Intersection"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#interface-extension-vs-intersection"
---
