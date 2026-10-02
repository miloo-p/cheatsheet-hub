---
title: "Betonung: `<strong>` und `<em>`"
description: "Bedeutung mit dem passenden Element ausdrücken, Aussehen mit CSS."
code:
  short: "<p><strong>Achtung:</strong> Das Löschen kann <em>nicht</em> rückgängig gemacht werden.</p>"
  long: |-
    <p>
      <span class="bold">Achtung:</span> Das Löschen kann
      <span class="italic">nicht</span> rückgängig gemacht werden.
    </p>

    <style>
      .bold { font-weight: bold; }
      .italic { font-style: italic; }
    </style>
explain:
  picture: "`<strong>` und `<em>` sind wie die Stimme beim Vorlesen: Wichtiges klingt ernster, Betontes wird betont. Ein `<span class=\"bold\">` ist nur dicker gedruckt, und wer vorliest, merkt nichts davon."
  steps:
    - "`<strong>` heißt: Dieser Teil ist wichtig, ernst oder dringend."
    - "`<em>` heißt: Diese Stelle wird betont, und das verändert die Aussage des Satzes."
    - "Browser zeigen beide standardmäßig fett bzw. kursiv, das lässt sich per CSS ändern."
    - "`<b>` und `<i>` gibt es auch. Sie heben hervor, ohne Wichtigkeit zu behaupten, z.B. Fachbegriffe oder fremdsprachige Wörter."
  mistake: "`<strong>` benutzen, nur weil Text fett aussehen soll, z.B. bei allen Labels. Dann ist jedes zweite Wort „besonders wichtig“, und die Auszeichnung verliert ihren Sinn. Für reine Optik ist CSS da."
  when: "`<strong>` und `<em>`, wenn sich Bedeutung oder Betonung ändern. CSS-Klassen, wenn es nur um das Aussehen geht."
  question: "Wie unterscheiden sich „Ich habe das <em>nicht</em> gelöscht“ und „Ich habe <em>das</em> nicht gelöscht“?"
  answer: "Im ersten Satz wird bestritten, dass überhaupt gelöscht wurde. Im zweiten wurde etwas anderes gelöscht. `<em>` trägt also echte Bedeutung."
links:
  - text: "<strong>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/strong"
  - text: "<em>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/em"
  - text: "<b>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/b"
---
