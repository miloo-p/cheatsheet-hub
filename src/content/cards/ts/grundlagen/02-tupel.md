---
title: "Tupel"
description: "Ein Array mit fester Länge, bei dem jede Position einen eigenen Typ hat. Kennst du von `useState`."
code:
  short: |-
    const point = [10, 20] as const;

    function useToggle() {
      const [on, setOn] = useState(false);
      return [on, () => setOn(!on)] as const;
    }
  long: |-
    const point: readonly [number, number] = [10, 20];

    function useToggle(): [boolean, () => void] {
      const [on, setOn] = useState(false);
      const toggle = (): void => setOn(!on);
      return [on, toggle];
    }
explain:
  picture: "Ein Tupel ist wie ein Formular mit festen Feldern: Feld 1 ist immer der Wert, Feld 2 immer die Funktion. Ein normales Array ist eher ein Stapel, in dem jedes Blatt gleich aussieht."
  steps:
    - "`[10, 20]` allein wird als `number[]` erkannt, also als Liste beliebiger Länge."
    - "`as const` macht daraus ein unveränderliches Tupel mit genau diesen Positionen."
    - "Mit dem Rückgabetyp `[boolean, () => void]` legst du die Positionen ausdrücklich fest."
    - "Beim Auspacken mit `const [on, toggle] = useToggle()` kennt TypeScript dadurch für jede Variable den richtigen Typ."
  mistake: "Ein Paar ohne Tupel-Typ zurückgeben: `return [on, toggle]` wird zu `(boolean | (() => void))[]`. Beim Auspacken ist dann jede Variable „boolean oder Funktion“, und `toggle()` lässt sich nicht aufrufen."
  when: "`as const` ist schnell und praktisch für eigene Hooks. Der explizite Rückgabetyp dokumentiert die Schnittstelle besser und ist bei exportierten Funktionen die sauberere Wahl."
  question: "Welchen Typ hat `const pair = [\"a\", 1]` ohne `as const`?"
  answer: "`(string | number)[]`, also ein Array, in dem jedes Element string oder number sein kann. Die Positionen gehen verloren."
links:
  - text: "Tupel-Typen"
    url: "https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types"
  - text: "const assertions"
    url: "https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions"
---
