---
title: "Optionale Parameter und Defaults"
description: "Ein `?` macht einen Parameter optional. Ein Default-Wert macht ihn ebenfalls optional und legt gleich den Typ fest."
code:
  short: |-
    function greet(name?: string) {
      return `Hi ${name ?? "Gast"}`;
    }

    function paginate(page = 1, size = 20) { ... }
  long: |-
    function greet(name: string | undefined): string {
      if (name === undefined) {
        return "Hi Gast";
      }
      return "Hi " + name;
    }

    function paginate(page: number = 1, size: number = 20): void { ... }
explain:
  picture: "Ein optionaler Parameter ist ein Feld mit dem Vermerk „darf leer bleiben“. Ein Default-Parameter ist ein vorausgefülltes Feld."
  steps:
    - "`name?: string` heißt: Der Parameter darf fehlen, sein Typ ist dann `string | undefined`."
    - "Darum musst du vor der Verwendung mit `??` oder `if` den `undefined`-Fall behandeln."
    - "`page = 1` macht den Parameter optional und leitet den Typ `number` aus dem Default ab."
    - "Achtung bei der ausführlichen Variante: `name: string | undefined` ist nicht optional. Der Aufrufer muss `greet(undefined)` schreiben, `greet()` ist dort ein Fehler."
  mistake: "Optionale Parameter vor Pflichtparameter setzen: `(a?: string, b: number)` ist ein Fehler. Optionale Parameter müssen hinten stehen."
  when: "`?` für Werte, die wirklich fehlen dürfen. Default-Werte, wenn es einen sinnvollen Standard gibt, denn dann musst du im Funktionskörper nichts mehr prüfen."
  question: "Was ist beim Aufruf der Unterschied zwischen `(x?: number)` und `(x: number | undefined)`?"
  answer: "Beim ersten darfst du `f()` schreiben. Beim zweiten musst du `f(undefined)` übergeben, weil der Parameter Pflicht ist."
links:
  - text: "Optionale Parameter"
    url: "https://www.typescriptlang.org/docs/handbook/2/functions.html#optional-parameters"
---
