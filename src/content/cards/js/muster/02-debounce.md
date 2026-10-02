---
title: "Debounce"
description: "Funktion erst ausführen, wenn eine Weile Ruhe ist, z.B. bei einem Suchfeld. Nutzt eine Closure für `timer`."
code:
  short: |-
    const debounce = (fn, delay = 300) => {
      let timer;
      return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), delay);
      };
    };
  long: |-
    function debounce(fn, delay) {
      if (delay === undefined) {
        delay = 300;
      }
      let timer = null;

      function debounced(value) {
        clearTimeout(timer);
        timer = setTimeout(function () {
          fn(value);
        }, delay);
      }

      return debounced;
    }
explain:
  picture: "Wie ein Aufzug, der wartet, bis keiner mehr einsteigt: Jede neue Person setzt den Türtimer zurück. Erst wenn kurz Ruhe ist, fährt er los."
  steps:
    - "`debounce` gibt eine neue Funktion zurück, die sich `timer` per Closure merkt."
    - "Bei jedem Tastendruck wird der alte Timer mit `clearTimeout` gelöscht."
    - "Dann startet ein neuer Timer."
    - "Nur wenn innerhalb von `delay` Millisekunden kein neuer Tastendruck kommt, läuft der Timer ab und `fn` wird ausgeführt."
    - "Ergebnis: Wer „berlin“ tippt, löst einen Request aus statt sechs."
  mistake: "In React die Debounce-Funktion bei jedem Render neu erzeugen. Dann hat jede Version ihren eigenen `timer`, und nichts wird abgebrochen. Lösung: mit `useMemo` oder `useRef` stabil halten oder einen fertigen Hook nutzen."
  when: "Die ausführliche Version reicht nur ein Argument durch. Die kurze reicht mit `...args` beliebig viele durch und ist dadurch universeller."
  question: "Was ist der Unterschied zwischen Debounce und Throttle?"
  answer: "Debounce wartet auf Ruhe und feuert einmal am Ende. Throttle feuert höchstens einmal pro Zeitintervall, auch wenn ununterbrochen Events kommen, z.B. beim Scrollen."
links:
  - text: "Debounce"
    url: "https://developer.mozilla.org/de/docs/Glossary/Debounce"
  - text: "Throttle"
    url: "https://developer.mozilla.org/de/docs/Glossary/Throttle"
  - text: "setTimeout()"
    url: "https://developer.mozilla.org/de/docs/Web/API/Window/setTimeout"
---
