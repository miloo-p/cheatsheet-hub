---
title: "Abstände mit `gap`, Push mit `auto`"
description: "Abstände zwischen Elementen mit `gap` statt Margins an jedem Kind. Ein `auto`-Margin schiebt Elemente an den Rand."
code:
  short: |-
    .nav {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .nav .logout { margin-left: auto; }
  long: |-
    .nav {
      display: flex;
      align-items: center;
    }
    .nav > * {
      margin-right: 1rem;
    }
    .nav > *:last-child {
      margin-right: 0;
    }
    .nav .logout {
      margin-left: auto;
    }
explain:
  picture: "`gap` ist wie die Fugen zwischen Fliesen: Sie liegen nur zwischen den Fliesen, nie am Rand. Margins kleben dagegen an jeder einzelnen Fliese."
  steps:
    - "`gap` setzt den Abstand nur zwischen die Flex-Items, nicht davor oder dahinter."
    - "Mit Margins bekommt auch das letzte Element einen Abstand, den du extra wieder entfernen musst."
    - "`margin-left: auto` auf einem Flex-Item nimmt allen freien Platz links davon ein."
    - "Dadurch rutscht der Logout-Button ganz nach rechts, die anderen Links bleiben links."
  mistake: "Bei umbrechenden Zeilen mit Margins arbeiten. Dann landen die Abstände am Zeilenende an der falschen Stelle. `gap` funktioniert auch über mehrere Zeilen korrekt, horizontal wie vertikal."
  when: "`gap` immer in Flexbox und Grid. Margins nur noch, wenn ein einzelnes Element einen besonderen Abstand braucht."
  question: "Was macht `gap: 1rem 2rem`?"
  answer: "1rem Abstand zwischen den Zeilen und 2rem zwischen den Spalten. Es ist die Kurzform für `row-gap` und `column-gap`."
links:
  - text: "gap"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/gap"
  - text: "Ausrichtung in Flexbox"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_flexible_box_layout/Aligning_items_in_a_flex_container"
---
