---
title: "Default- und Rest-Parameter"
description: "Standardwerte direkt in der Signatur, beliebig viele Argumente mit `...` als Array einsammeln."
code:
  short: |-
    const greet = (name = "Gast") => `Hi ${name}`;

    const sum = (...nums) => nums.reduce((a, b) => a + b, 0);
    sum(1, 2, 3); // 6
  long: |-
    function greet(name) {
      if (name === undefined) {
        name = "Gast";
      }
      return "Hi " + name;
    }

    function sum(...nums) {
      let total = 0;
      for (const n of nums) {
        total = total + n;
      }
      return total;
    }
explain:
  picture: "Ein Default-Parameter ist ein Ersatz für den Fall, dass der Aufrufer nichts mitbringt. Ein Rest-Parameter ist ein Sammelkorb, der alle übrigen Argumente in ein Array packt."
  steps:
    - "`name = \"Gast\"` greift nur, wenn das Argument `undefined` ist, also weggelassen wurde."
    - "`...nums` sammelt alle übergebenen Argumente in ein echtes Array namens `nums`."
    - "Darauf funktionieren alle Array-Werkzeuge, z.B. `reduce` oder `for...of`."
  mistake: "Der Default greift nicht bei `null`: `greet(null)` ergibt `Hi null`. Und der Rest-Parameter muss immer der letzte sein, `(...a, b)` ist ein Syntaxfehler."
  when: "Defaults gehören in die Signatur, dann sieht man beim Lesen sofort, was optional ist. Die Prüfung im Funktionskörper brauchst du nur für kompliziertere Regeln."
  question: "Was ergibt `greet(\"\")`, wenn der Default `\"Gast\"` ist?"
  answer: "`Hi ` mit leerem Namen. Ein leerer String ist nicht `undefined`, also greift der Default nicht."
links:
  - text: "Default-Parameter"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Functions/Default_parameters"
  - text: "Rest-Parameter"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Functions/rest_parameters"
---
