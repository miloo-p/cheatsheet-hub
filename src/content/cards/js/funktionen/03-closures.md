---
title: "Closures"
description: "Die innere Funktion merkt sich `count` aus der äußeren Funktion, auch nachdem diese längst fertig ist."
code:
  short: |-
    const createCounter = () => {
      let count = 0;
      return () => ++count;
    };
    const next = createCounter();
    next(); // 1
    next(); // 2
  long: |-
    function createCounter() {
      let count = 0;

      function increment() {
        count = count + 1;
        return count;
      }

      return increment;
    }
    const next = createCounter();
    next(); // 1
    next(); // 2
explain:
  picture: "Eine Closure ist ein Rucksack: Wenn eine Funktion entsteht, packt sie die Variablen ihrer Umgebung ein und trägt sie überallhin mit, auch wenn die Umgebung längst verschwunden ist."
  steps:
    - "`createCounter()` legt `count = 0` an und gibt die innere Funktion zurück."
    - "Normalerweise wäre `count` nach dem Ende von `createCounter` weg."
    - "Weil die innere Funktion `count` benutzt, bleibt die Variable in ihrem Rucksack erhalten."
    - "Jeder Aufruf von `next()` greift auf genau dieses `count` zu und erhöht es."
    - "Ein zweites `createCounter()` erzeugt einen neuen, unabhängigen Rucksack mit eigenem `count`."
  mistake: "Zu glauben, `count` sei global oder geteilt. Zwei Counter zählen unabhängig. In React begegnet dir die Kehrseite als Stale Closure: Ein Callback in `useEffect` hat sich einen alten State-Wert gemerkt."
  when: "Beide Varianten sind gleichwertig. Die ausführliche mit benannter innerer Funktion zeigt beim Lernen deutlicher, dass hier eine Funktion zurückgegeben wird."
  question: "Was geben `a()`, `a()`, `b()` aus, wenn `a = createCounter()` und `b = createCounter()`?"
  answer: "1, 2, 1. `b` hat seinen eigenen Rucksack mit eigenem `count`."
links:
  - text: "Closures"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Guide/Closures"
---
