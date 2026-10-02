---
title: "Menüs und Hinweise: `popover`"
description: "Menüs, Tooltips und Hinweise, die über allem schweben und sich von selbst wieder schließen."
code:
  short: |-
    <button popovertarget="user-menu">Konto</button>

    <div id="user-menu" popover>
      <a href="/profil">Profil</a>
      <a href="/logout">Abmelden</a>
    </div>
  long: |-
    <button id="menu-btn" aria-expanded="false" aria-controls="user-menu">Konto</button>
    <div id="user-menu" class="dropdown" hidden>...</div>

    <script>
      const btn = document.getElementById("menu-btn");
      const menu = document.getElementById("user-menu");
      btn.addEventListener("click", () => {
        menu.hidden = !menu.hidden;
        btn.setAttribute("aria-expanded", String(!menu.hidden));
      });
      document.addEventListener("click", e => {
        if (!menu.contains(e.target) && e.target !== btn) menu.hidden = true;
      });
      document.addEventListener("keydown", e => {
        if (e.key === "Escape") menu.hidden = true;
      });
    </script>
explain:
  picture: "Ein Popover ist ein Klebezettel, der kurz über der Seite erscheint. Ein Klick daneben oder Escape, und er ist wieder weg, ohne dass du das selbst programmieren musst."
  steps:
    - "Das Attribut `popover` macht ein Element zum Popover. Es ist zunächst unsichtbar."
    - "`popovertarget` am Button verknüpft ihn mit der `id` des Popovers. Ein Klick schaltet es um."
    - "Das Popover erscheint in der obersten Ebene. `z-index` und `overflow` der Elternelemente spielen keine Rolle."
    - "Ein Klick daneben oder Escape schließt es automatisch (Light Dismiss). Die ausführliche Variante baut jeden dieser Punkte einzeln nach."
  mistake: "Ein Popover für etwas benutzen, das den Rest der Seite sperren soll. Popover sind nicht modal. Für „erst entscheiden, dann weiter“ ist `<dialog>` mit `showModal()` richtig."
  when: "Popover für Dropdown-Menüs, Tooltips und Hinweise. Seit 2024 unterstützen alle aktuellen Browser das Attribut."
  question: "Wie verhinderst du, dass sich ein Popover per Klick daneben schließt?"
  answer: "Mit `popover=\"manual\"`. Dann schließt es sich nur über einen Button oder per JavaScript mit `hidePopover()`."
links:
  - text: "popover"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Global_attributes/popover"
  - text: "Popover API"
    url: "https://developer.mozilla.org/de/docs/Web/API/Popover_API"
---
