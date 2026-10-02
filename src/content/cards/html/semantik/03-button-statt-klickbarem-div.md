---
title: "`<button>` statt klickbarem `<div>`"
description: "Ein `<button>` kann von Haus aus alles, was ein Button braucht. Ein klickbares `<div>` muss das mühsam nachbauen."
code:
  short: "<button type=\"button\" onclick=\"toggleMenu()\">Menü</button>"
  long: |-
    <div class="button" role="button" tabindex="0"
         onclick="toggleMenu()"
         onkeydown="if (event.key === 'Enter' || event.key === ' ') toggleMenu()">
      Menü
    </div>
explain:
  picture: "Ein `<button>` ist ein Werkzeug von der Stange: Griff, Klinge und Sicherung sind schon dran. Ein klickbares `<div>` ist ein Stück Holz, an das du jedes Teil selbst schrauben musst."
  steps:
    - "`<button>` ist per Tab erreichbar, reagiert auf Enter und Leertaste und wird von Screenreadern als Schaltfläche angesagt."
    - "Ein `<div>` kann nichts davon. `role=\"button\"` sorgt für die Ansage, `tabindex=\"0\"` für die Erreichbarkeit per Tab."
    - "Die Tastaturbedienung musst du per `onkeydown` selbst nachbauen."
    - "`type=\"button\"` ist wichtig: In einem Formular ist der Standard `submit`, und jeder Klick würde das Formular absenden."
  mistake: "`type=\"button\"` in Formularen vergessen. Ein Button zum Anzeigen des Passworts schickt dann bei jedem Klick das Formular ab."
  when: "Immer `<button>` für Aktionen. Die div-Variante ist ein Beispiel, wie man es nicht machen sollte. Du triffst sie aber in vielen alten Codebasen."
  question: "Wann nimmst du `<button>` und wann `<a>`?"
  answer: "`<a href>` für Navigation zu einer anderen Seite oder Stelle. `<button>` für Aktionen auf der aktuellen Seite: öffnen, speichern, löschen, absenden."
links:
  - text: "<button>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/button"
  - text: "HTML und Barrierefreiheit"
    url: "https://developer.mozilla.org/de/docs/Learn_web_development/Core/Accessibility/HTML"
---
