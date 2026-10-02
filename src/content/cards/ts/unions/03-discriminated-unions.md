---
title: "Discriminated Unions"
description: "Jede Variante hat ein gemeinsames Feld mit festem Wert. Daran erkennt TypeScript, welche Variante vorliegt."
code:
  short: |-
    type State =
      | { status: "loading" }
      | { status: "error"; message: string }
      | { status: "success"; data: Todo[] };

    function render(state: State): string {
      switch (state.status) {
        case "loading": return "Lädt …";
        case "error":   return state.message;
        case "success": return `${state.data.length} Todos`;
      }
    }
  long: |-
    interface LoadingState { status: "loading"; }
    interface ErrorState   { status: "error"; message: string; }
    interface SuccessState { status: "success"; data: Todo[]; }

    type State = LoadingState | ErrorState | SuccessState;

    function render(state: State): string {
      if (state.status === "loading") {
        return "Lädt …";
      }
      if (state.status === "error") {
        return state.message;
      }
      return state.data.length + " Todos";
    }
explain:
  picture: "Wie Pakete mit farbigem Etikett: Rot heißt Fehler, und nur rote Pakete enthalten eine Fehlermeldung. Wer das Etikett liest, weiß genau, was drin ist."
  steps:
    - "Jede Variante hat das Feld `status` mit einem anderen festen Wert. Das ist der Diskriminator."
    - "Prüfst du `state.status === \"error\"`, schließt TypeScript alle anderen Varianten aus."
    - "Im Error-Zweig ist `state.message` deshalb erlaubt, im Loading-Zweig nicht."
    - "Widersprüchliche Zustände wie „lädt, hat aber schon Daten“ lassen sich gar nicht erst bauen."
  mistake: "Den Zustand als ein Objekt mit lauter optionalen Feldern modellieren: `{ loading: boolean; error?: string; data?: Todo[] }`. Dann sind widersprüchliche Kombinationen möglich, und du musst überall `?.` schreiben."
  when: "Die Kurzform für überschaubare Varianten. Einzelne Interfaces, wenn die Varianten groß sind oder einzeln wiederverwendet werden."
  question: "Was passiert, wenn du im `switch` den Fall `\"success\"` vergisst und die Funktion den Rückgabetyp `string` hat?"
  answer: "TypeScript meldet, dass die Funktion nicht in allen Fällen einen `string` zurückgibt. So findest du vergessene Varianten automatisch."
links:
  - text: "Discriminated Unions"
    url: "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions"
  - text: "Exhaustiveness Checking"
    url: "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#exhaustiveness-checking"
---
