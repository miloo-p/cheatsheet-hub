---
title: "Seitenstruktur mit Landmarks"
description: "Semantische Elemente beschreiben, welche Rolle ein Bereich hat. Ein `<div>` sagt dazu nichts."
code:
  short: |-
    <header>...</header>
    <nav>...</nav>
    <main>
      <article>...</article>
      <aside>...</aside>
    </main>
    <footer>...</footer>
  long: |-
    <div id="header" role="banner">...</div>
    <div id="nav" role="navigation">...</div>
    <div id="main" role="main">
      <div class="article">...</div>
      <div class="sidebar" role="complementary">...</div>
    </div>
    <div id="footer" role="contentinfo">...</div>
explain:
  picture: "Semantische Elemente sind wie beschriftete Umzugskartons: „Küche“, „Bad“, „Bücher“. Ein `<div>` ist ein Karton ohne Aufschrift. Man kommt auch ans Ziel, muss aber jeden einzelnen öffnen."
  steps:
    - "`<header>`, `<nav>`, `<main>`, `<aside>` und `<footer>` heißen Landmarks. Screenreader können direkt zwischen ihnen springen."
    - "`<main>` gibt es pro Seite nur einmal sichtbar. Dort steht der eigentliche Inhalt."
    - "`<article>` ist ein in sich geschlossener Inhalt, der auch allein Sinn ergibt, z.B. ein Blogpost oder eine Produktkarte."
    - "Die ausführliche Variante erreicht dieselbe Bedeutung mit `role`-Attributen. So machte man es vor HTML5."
  mistake: "Jedes `<div>` durch `<section>` ersetzen. `<section>` ist ein thematischer Abschnitt, der eine Überschrift haben sollte. Für reine Layout-Container bleibt `<div>` richtig."
  when: "Immer die semantischen Elemente. `role` brauchst du nur, wenn es für eine Rolle kein passendes Element gibt."
  question: "Wie oft darf `<header>` auf einer Seite vorkommen?"
  answer: "Mehrfach. Neben dem Seitenkopf kann jedes `<article>` oder `<section>` einen eigenen `<header>` haben. Nur `<main>` ist einmalig."
links:
  - text: "<main>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/main"
  - text: "<header>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/header"
  - text: "<article>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/article"
  - text: "<aside>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/aside"
---
