---
title: "`useState` typisieren"
description: "Bei eindeutigen Startwerten leitet React den Typ ab. Startet der State leer, musst du ihn angeben."
code:
  short: |-
    const [count, setCount] = useState(0);              // number
    const [user, setUser] = useState<User | null>(null);
  long: |-
    const [count, setCount] = useState<number>(0);

    type MaybeUser = User | null;
    const [user, setUser] = useState<MaybeUser>(null);
explain:
  picture: "Der Startwert ist das erste Teil in einer Kiste. Liegt eine Zahl drin, weiß jeder: Hier kommen Zahlen rein. Ist die Kiste leer, musst du draufschreiben, was hineingehört."
  steps:
    - "`useState(0)` erkennt `number` aus dem Startwert. `setCount(\"a\")` wäre ein Fehler."
    - "`useState(null)` würde nur den Typ `null` ableiten, und `setUser(user)` wäre später verboten."
    - "Mit `useState<User | null>(null)` sagst du: Startet als `null`, darf später ein `User` sein."
    - "Vor der Benutzung musst du darum `null` ausschließen, z.B. mit `if (!user) return ...`."
  mistake: "`useState([])` für eine Liste. Das leere Array wird als `never[]` erkannt, und `setTodos([todo])` schlägt fehl. Richtig ist `useState<Todo[]>([])`."
  when: "Typ ableiten lassen, wenn der Startwert ihn eindeutig zeigt. Explizit bei `null`, leeren Arrays und Unions wie `useState<Status>(\"idle\")`."
  question: "Welchen Typ hat `status` bei `const [status, setStatus] = useState(\"idle\")`?"
  answer: "`string`, nicht `\"idle\"`. Willst du nur bestimmte Werte erlauben, brauchst du `useState<Status>(\"idle\")`."
links:
  - text: "useState typisieren (EN)"
    url: "https://react.dev/learn/typescript#typing-usestate"
  - text: "useState-Referenz (EN)"
    url: "https://react.dev/reference/react/useState"
---
