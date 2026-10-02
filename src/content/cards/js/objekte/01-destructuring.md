---
title: "Destructuring"
description: "Werte direkt in Variablen auspacken. Funktioniert bei Objekten `{}`, Arrays `[]` und in Funktionsparametern (React-Props)."
code:
  short: |-
    const { name, age = 18 } = user;
    const { id: userId } = user;
    const [value, setValue] = useState(0);

    function Card({ title, children }) { ... }
  long: |-
    const name = user.name;
    const age = user.age !== undefined ? user.age : 18;
    const userId = user.id;

    const state = useState(0);
    const value = state[0];
    const setValue = state[1];

    function Card(props) {
      const title = props.title;
      const children = props.children;
      ...
    }
explain:
  picture: "Destructuring ist Auspacken nach Etikett: Du sagst, welche Fächer du aus dem Paket willst, und bekommst den Inhalt direkt in gleichnamige Variablen."
  steps:
    - "`{ name, age = 18 } = user` liest `user.name` und `user.age`. Ist `age` `undefined`, gilt 18."
    - "`{ id: userId }` heißt: Nimm das Feld `id`, aber nenne die Variable `userId`."
    - "Bei Arrays zählt die Position, nicht der Name. Deshalb kannst du bei `useState` die Namen frei wählen."
    - "In Parametern wie `({ title })` wird das übergebene Objekt, in React die Props, direkt beim Aufruf ausgepackt."
  mistake: "Destructuring von `undefined` stürzt ab: `const { name } = undefined` wirft einen TypeError, z.B. wenn API-Daten noch nicht geladen sind. Und Objekt- mit Array-Destructuring verwechseln: `const { a, b } = [1, 2]` ergibt zweimal `undefined`."
  when: "In React fast immer Destructuring, weil man die Props sofort sieht. Die ausführliche Form hilft, wenn du nachvollziehen willst, woher ein Wert kommt."
  question: "Welche Variable existiert nach `const { id: userId } = user`: `id` oder `userId`?"
  answer: "Nur `userId`. Links vom Doppelpunkt steht der Feldname im Objekt, rechts der neue Variablenname."
links:
  - text: "Destructuring"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Destructuring"
  - text: "Props an Komponenten übergeben (EN)"
    url: "https://react.dev/learn/passing-props-to-a-component"
---
