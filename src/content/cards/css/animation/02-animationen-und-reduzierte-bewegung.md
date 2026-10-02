---
title: "Animationen und reduzierte Bewegung"
description: "Mehrstufige Animationen mit `@keyframes`, abgeschaltet für alle, die im System weniger Bewegung eingestellt haben."
code:
  short: |-
    @keyframes fade-in {
      from { opacity: 0; transform: translateY(8px); }
    }

    .toast { animation: fade-in 300ms ease-out both; }

    @media (prefers-reduced-motion: reduce) {
      .toast { animation: none; }
    }
  long: |-
    @keyframes fade-in {
      from { opacity: 0; transform: translateY(8px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    .toast {
      animation-name: fade-in;
      animation-duration: 300ms;
      animation-timing-function: ease-out;
      animation-fill-mode: both;
    }

    @media (prefers-reduced-motion: reduce) {
      .toast {
        animation: none;
      }
    }
preview:
  height: 200
  replay: true
  html: |-
    <div class="toast">Gespeichert</div>
    <div class="toast" style="animation-delay: .4s">Neue Nachricht</div>
    <div class="toast" style="animation-delay: .8s">Upload fertig</div>
    <p class="hint">Mit „Bewegung reduzieren“ im System erscheinen die Hinweise ohne Animation.</p>
  css: |-
    @keyframes fade-in {
      from { opacity: 0; transform: translateY(8px); }
    }

    .toast { animation: fade-in 300ms ease-out both; }

    @media (prefers-reduced-motion: reduce) {
      .toast { animation: none; }
    }

    .toast { background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--brand);
             border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; max-width: 260px; box-shadow: 0 4px 12px rgb(0 0 0 / .1); }
explain:
  picture: "`@keyframes` ist ein Daumenkino: Du zeichnest Anfangs- und Endbild, und der Browser malt die Bilder dazwischen."
  steps:
    - "`@keyframes fade-in` definiert eine Animation mit Namen. `from` ist der Start, `to` das Ende."
    - "Fehlt `to`, nimmt der Browser den normalen Zustand des Elements als Ende. Darum reicht in der Kurzform `from`."
    - "`animation` verbindet Element und Keyframes: Name, Dauer, Kurve und Füllmodus."
    - "`both` sorgt dafür, dass der Startzustand schon vor Beginn gilt und der Endzustand danach erhalten bleibt."
    - "`prefers-reduced-motion` erkennt, ob jemand im Betriebssystem weniger Bewegung eingestellt hat, z.B. wegen Schwindel."
  mistake: "Den Namen der Animation falsch schreiben. Es gibt keine Fehlermeldung, die Animation läuft einfach nicht. Und `prefers-reduced-motion` vergessen: Große Bewegungen können bei manchen Menschen Übelkeit auslösen."
  when: "`transition` für Wechsel zwischen zwei Zuständen. `@keyframes` für alles, was von selbst startet, sich wiederholt oder mehr als zwei Stufen hat."
  question: "Wie lässt du eine Animation endlos laufen?"
  answer: "Mit `infinite` in der Kurzform, z.B. `animation: spin 1s linear infinite;`, oder mit `animation-iteration-count: infinite`."
links:
  - text: "animation"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/animation"
  - text: "@keyframes"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/@keyframes"
  - text: "prefers-reduced-motion"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/@media/prefers-reduced-motion"
  - text: "CSS-Animationen verwenden"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_animations/Using_CSS_animations"
---
