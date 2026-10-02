---
title: "Klassen"
description: "Im React-Frontend selten, im Backend (Services, eigene Fehler) häufig. Felder können direkt in der Klasse stehen statt im `constructor`."
code:
  short: |-
    class User {
      role = "user";
      constructor(name) { this.name = name; }
      get isAdmin() { return this.role === "admin"; }
    }
    const u = new User("Lea");
    u.isAdmin; // false
  long: |-
    class User {
      constructor(name) {
        this.name = name;
        this.role = "user";
      }

      isAdmin() {
        if (this.role === "admin") {
          return true;
        }
        return false;
      }
    }
    const u = new User("Lea");
    u.isAdmin(); // false
explain:
  picture: "Eine Klasse ist ein Bauplan, und `new` baut nach diesem Plan ein konkretes Objekt, eine Instanz. Jede Instanz hat eigene Daten, teilt sich aber die Methoden des Bauplans."
  steps:
    - "`new User(\"Lea\")` legt ein leeres Objekt an und ruft den `constructor` auf."
    - "`this` zeigt im Constructor auf genau dieses neue Objekt. `this.name = name` speichert den Wert darin."
    - "Klassenfelder wie `role = \"user\"` sind eine Kurzform für eine Zuweisung im Constructor."
    - "`get isAdmin()` ist ein Getter: Er wird wie eine Eigenschaft ohne Klammern gelesen, führt aber Code aus."
  mistake: "`new` vergessen: `User(\"Lea\")` wirft einen Fehler. Oder eine Methode als Callback weitergeben, z.B. `button.onclick = u.isAdmin`. Dabei geht `this` verloren."
  when: "Getter sind elegant für berechnete Werte. Eine normale Methode `isAdmin()` ist expliziter und für Einsteiger leichter zu lesen. Im Backend begegnen dir Klassen bei Services, Models und eigenen Error-Typen."
  question: "Wie rufst du `isAdmin` in den beiden Varianten auf?"
  answer: "Beim Getter ohne Klammern (`u.isAdmin`), bei der Methode mit Klammern (`u.isAdmin()`). Lässt du bei der Methode die Klammern weg, bekommst du die Funktion selbst statt des Ergebnisses."
links:
  - text: "Klassen"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Classes"
  - text: "constructor"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Classes/constructor"
  - text: "Getter (get)"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Functions/get"
---
