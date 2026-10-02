---
title: "Eigene Type Guards"
description: "Eigene Prüffunktionen, die TypeScript als Narrowing versteht. Praktisch, wenn dieselbe Prüfung mehrfach vorkommt."
code:
  short: |-
    if ("permissions" in user) {
      showAdminPanel(user.permissions);
    }
  long: |-
    function isAdmin(user: User | Admin): user is Admin {
      return "permissions" in user;
    }

    if (isAdmin(user)) {
      showAdminPanel(user.permissions);
    }
explain:
  picture: "Ein Type Guard ist ein Ausweis-Scanner: Er prüft einmal, und danach behandelt jeder die Person entsprechend ihrem Ausweis."
  steps:
    - "Der `in`-Operator prüft, ob ein Feld existiert, und TypeScript engt den Typ daraufhin ein."
    - "Lagerst du die Prüfung in eine Funktion mit Rückgabe `boolean` aus, geht dieses Wissen verloren."
    - "Der Rückgabetyp `user is Admin` (Type Predicate) sagt TypeScript: Liefert die Funktion `true`, ist `user` ein `Admin`."
    - "Im `if` danach ist `user.permissions` deshalb erlaubt."
  mistake: "Eine falsche Prüfung schreiben. TypeScript glaubt dem Type Predicate blind: Prüft `isAdmin` das falsche Feld, ist der Typ trotzdem `Admin`, und der Fehler zeigt sich erst zur Laufzeit."
  when: "`in` oder `typeof` direkt für einmalige Prüfungen. Ein eigener Type Guard, wenn die Prüfung mehrfach gebraucht wird oder komplexer ist, z.B. für `unknown`-Daten."
  question: "Was ändert sich, wenn `isAdmin` nur `: boolean` statt `: user is Admin` zurückgibt?"
  answer: "Die Funktion läuft gleich, aber TypeScript engt den Typ im `if` nicht mehr ein. `user.permissions` wäre dann ein Fehler."
links:
  - text: "in-Operator"
    url: "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-in-operator-narrowing"
  - text: "Type Predicates"
    url: "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates"
---
