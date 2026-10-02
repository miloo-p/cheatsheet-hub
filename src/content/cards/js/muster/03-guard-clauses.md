---
title: "Guard Clauses"
description: "Hier ist es umgekehrt: Die kurze Variante mit frühen `return`s ist die empfohlene, die verschachtelte ist schwerer zu lesen."
code:
  short: |-
    function checkout(cart, user) {
      if (!user) return redirect("/login");
      if (!cart.length) return showError("Korb leer");

      placeOrder(cart, user);
    }
  long: |-
    function checkout(cart, user) {
      if (user) {
        if (cart.length > 0) {
          placeOrder(cart, user);
        } else {
          showError("Korb leer");
        }
      } else {
        redirect("/login");
      }
    }
explain:
  picture: "Ein Türsteher prüft am Eingang: Wer kein Ticket hat, wird sofort abgewiesen. Wer durchkommt, ist garantiert berechtigt, drinnen muss niemand mehr kontrollieren."
  steps:
    - "Jede Bedingung prüft einen Fehlerfall und beendet die Funktion sofort mit `return`."
    - "Nach allen Guards steht fest, dass alle Voraussetzungen erfüllt sind."
    - "Der eigentliche Zweck der Funktion, der Happy Path, steht ganz unten und ohne Einrückung."
    - "Die verschachtelte Variante macht dasselbe, aber Bedingung und Fehlerbehandlung liegen weit auseinander."
  mistake: "Das `return` vergessen: Dann wird zwar der Fehler gezeigt, aber der Code läuft weiter und bestellt trotzdem. Im Backend ist es derselbe Klassiker: `res.status(400).json(...)` ohne `return` führt zu „Cannot set headers after they are sent“."
  when: "Guard Clauses sind hier die empfohlene Variante. Faustregel: Ab mehr als zwei Ebenen Einrückung prüfen, ob sich Bedingungen umdrehen und früh beenden lassen."
  question: "Wo begegnen dir Guard Clauses im Backend ständig?"
  answer: "In Express-Routen und Middleware: `if (!req.user) return res.status(401)...`, `if (!item) return res.status(404)...` und erst danach die eigentliche Logik."
links:
  - text: "return"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/return"
  - text: "if...else"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/if...else"
---
