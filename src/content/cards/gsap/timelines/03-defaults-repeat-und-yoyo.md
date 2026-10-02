---
title: "`defaults`, `repeat` und `yoyo`"
description: "Gemeinsame Einstellungen einmal für die ganze Timeline festlegen und Abläufe wiederholen."
code:
  short: |-
    const tl = gsap.timeline({
      defaults: { duration: 0.6, ease: "power2.inOut" },
      repeat: -1,
      yoyo: true,
      repeatDelay: 0.3,
    });
    tl.to(".a", { x: 220 }).to(".b", { x: 220 });
  long: |-
    const tl = gsap.timeline({ repeat: -1, yoyo: true, repeatDelay: 0.3 });
    tl.to(".a", { x: 220, duration: 0.6, ease: "power2.inOut" })
      .to(".b", { x: 220, duration: 0.6, ease: "power2.inOut" });
demo:
  height: 130
  html: "<div class=\"col\"><div class=\"box a\"></div><div class=\"box alt b\"></div></div>"
  js: |-
    const tl = gsap.timeline({ defaults: { duration: 0.6, ease: "power2.inOut" }, repeat: -1, yoyo: true, repeatDelay: 0.3 });
    tl.to(".a", { x: 220 }).to(".b", { x: 220 });
explain:
  picture: "`defaults` ist die Hausordnung der Timeline: Was dort steht, gilt für alle Tweens, solange einer nicht ausdrücklich etwas anderes sagt."
  steps:
    - "Werte in `defaults` erben alle Tweens der Timeline, z.B. Dauer und Easing."
    - "Ein Tween kann einzelne Werte überschreiben, indem er sie selbst angibt."
    - "`repeat: -1` wiederholt endlos, `repeat: 2` spielt insgesamt dreimal."
    - "`yoyo: true` spielt jede zweite Wiederholung rückwärts, die Bewegung pendelt also hin und her."
    - "`repeatDelay` legt eine Pause zwischen die Wiederholungen."
  mistake: "`repeat: 3` als „dreimal insgesamt“ verstehen. Es heißt „drei Wiederholungen nach dem ersten Durchlauf“, also viermal insgesamt."
  when: "`defaults` ab dem zweiten Tween mit gleichen Einstellungen. Das hält Timelines kurz und Änderungen an einer Stelle."
  question: "Ein Tween in einer Timeline mit `defaults: { duration: 1 }` hat `duration: 0.2`. Wie lange dauert er?"
  answer: "0,2 Sekunden. Eigene Werte des Tweens haben Vorrang vor den Defaults."
links:
  - text: "Timeline (defaults, repeat, yoyo)"
    url: "https://gsap.com/docs/v3/GSAP/Timeline"
---
