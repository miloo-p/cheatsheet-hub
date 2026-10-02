---
title: "Generische Typen"
description: "Auch Typen können Platzhalter haben. So beschreibst du eine Hülle einmal und füllst sie mit wechselndem Inhalt."
code:
  short: |-
    type ApiResponse<T> = { data: T; error: string | null };

    const res: ApiResponse<User[]> = await getUsers();
  long: |-
    interface ApiResponse<T> {
      data: T;
      error: string | null;
    }

    type UsersResponse = ApiResponse<User[]>;

    const res: UsersResponse = await getUsers();
explain:
  picture: "`ApiResponse<T>` ist ein Versandkarton mit Standardaufdruck (Daten, Fehlerfeld). Was drinliegt, steht auf dem Etikett: `<User[]>` oder `<Todo>`."
  steps:
    - "`ApiResponse<T>` definiert die Hülle mit einem Platzhalter `T` für den Inhalt."
    - "`ApiResponse<User[]>` setzt `T = User[]` ein. `data` hat jetzt den Typ `User[]`."
    - "Dieselbe Hülle funktioniert für jeden Endpunkt: `ApiResponse<Todo>`, `ApiResponse<number>` und so weiter."
    - "Du kennst das Muster schon: `Promise<User>` und `Array<string>` sind ebenfalls generische Typen."
  mistake: "Für jeden Endpunkt ein eigenes, fast gleiches Interface anlegen (`UsersResponse`, `TodosResponse` …). Ändert sich das Antwortformat, musst du alle einzeln anpassen."
  when: "Ein Alias wie `UsersResponse` lohnt sich, wenn der zusammengesetzte Typ oft vorkommt. Sonst `ApiResponse<User[]>` direkt schreiben."
  question: "Welchen Typ hat `res.data[0].name`, wenn `res` vom Typ `ApiResponse<User[]>` ist?"
  answer: "`string`, also der Typ von `User.name`. TypeScript reicht den Typ durch alle Ebenen durch."
links:
  - text: "Generische Typen"
    url: "https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-types"
  - text: "Generische Objekttypen"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#generic-object-types"
---
