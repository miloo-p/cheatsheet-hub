D = "https://gsap.com/docs/v3/"
R = "https://gsap.com/resources/"
MDN = "https://developer.mozilla.org/de/docs/"

def C(t, d, k, a, e, l, demo=None, labels=None):
    c = dict(t=t, d=d, k=k.strip("\n"), a=(a.strip("\n") if a else None), e=e, l=l, demo=demo)
    if labels: c["labels"] = labels
    return c

BOX = '<div class="box"></div>'
BOX3 = '<div class="col"><div class="box"></div><div class="box alt"></div><div class="box warn"></div></div>'

SECTIONS = []

SECTIONS.append(("grundlagen", "Grundlagen", "tweens", "Ein Tween animiert Eigenschaften von A nach B. Fast alles in GSAP baut darauf auf.", [
C("Animieren mit `gsap.to()`",
  "Ein Element vom aktuellen Zustand zu neuen Werten animieren.",
  """
gsap.to(".box", {
  x: 220,
  rotation: 360,
  duration: 1,
});
""", """
document.querySelector(".box").animate(
  [
    { transform: "translateX(0) rotate(0deg)" },
    { transform: "translateX(220px) rotate(360deg)" },
  ],
  { duration: 1000, easing: "ease-out", fill: "forwards" }
);
""",
 ("Ein Tween ist wie ein Navi-Auftrag: Du sagst nur, wo es hingehen soll und wie lange die Fahrt dauern darf. Den Weg dazwischen berechnet GSAP Bild für Bild.",
  ["`gsap.to()` nimmt ein Ziel (Selektor, Element oder Array) und ein Objekt mit Zielwerten.",
   "`x` und `rotation` sind GSAP-Kurzformen für Transforms. GSAP setzt daraus den `transform`-String zusammen.",
   "`duration` ist in Sekunden angegeben, nicht in Millisekunden wie bei CSS oder der Web Animations API.",
   "Der Standard-Ease ist `power1.out`: schneller Start, sanftes Ende.",
   "Die Variante ohne GSAP nutzt die Web Animations API (`element.animate`). Dort musst du Start- und Endzustand komplett angeben und mit `fill: \"forwards\"` festhalten."],
  "Die Dauer in Millisekunden angeben: `duration: 1000` dauert bei GSAP über 16 Minuten. Und bei `element.animate` ohne `fill: \"forwards\"` springt das Element nach dem Ende zurück an den Start.",
  "GSAP, sobald mehrere Animationen zusammenspielen, Scrollen beteiligt ist oder du Werte während der Animation ändern willst. Für einen einzelnen Hover-Effekt reicht eine CSS-Transition.",
  "Wie lange dauert `gsap.to(\".box\", { x: 100 })` ohne Angabe von `duration`?",
  "0,5 Sekunden. Das ist die Standarddauer in GSAP."),
 [("gsap.to()", D+"GSAP/gsap.to()"), ("Transforms (CSSPlugin)", D+"GSAP/CorePlugins/CSS"), ("Web Animations API (MDN)", MDN+"Web/API/Web_Animations_API")],
 demo=dict(html=BOX, js='gsap.to(".box", { x: 220, rotation: 360, duration: 1 });', h=90)),

C("`from()` und `fromTo()`",
  "Vom Ziel aus zurück animieren, ideal für Einblend-Effekte. Oder Start und Ende komplett festlegen.",
  """
gsap.from(".card", { y: 40, autoAlpha: 0, duration: 0.6 });

gsap.fromTo(".bar",
  { scaleX: 0 },
  { scaleX: 1, duration: 1, transformOrigin: "left center" }
);
""", """
document.querySelector(".card").animate(
  [
    { transform: "translateY(40px)", opacity: 0, visibility: "hidden" },
    { transform: "translateY(0)", opacity: 1, visibility: "visible" },
  ],
  { duration: 600, easing: "ease-out" }
);

const bar = document.querySelector(".bar");
bar.style.transformOrigin = "left center";
bar.animate([{ transform: "scaleX(0)" }, { transform: "scaleX(1)" }],
  { duration: 1000, fill: "forwards" });
""",
 ("`from()` ist wie ein Film, der rückwärts gedreht und vorwärts abgespielt wird: Das Element steht schon an seinem Platz, GSAP schiebt es kurz weg und lässt es dorthin zurückfliegen.",
  ["`gsap.from()` nimmt die angegebenen Werte als Start und den aktuellen Zustand aus dem CSS als Ziel.",
   "`autoAlpha` ist eine GSAP-Kurzform: Es animiert `opacity` und setzt `visibility: hidden`, sobald der Wert 0 ist. Unsichtbare Elemente sind dann auch nicht mehr klickbar.",
   "`fromTo()` legt Start und Ziel ausdrücklich fest und ist damit unabhängig vom aktuellen Zustand.",
   "`transformOrigin` bestimmt den Fixpunkt für `scale` und `rotation`. Mit `left center` wächst der Balken von links."],
  "Ein `from()` mehrfach hintereinander auslösen, z.B. bei jedem Klick. Startet die zweite Animation, während die erste noch läuft, liest GSAP den halb animierten Zustand als neues Ziel, und das Element bleibt irgendwo in der Mitte hängen. Für wiederholbare Animationen ist `fromTo()` sicher.",
  "`from()` für Einblendungen beim Laden. `fromTo()`, wenn eine Animation mehrfach abgespielt wird oder der Ausgangszustand nicht sicher ist.",
  "Warum flackert ein Element manchmal kurz sichtbar auf, bevor `gsap.from(…, { autoAlpha: 0 })` startet?",
  "Weil das Element schon gerendert wird, bevor das Skript läuft. Abhilfe: im CSS `visibility: hidden` setzen und mit `autoAlpha` einblenden, oder das Skript früher laden."),
 [("gsap.from()", D+"GSAP/gsap.from()"), ("gsap.fromTo()", D+"GSAP/gsap.fromTo()")],
 demo=dict(html='<div class="col"><div class="chip card">Karte erscheint</div><div class="box bar" style="width:100%;height:10px"></div></div>',
           js='gsap.from(".card", { y: 40, autoAlpha: 0, duration: 0.6 });\ngsap.fromTo(".bar", { scaleX: 0 }, { scaleX: 1, duration: 1, transformOrigin: "left center" });', h=100)),

C("Easing",
  "Die Kurve bestimmt, wie sich eine Bewegung anfühlt: träge, federnd, mechanisch oder verspielt.",
  """
gsap.to(".a", { x: 220, ease: "power3.out" });
gsap.to(".b", { x: 220, ease: "back.out(1.7)" });
gsap.to(".c", { x: 220, ease: "elastic.out(1, 0.4)" });
""", """
.a { transition: transform .5s cubic-bezier(0.215, 0.61, 0.355, 1); }
.b { transition: transform .5s cubic-bezier(0.34, 1.56, 0.64, 1); }
/* Elastisch geht nur mit vielen Stützpunkten in linear(): */
.c { transition: transform .5s linear(0, 0.7 10%, 1.15 20%, 0.95 35%, 1.02 50%, 1); }
""",
 ("Easing ist der Fahrstil: Ein Taxi fährt sanft an und bremst sanft (`inOut`), ein Sportwagen zieht los und rollt aus (`out`), ein Flummi springt über das Ziel hinaus und federt zurück (`elastic`).",
  ["`.out` heißt: schnell starten, langsam ankommen. Das passt für fast alles, was ins Bild kommt.",
   "`.in` heißt: langsam starten, schnell enden. Gut für Elemente, die das Bild verlassen.",
   "`.inOut` ist an beiden Enden weich, typisch für Bewegungen von A nach B innerhalb der Seite.",
   "Die Zahl bei `power1` bis `power4` gibt die Stärke an. `back` schießt leicht über das Ziel hinaus, `elastic` schwingt nach.",
   "In CSS gibt es `cubic-bezier()` für einfache Kurven. Federn und Abpraller lassen sich nur mit der neueren Funktion `linear()` und vielen Stützpunkten annähern."],
  "Für alles dasselbe Easing nehmen, meist `linear` oder den Standardwert. Lineare Bewegungen wirken mechanisch, weil sich in der echten Welt nichts ohne Beschleunigung bewegt. `linear` passt nur für Endlosschleifen wie Ladekreisel.",
  "GSAP, wenn du ausdrucksstarke Kurven brauchst oder sie im Ease Visualizer ausprobieren willst. Für einfache Übergänge sind `ease-out` oder ein `cubic-bezier` in CSS völlig ausreichend.",
  "Welches Easing passt zu einem Modal, das den Bildschirm verlässt?",
  "Ein `.in`-Ease wie `power2.in`. Es beschleunigt zum Ende hin, so wirkt das Wegfliegen natürlich."),
 [("Eases und Ease Visualizer", D+"Eases"), ("linear() (MDN)", MDN+"Web/CSS/easing-function/linear")],
 demo=dict(html='<div class="col"><div class="box a"></div><div class="box alt b"></div><div class="box warn c"></div></div>',
           js='gsap.to(".a", { x: 220, ease: "power3.out", duration: 1 });\ngsap.to(".b", { x: 220, ease: "back.out(1.7)", duration: 1 });\ngsap.to(".c", { x: 220, ease: "elastic.out(1, 0.4)", duration: 1.6 });', h=180)),

C("Versetzt starten: `stagger`",
  "Viele Elemente nacheinander statt gleichzeitig animieren, mit einer einzigen Zeile.",
  """
gsap.from(".item", {
  y: 20,
  autoAlpha: 0,
  stagger: 0.1,
});
""", """
document.querySelectorAll(".item").forEach((el, i) => {
  el.animate(
    [
      { transform: "translateY(20px)", opacity: 0 },
      { transform: "translateY(0)", opacity: 1 },
    ],
    { duration: 500, delay: i * 100, easing: "ease-out", fill: "backwards" }
  );
});
""",
 ("`stagger` ist eine La-Ola-Welle im Stadion: Jeder macht dieselbe Bewegung, aber einen Augenblick nach dem Nachbarn.",
  ["`stagger: 0.1` startet jedes Element 0,1 Sekunden nach dem vorherigen.",
   "Die Gesamtdauer wächst mit der Anzahl: Bei 20 Elementen startet das letzte erst nach 1,9 Sekunden.",
   "Als Objekt lässt sich mehr steuern: `stagger: { each: 0.1, from: \"center\" }` startet in der Mitte und läuft nach außen. `amount: 1` verteilt alle Starts auf genau eine Sekunde, egal wie viele Elemente es sind.",
   "Ohne GSAP berechnest du die Verzögerung pro Element selbst aus dem Index."],
  "`each` bei langen Listen verwenden. Bei 100 Einträgen dauert die Animation dann über 10 Sekunden, und Nutzer warten auf Inhalte. Für variable Listen ist `amount` sicherer.",
  "GSAP, sobald du mit `from`, `amount` oder Raster-Staggers arbeiten willst. Für drei feste Elemente geht es auch mit CSS und `animation-delay`.",
  "Wie animierst du ein Raster von innen nach außen?",
  "Mit `stagger: { each: 0.05, grid: \"auto\", from: \"center\" }`. GSAP berechnet die Abstände im Raster selbst."),
 [("Staggers", R+"getting-started/Staggers")],
 demo=dict(html='<div class="row" style="flex-wrap:wrap">' + '<div class="box item"></div>' * 6 + '</div>',
           js='gsap.from(".item", { y: 20, autoAlpha: 0, stagger: 0.1 });', h=90)),

C("Transforms setzen: `gsap.set()`",
  "Werte sofort setzen, ohne Animation. GSAP verwaltet alle Transforms einzeln, sodass sie sich nicht gegenseitig überschreiben.",
  """
gsap.set(".box", { xPercent: -50, rotation: 15 });

// später, nur x ändern – rotation bleibt erhalten
gsap.to(".box", { x: 120 });
""", """
const box = document.querySelector(".box");
box.style.transform = "translateX(-50%) rotate(15deg)";

// später: der komplette String muss neu gebaut werden,
// sonst geht die Drehung verloren
box.style.transform = "translateX(-50%) translateX(120px) rotate(15deg)";
""",
 ("CSS-Transforms sind ein einzelner Satz, den du immer komplett neu schreiben musst. GSAP führt stattdessen eine Liste mit einzelnen Einträgen für Verschiebung, Drehung und Skalierung und baut daraus den Satz.",
  ["`gsap.set()` ist ein Tween mit Dauer 0, also eine sofortige Zuweisung.",
   "GSAP speichert `x`, `y`, `rotation`, `scale` und `xPercent` getrennt pro Element.",
   "Animierst du danach nur `x`, bleiben die anderen Transforms unverändert.",
   "`xPercent: -50` verschiebt um die Hälfte der eigenen Breite und lässt sich mit `x` kombinieren. Das ist praktisch für zentrierte Elemente."],
  "Ein Element per CSS `transform` positionieren und dann mit GSAP animieren. GSAP liest den vorhandenen Transform zwar ein, aber gemischte Quellen führen schnell zu Sprüngen. Am besten setzt du Transforms für animierte Elemente nur noch mit GSAP.",
  "`gsap.set()` für Startzustände vor einer Animation. Für statisches Layout ohne Animation bleibt CSS der richtige Ort.",
  "Was ist der Unterschied zwischen `x: 100` und `left: 100`?",
  "`x` verschiebt per `transform` und läuft flüssig auf der Grafikkarte. `left` verändert das Layout und zwingt den Browser bei jedem Bild zum Neuberechnen. Siehe Karte „Flüssig animieren“."),
 [("gsap.set()", D+"GSAP/gsap.set()"), ("Transforms (CSSPlugin)", D+"GSAP/CorePlugins/CSS")],
 demo=dict(html=BOX, js='gsap.set(".box", { rotation: 15 });\ngsap.to(".box", { x: 120, duration: 0.8, delay: 0.4 });', h=90)),

C("Steuern: `play`, `pause`, `reverse`",
  "Jede Animation ist ein Objekt mit Fernbedienung. Seit Version 3.15 gibt es dazu `easeReverse` für einen natürlichen Rückweg.",
  """
const tween = gsap.to(".menu", {
  x: 220,
  ease: "expo.out",
  easeReverse: true,
  paused: true,
});

openBtn.onclick = () => tween.play();
closeBtn.onclick = () => tween.reverse();
""", """
const anim = document.querySelector(".menu").animate(
  [{ transform: "translateX(0)" }, { transform: "translateX(220px)" }],
  { duration: 1000, easing: "cubic-bezier(0.19, 1, 0.22, 1)", fill: "both" }
);
anim.pause();

openBtn.onclick = () => { anim.playbackRate = 1; anim.play(); };
closeBtn.onclick = () => anim.reverse();
""",
 ("Ein Tween ist eine Videokassette im Rekorder: Du kannst abspielen, anhalten, zurückspulen oder an eine Stelle springen. `easeReverse` sorgt dafür, dass das Zurückspulen nicht wie ein rückwärts laufender Film aussieht.",
  ["`paused: true` erzeugt die Animation, ohne sie zu starten.",
   "`play()`, `pause()`, `reverse()`, `restart()` und `progress(0.5)` steuern sie jederzeit, auch mitten im Lauf.",
   "Beim normalen `reverse()` läuft auch das Easing rückwärts. Aus `expo.out` wird beim Schließen ein träger Start mit hartem Ende.",
   "`easeReverse: true` (neu in GSAP 3.15) verwendet beim Rückweg dieselbe Kurvenform in der passenden Richtung. Mit einem Ease-Namen wie `easeReverse: \"sine.in\"` bekommt der Rückweg ein ganz eigenes Gefühl."],
  "Bei jedem Klick einen neuen Tween erzeugen, statt einen vorhandenen zu steuern. Bei schnellem Klicken laufen dann mehrere Animationen gegeneinander. Ein Tween mit `play()` und `reverse()` lässt sich beliebig unterbrechen.",
  "GSAP für Menüs, Drawer und Modals, die man jederzeit umkehren kann. Die Web Animations API hat ebenfalls `reverse()`, aber kein getrenntes Easing für den Rückweg.",
  "Welche Option hat `easeReverse` ersetzt?",
  "`yoyoEase`. Es funktioniert weiterhin, wird aber intern in `easeReverse` umgewandelt und gilt als veraltet."),
 [("Tween-Methoden", D+"GSAP/Tween"), ("GSAP 3.15: easeReverse", "https://gsap.com/blog/3-15/")],
 demo=dict(html='<div class="col"><div class="box menu"></div><div class="row"><button type="button" class="chip open">Öffnen</button><button type="button" class="chip close">Schließen</button></div></div>',
           js='const tween = gsap.to(".menu", { x: 220, duration: 1, ease: "expo.out", easeReverse: true, paused: true });\nstage.querySelector(".open").onclick = () => tween.play();\nstage.querySelector(".close").onclick = () => tween.reverse();', h=120)),
]))

SECTIONS.append(("timelines", "Timelines", "timeline", "Mehrere Tweens zu einer Abfolge verbinden, die du als Ganzes steuerst.", [
C("Abfolgen mit `gsap.timeline()`",
  "Animationen nacheinander abspielen, ohne Verzögerungen von Hand auszurechnen.",
  """
const tl = gsap.timeline();
tl.to(".a", { x: 220 })
  .to(".b", { x: 220 })
  .to(".c", { x: 220 });
""", """
const opts = { duration: 500, fill: "forwards", easing: "ease-out" };
const move = [{ transform: "translateX(0)" }, { transform: "translateX(220px)" }];

document.querySelector(".a").animate(move, { ...opts, delay: 0 });
document.querySelector(".b").animate(move, { ...opts, delay: 500 });
document.querySelector(".c").animate(move, { ...opts, delay: 1000 });
""",
 ("Eine Timeline ist ein Drehbuch: Szene folgt auf Szene. Willst du eine Szene verlängern, rutschen alle folgenden automatisch nach hinten, ohne dass du jede Uhrzeit neu ausrechnest.",
  ["`gsap.timeline()` erzeugt einen Container für Tweens.",
   "Jedes `.to()` auf der Timeline wird standardmäßig ans Ende angehängt.",
   "Änderst du die Dauer eines Tweens, verschieben sich alle späteren automatisch.",
   "Die ganze Timeline lässt sich wie ein einzelner Tween steuern: `tl.pause()`, `tl.reverse()`, `tl.progress(0.5)`.",
   "Ohne Timeline musst du jede Verzögerung selbst ausrechnen und bei jeder Änderung alle nachfolgenden anpassen."],
  "Abfolgen mit `delay` in einzelnen Tweens bauen. Das funktioniert, bis du die erste Dauer änderst und alle Verzögerungen danach falsch sind. Und `reverse()` geht nur für die ganze Timeline, nicht für lose Tweens.",
  "Eine Timeline, sobald zwei oder mehr Schritte voneinander abhängen. Einzelne `delay`-Werte nur für wirklich unabhängige Animationen.",
  "Wie lange dauert die Timeline im Beispiel ohne Angabe von `duration`?",
  "1,5 Sekunden: drei Tweens mit der Standarddauer von 0,5 Sekunden hintereinander."),
 [("Timeline", D+"GSAP/Timeline"), ("gsap.timeline()", D+"GSAP/gsap.timeline()")],
 demo=dict(html='<div class="col"><div class="box a"></div><div class="box alt b"></div><div class="box warn c"></div></div>',
           js='const tl = gsap.timeline();\ntl.to(".a", { x: 220 }).to(".b", { x: 220 }).to(".c", { x: 220 });', h=180)),

C("Der Positionsparameter",
  "Das dritte Argument bestimmt, wo ein Tween in der Timeline startet: überlappend, gleichzeitig oder mit Pause.",
  """
tl.to(".a", { x: 220, duration: 1 })
  .to(".b", { x: 220 }, "<")        // gleichzeitig mit dem vorigen
  .to(".c", { x: 220 }, "-=0.3")    // 0,3 s vor dem Ende
  .add("ende", "+=0.5")             // Label nach 0,5 s Pause
  .to(".a", { rotation: 90 }, "ende");
""", """
// Startzeiten in Sekunden, von Hand berechnet:
tl.to(".a", { x: 220, duration: 1 }, 0)
  .to(".b", { x: 220 }, 0)            // gleichzeitig mit .a
  .to(".c", { x: 220 }, 0.7)          // Ende bei 1 s, minus 0,3 s
  .to(".a", { rotation: 90 }, 1.7);   // Ende von .c (1,2 s) + 0,5 s Pause
""",
 ("Der Positionsparameter ist wie Regieanweisungen im Drehbuch: „gleichzeitig mit der letzten Szene“, „kurz bevor sie endet“, „nach einer Pause“. Relative Angaben bleiben richtig, auch wenn sich Szenen ändern.",
  ["Ohne Angabe wird ans Ende der Timeline angehängt.",
   "`\"<\"` startet gleichzeitig mit dem Start des vorigen Tweens, `\">\"` an dessen Ende.",
   "`\"-=0.3\"` startet 0,3 Sekunden vor dem Ende der Timeline, also überlappend. `\"+=0.5\"` lässt eine Pause.",
   "Eine Zahl wie `1.2` ist eine absolute Zeit ab Timeline-Beginn.",
   "Labels wie `\"ende\"` sind benannte Sprungmarken. Tweens können dort starten, und `tl.play(\"ende\")` springt direkt hin."],
  "Absolute Zeiten benutzen wie in der rechten Variante. Ändert sich eine einzige Dauer, stimmen alle Zeiten danach nicht mehr und müssen neu gerechnet werden. Relative Angaben wie `\"<\"` und `\"-=0.3\"` passen sich automatisch an.",
  "Relative Positionen für fast alles. Absolute Zahlen nur, wenn ein Tween genau zu einem festen Zeitpunkt starten muss, z.B. synchron zu Audio.",
  "Was bedeutet `\"<0.2\"`?",
  "0,2 Sekunden nach dem Start des vorigen Tweens. So entsteht ein leichter Versatz, ähnlich wie bei `stagger`."),
 [("Positionsparameter", R+"position-parameter")],
 demo=dict(html='<div class="col"><div class="box a"></div><div class="box alt b"></div><div class="box warn c"></div></div>',
           js='const tl = gsap.timeline();\ntl.to(".a", { x: 220, duration: 1 })\n  .to(".b", { x: 220 }, "<")\n  .to(".c", { x: 220 }, "-=0.3")\n  .add("ende", "+=0.5")\n  .to(".a", { rotation: 90 }, "ende");', h=180),
 labels=("Relativ", "Absolut")),

C("`defaults`, `repeat` und `yoyo`",
  "Gemeinsame Einstellungen einmal für die ganze Timeline festlegen und Abläufe wiederholen.",
  """
const tl = gsap.timeline({
  defaults: { duration: 0.6, ease: "power2.inOut" },
  repeat: -1,
  yoyo: true,
  repeatDelay: 0.3,
});
tl.to(".a", { x: 220 }).to(".b", { x: 220 });
""", """
const tl = gsap.timeline({ repeat: -1, yoyo: true, repeatDelay: 0.3 });
tl.to(".a", { x: 220, duration: 0.6, ease: "power2.inOut" })
  .to(".b", { x: 220, duration: 0.6, ease: "power2.inOut" });
""",
 ("`defaults` ist die Hausordnung der Timeline: Was dort steht, gilt für alle Tweens, solange einer nicht ausdrücklich etwas anderes sagt.",
  ["Werte in `defaults` erben alle Tweens der Timeline, z.B. Dauer und Easing.",
   "Ein Tween kann einzelne Werte überschreiben, indem er sie selbst angibt.",
   "`repeat: -1` wiederholt endlos, `repeat: 2` spielt insgesamt dreimal.",
   "`yoyo: true` spielt jede zweite Wiederholung rückwärts, die Bewegung pendelt also hin und her.",
   "`repeatDelay` legt eine Pause zwischen die Wiederholungen."],
  "`repeat: 3` als „dreimal insgesamt“ verstehen. Es heißt „drei Wiederholungen nach dem ersten Durchlauf“, also viermal insgesamt.",
  "`defaults` ab dem zweiten Tween mit gleichen Einstellungen. Das hält Timelines kurz und Änderungen an einer Stelle.",
  "Ein Tween in einer Timeline mit `defaults: { duration: 1 }` hat `duration: 0.2`. Wie lange dauert er?",
  "0,2 Sekunden. Eigene Werte des Tweens haben Vorrang vor den Defaults."),
 [("Timeline (defaults, repeat, yoyo)", D+"GSAP/Timeline")],
 demo=dict(html='<div class="col"><div class="box a"></div><div class="box alt b"></div></div>',
           js='const tl = gsap.timeline({ defaults: { duration: 0.6, ease: "power2.inOut" }, repeat: -1, yoyo: true, repeatDelay: 0.3 });\ntl.to(".a", { x: 220 }).to(".b", { x: 220 });', h=130)),
]))

SC = '<div class="scroller"><div class="spacer">↓ hier scrollen</div><div class="box target"></div><div class="spacer"></div></div>'

SECTIONS.append(("scrolltrigger", "ScrollTrigger", "scroll", "Animationen an die Scrollposition koppeln. Die Demos scrollen in ihrem eigenen Kasten.", [
C("Beim Hineinscrollen abspielen",
  "Eine Animation starten, sobald ein Element in den sichtbaren Bereich kommt.",
  """
gsap.registerPlugin(ScrollTrigger);

gsap.from(".target", {
  x: -100,
  autoAlpha: 0,
  scrollTrigger: {
    trigger: ".target",
    start: "top 80%",
    toggleActions: "play none none reverse",
  },
});
""", """
const target = document.querySelector(".target");

const observer = new IntersectionObserver(([entry]) => {
  target.classList.toggle("visible", entry.isIntersecting);
}, { rootMargin: "0px 0px -20% 0px" });

observer.observe(target);

/* CSS */
.target { opacity: 0; transform: translateX(-100px); transition: .5s; }
.target.visible { opacity: 1; transform: none; }
""",
 ("Ein ScrollTrigger ist eine Lichtschranke im Flur: Wenn das Element eine bestimmte Linie im Fenster überquert, wird die Animation ausgelöst.",
  ["`trigger` ist das Element, dessen Position beobachtet wird.",
   "`start: \"top 80%\"` heißt: wenn die Oberkante des Elements die Linie bei 80% der Fensterhöhe erreicht.",
   "`toggleActions` legt vier Aktionen fest: beim Hineinscrollen, beim Verlassen nach unten, beim Zurückkommen von unten und beim Verlassen nach oben. Hier: abspielen, nichts, nichts, rückwärts.",
   "`markers: true` zeigt die Start- und End-Linien beim Entwickeln an.",
   "Ohne GSAP übernimmt ein `IntersectionObserver` die Lichtschranke, und eine CSS-Transition die Animation."],
  "`markers: true` im fertigen Projekt vergessen. Und: ScrollTrigger in einem eigenen Scroll-Container benutzen, ohne `scroller` anzugeben. Dann beobachtet er das Fenster, und nichts passiert.",
  "Für einfache Einblendungen reicht der `IntersectionObserver` mit CSS völlig. ScrollTrigger lohnt sich, sobald Timelines, `scrub` oder `pin` ins Spiel kommen.",
  "Was bedeutet `start: \"center center\"`?",
  "Die Animation startet, wenn die Mitte des Elements die Mitte des Fensters erreicht."),
 [("ScrollTrigger", D+"Plugins/ScrollTrigger/"), ("IntersectionObserver (MDN)", MDN+"Web/API/Intersection_Observer_API")],
 demo=dict(html=SC, js='const scroller = stage.querySelector(".scroller");\ngsap.from(".target", { x: -100, autoAlpha: 0, scrollTrigger: { trigger: ".target", scroller, start: "top 80%", toggleActions: "play none none reverse", markers: true } });', h=200)),

C("An den Scroll koppeln: `scrub`",
  "Die Animation läuft genau so weit, wie gescrollt wurde, vor und zurück.",
  """
gsap.to(".progress", {
  scaleX: 1,
  ease: "none",
  scrollTrigger: {
    trigger: "article",
    start: "top top",
    end: "bottom bottom",
    scrub: true,
  },
});
""", """
const bar = document.querySelector(".progress");
const article = document.querySelector("article");

window.addEventListener("scroll", () => {
  const rect = article.getBoundingClientRect();
  const total = rect.height - window.innerHeight;
  const progress = Math.min(Math.max(-rect.top / total, 0), 1);
  bar.style.transform = `scaleX(${progress})`;
}, { passive: true });
""",
 ("Mit `scrub` wird die Scrollleiste zum Abspielregler eines Videos. Scrollst du ein Stück nach unten, läuft das Video ein Stück weiter. Scrollst du zurück, spult es zurück.",
  ["`scrub: true` verbindet den Fortschritt der Animation direkt mit der Scrollposition zwischen `start` und `end`.",
   "`scrub: 1` glättet die Kopplung: Die Animation braucht eine Sekunde, um zur Scrollposition aufzuholen. Das wirkt weicher.",
   "`ease: \"none\"` ist hier wichtig, sonst läuft die Animation an manchen Scrollstellen schneller als an anderen.",
   "Ohne GSAP rechnest du den Fortschritt im Scroll-Event selbst aus. Modernes CSS kann das auch mit `animation-timeline: scroll()`, das wird aber noch nicht in allen Browsern unterstützt."],
  "Bei `scrub` ein Easing wie `power2.out` stehen lassen. Dann passt der Fortschritt nicht mehr gleichmäßig zum Scrollen, und es fühlt sich an, als würde die Seite haken.",
  "`scrub` für Fortschrittsbalken, Parallax und Scroll-Geschichten. Für einen einfachen Lesefortschritt lohnt sich ein Blick auf CSS Scroll-Driven Animations.",
  "Was ist der Unterschied zwischen `scrub: true` und `scrub: 0.5`?",
  "Bei `true` folgt die Animation exakt und sofort. Bei `0.5` braucht sie eine halbe Sekunde zum Aufholen und wirkt dadurch gedämpft."),
 [("ScrollTrigger: scrub", D+"Plugins/ScrollTrigger/"), ("Scroll-Driven Animations (MDN)", MDN+"Web/CSS/CSS_scroll-driven_animations")],
 demo=dict(html='<div class="scroller"><div class="box progress" style="position:sticky;top:0;width:100%;height:8px;transform:scaleX(0);transform-origin:left;z-index:1"></div><div class="spacer">↓ scrollen</div><div class="spacer">weiter …</div><div class="spacer">fast geschafft</div></div>',
           js='const scroller = stage.querySelector(".scroller");\ngsap.to(".progress", { scaleX: 1, ease: "none", scrollTrigger: { trigger: scroller.firstElementChild.nextElementSibling, scroller, start: "top top", end: () => "+=" + (scroller.scrollHeight - scroller.clientHeight), scrub: true } });', h=200)),

C("Festhalten: `pin`",
  "Ein Element bleibt stehen, während daneben weitergescrollt wird, und läuft danach normal weiter.",
  """
gsap.to(".panel", {
  rotation: 360,
  scrollTrigger: {
    trigger: ".panel",
    start: "top 20%",
    end: "+=300",
    pin: true,
    scrub: true,
  },
});
""", """
/* CSS: Festhalten geht ohne GSAP mit sticky */
.panel-wrap { height: 600px; }       /* Strecke, auf der es klebt */
.panel { position: sticky; top: 20%; }

/* Die Drehung muss JavaScript im Scroll-Event berechnen,
   wie in der Karte zu scrub. */
""",
 ("`pin` ist ein Magnet an der Scheibe: Das Element bleibt an einer Stelle im Fenster haften, während die Seite für eine festgelegte Strecke darunter weiterläuft. Danach löst sich der Magnet.",
  ["`pin: true` hält den Trigger zwischen `start` und `end` fest.",
   "`end: \"+=300\"` heißt: 300 Pixel Scrollstrecke nach dem Start.",
   "ScrollTrigger fügt dafür automatisch Abstand ein (`pinSpacing`), damit der folgende Inhalt nicht darunter verschwindet.",
   "Kombiniert mit `scrub` entsteht das typische Muster „Element bleibt stehen und animiert, während man scrollt“.",
   "Das reine Festhalten kann CSS mit `position: sticky`. Nur die Kopplung an eine Animation braucht JavaScript."],
  "Ein Element pinnen, das selbst animiert wird, und dann das Pin-Element auch per `transform` bewegen. Das kann sich beißen. Besser einen Wrapper pinnen und das innere Element animieren.",
  "`position: sticky`, wenn ein Element nur kleben soll. ScrollTrigger mit `pin`, wenn während des Klebens etwas passiert, z.B. eine Folge von Bildern oder ein horizontales Scrollen.",
  "Wofür ist `pinSpacing: false` gut?",
  "Wenn das nachfolgende Element über das gepinnte Element hinweggleiten soll, z.B. für gestapelte Karten. Ohne Abstand rückt der Inhalt nicht nach unten."),
 [("ScrollTrigger: pin", D+"Plugins/ScrollTrigger/"), ("position: sticky (MDN)", MDN+"Web/CSS/position")],
 demo=dict(html='<div class="scroller"><div class="spacer">↓ scrollen</div><div class="box panel" style="margin-inline:auto"></div><div class="spacer"></div><div class="spacer">Ende</div></div>',
           js='const scroller = stage.querySelector(".scroller");\ngsap.to(".panel", { rotation: 360, scrollTrigger: { trigger: ".panel", scroller, start: "top 30%", end: "+=200", pin: true, scrub: true } });', h=220),
 labels=("Mit GSAP", "Ohne GSAP (nur sticky)")),
]))

SECTIONS.append(("plugins", "Plugins", "plugins", "Seit 2025 sind alle GSAP-Plugins kostenlos, auch für kommerzielle Projekte. Zwei der nützlichsten.", [
C("Layout-Wechsel animieren: Flip",
  "Elemente springen bei einer Layout-Änderung nicht, sondern gleiten an ihre neue Position.",
  """
gsap.registerPlugin(Flip);

const state = Flip.getState(".item");
container.classList.toggle("grid");   // Layout ändern
Flip.from(state, { duration: 0.6, ease: "power2.inOut" });
""", """
const items = [...document.querySelectorAll(".item")];
const first = items.map(el => el.getBoundingClientRect());   // F: First

container.classList.toggle("grid");                           // Layout ändern
items.forEach((el, i) => {
  const last = el.getBoundingClientRect();                    // L: Last
  const dx = first[i].left - last.left;                       // I: Invert
  const dy = first[i].top - last.top;
  el.animate(                                                 // P: Play
    [{ transform: `translate(${dx}px, ${dy}px)` }, { transform: "none" }],
    { duration: 600, easing: "ease-in-out" }
  );
});
""",
 ("Flip ist ein Zaubertrick: Das Element springt sofort an seinen neuen Platz, wird aber optisch an den alten zurückversetzt und gleitet dann sichtbar hinüber. Die Zuschauer sehen nur das Gleiten.",
  ["FLIP steht für First, Last, Invert, Play.",
   "First: `Flip.getState()` merkt sich Position und Größe aller Elemente.",
   "Last: Du änderst das Layout ganz normal, per Klasse, Umsortieren oder Verschieben im DOM.",
   "Invert und Play: `Flip.from()` versetzt die Elemente per Transform an die alte Position und animiert sie zur neuen.",
   "Die ausführliche Variante zeigt genau diese vier Schritte von Hand. Flip kümmert sich zusätzlich um Größenänderungen, verschachtelte Elemente und unterbrochene Animationen."],
  "Den Zustand erst nach der Layout-Änderung erfassen. Dann sind First und Last identisch, und es passiert nichts. `getState()` muss immer vor der Änderung stehen.",
  "Flip für Filter, Sortierungen, Raster-Wechsel und Elemente, die den Container wechseln. Für ein einzelnes Element reicht oft die ausführliche Variante.",
  "Wofür steht das I in FLIP?",
  "Für Invert: Das Element wird per Transform optisch an seine alte Position zurückgesetzt, bevor es animiert wird."),
 [("Flip", D+"Plugins/Flip/")],
 demo=dict(html='<div class="col"><div class="row flipwrap"><div class="box item"></div><div class="box alt item"></div><div class="box warn item"></div><div class="box item" style="opacity:.5"></div></div><button type="button" class="chip shuffle" style="justify-self:start">Mischen</button></div>',
           js='const wrap = stage.querySelector(".flipwrap");\nconst shuffle = () => {\n  const state = Flip.getState(wrap.children);\n  [...wrap.children].sort(() => Math.random() - 0.5).forEach(el => wrap.appendChild(el));\n  wrap.style.flexDirection = wrap.style.flexDirection === "column" ? "row" : "column";\n  Flip.from(state, { duration: 0.6, ease: "power2.inOut" });\n};\nstage.querySelector(".shuffle").onclick = shuffle;\nshuffle();', h=250)),

C("Text animieren: SplitText",
  "Text in Zeilen, Wörter oder Buchstaben zerlegen und einzeln animieren, barrierefrei.",
  """
gsap.registerPlugin(SplitText);

SplitText.create(".headline", {
  type: "words, chars",
  autoSplit: true,
  onSplit(self) {
    return gsap.from(self.chars, {
      y: 20, autoAlpha: 0, stagger: 0.03,
    });
  },
});
""", """
const el = document.querySelector(".headline");
const text = el.textContent;
el.setAttribute("aria-label", text);
el.innerHTML = [...text].map(ch =>
  `<span aria-hidden="true" style="display:inline-block">${ch === " " ? "&nbsp;" : ch}</span>`
).join("");

el.querySelectorAll("span").forEach((span, i) => {
  span.animate(
    [{ transform: "translateY(20px)", opacity: 0 }, { transform: "none", opacity: 1 }],
    { duration: 500, delay: i * 30, fill: "backwards" }
  );
});
""",
 ("SplitText ist ein Setzkasten: Der Satz wird in einzelne Lettern zerlegt, damit jede für sich tanzen kann. Für Screenreader bleibt trotzdem der ganze Satz lesbar.",
  ["`type` legt fest, was zerlegt wird: `chars`, `words`, `lines` oder eine Kombination.",
   "Jedes Teil steckt danach in einem eigenen Element und ist über `self.chars`, `self.words` oder `self.lines` erreichbar.",
   "SplitText setzt automatisch `aria-label` auf das Original und blendet die Einzelteile für Screenreader aus.",
   "`autoSplit` zerlegt neu, wenn Schriften nachladen oder sich die Breite ändert. Dann verschieben sich nämlich Zeilenumbrüche. Die Animation aus `onSplit` wird dabei mitgeführt.",
   "Die ausführliche Variante zeigt das Prinzip mit Buchstaben. Zeilen korrekt zu erkennen ist von Hand deutlich schwieriger."],
  "Text nach `lines` zerlegen, bevor die Webfont geladen ist. Dann stimmen die Zeilen nicht mehr, sobald die Schrift erscheint. `autoSplit: true` oder `document.fonts.ready` abwarten löst das.",
  "SplitText für Überschriften und kurze Texte. Lange Fließtexte Buchstabe für Buchstabe zu animieren ist schwer lesbar und belastet die Leistung.",
  "Was macht `split.revert()`?",
  "Es stellt das ursprüngliche HTML wieder her und entfernt alle erzeugten Elemente. Wichtig beim Aufräumen, z.B. in React."),
 [("SplitText", D+"Plugins/SplitText/"), ("GSAP-Lizenz", "https://gsap.com/licensing/")],
 demo=dict(html='<p class="headline" style="font-family:var(--font-display);font-size:26px;font-weight:800;margin:0">Hallo Bootcamp!</p>',
           js='SplitText.create(".headline", { type: "words, chars", onSplit(self) { return gsap.from(self.chars, { y: 20, autoAlpha: 0, stagger: 0.03 }); } });', h=90)),
]))

SECTIONS.append(("praxis", "Praxis: React, Performance, Barrierefreiheit", "praxis", "Damit Animationen im echten Projekt flüssig laufen, aufräumen und niemanden stören.", [
C("GSAP in React: `useGSAP`",
  "Der offizielle Hook räumt Animationen automatisch auf und begrenzt Selektoren auf deine Komponente.",
  """
import { useRef } from "react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";
gsap.registerPlugin(useGSAP);

function Hero() {
  const container = useRef(null);
  useGSAP(() => {
    gsap.from(".title", { y: 40, autoAlpha: 0 });
  }, { scope: container });

  return <section ref={container}><h1 className="title">Hallo</h1></section>;
}
""", """
import { useRef, useLayoutEffect } from "react";
import gsap from "gsap";

function Hero() {
  const container = useRef(null);
  useLayoutEffect(() => {
    const ctx = gsap.context(() => {
      gsap.from(".title", { y: 40, autoAlpha: 0 });
    }, container);
    return () => ctx.revert();   // Aufräumen beim Unmount
  }, []);

  return <section ref={container}><h1 className="title">Hallo</h1></section>;
}
""",
 ("`useGSAP` ist ein Hausmeister für deine Komponente: Er merkt sich jede Animation, die darin entsteht, und räumt sie weg, sobald die Komponente verschwindet.",
  ["`scope: container` sorgt dafür, dass `\".title\"` nur innerhalb dieser Komponente gesucht wird, nicht auf der ganzen Seite.",
   "Beim Unmount werden alle Animationen und ScrollTrigger aus dem Hook automatisch zurückgesetzt.",
   "Im Strict Mode führt React Effekte in der Entwicklung doppelt aus. Ohne Aufräumen laufen dann zwei Animationen gleichzeitig. `useGSAP` verhindert das.",
   "Animationen, die später entstehen, z.B. in einem `onClick`, wickelst du in `contextSafe()`, damit auch sie aufgeräumt werden.",
   "Die ausführliche Variante zeigt, was der Hook intern tut: `gsap.context()` plus `revert()` im Cleanup."],
  "GSAP in einem normalen `useEffect` ohne Aufräumen benutzen. Im Strict Mode verdoppeln sich dann `from()`-Animationen, und Elemente bleiben unsichtbar, weil die zweite Animation den halb animierten Zustand als Ziel nimmt.",
  "`useGSAP` in jedem React-Projekt mit GSAP. Die manuelle Variante nur, wenn du das Paket `@gsap/react` nicht installieren kannst.",
  "Eine Animation soll bei Klick starten. Wie bindest du sie sauber ein?",
  "Mit `const { contextSafe } = useGSAP({ scope: container });` und `const onClick = contextSafe(() => gsap.to(...));`. So wird auch sie beim Unmount aufgeräumt."),
 [("GSAP mit React", R+"React/"), ("gsap.context()", D+"GSAP/gsap.context()")],
 labels=("Mit useGSAP", "Mit useLayoutEffect")),

C("Flüssig animieren: Transforms statt Layout",
  "Manche Eigenschaften kann der Browser billig animieren, andere zwingen ihn bei jedem Bild zum Neuberechnen der Seite.",
  """
gsap.to(".box", {
  x: 200,          // transform: translateX
  scale: 1.2,      // transform: scale
  autoAlpha: 0.5,  // opacity
});
""", """
gsap.to(".box", {
  left: 200,       // Layout: Position neu berechnen
  width: 60,       // Layout: Größe neu berechnen
  marginTop: 20,   // Layout: alles darunter verschiebt sich
});
""",
 ("Transforms sind wie das Verschieben eines Fotos auf einem Leuchttisch. `left` und `width` sind, als würdest du für jedes Einzelbild die ganze Seite neu setzen und drucken.",
  ["Jedes Bild durchläuft Layout (Positionen berechnen), Paint (Pixel malen) und Composite (Ebenen zusammensetzen).",
   "`transform` und `opacity` brauchen nur den letzten, günstigen Schritt. Die Grafikkarte erledigt das.",
   "`left`, `top`, `width`, `height` und `margin` lösen bei jedem Bild ein neues Layout aus, oft für die halbe Seite.",
   "Bei 60 Bildern pro Sekunde bleiben pro Bild etwa 16 Millisekunden. Layout-Animationen sprengen das schnell, besonders auf Handys."],
  "`width` und `height` animieren, um etwas wachsen zu lassen. `scale` wirkt meist gleich und bleibt flüssig. Wenn sich die Größe wirklich ändern muss, z.B. weil Text umbrechen soll, ist Flip die bessere Wahl.",
  "Immer zuerst `x`, `y`, `scale`, `rotation` und `autoAlpha`. Layout-Eigenschaften nur, wenn es nicht anders geht, und dann bei kleinen Elementen.",
  "Wie prüfst du, ob eine Animation ruckelt?",
  "In den Chrome-Entwicklertools unter „Performance“ aufzeichnen und nach langen Frames und lila Layout-Balken suchen. Oder unter „Rendering“ die Option „Frame Rendering Stats“ einschalten."),
 [("Rendering-Performance (web.dev, EN)", "https://web.dev/articles/rendering-performance")],
 demo=dict(html='<div class="col"><div class="box good"></div><div class="box warn bad" style="position:relative;left:0"></div><span class="note">oben: transform · unten: left/width</span></div>',
           js='gsap.to(".good", { x: 200, scale: 1.2, duration: 1, repeat: 1, yoyo: true });\ngsap.to(".bad", { left: 200, width: 60, duration: 1, repeat: 1, yoyo: true });', h=150),
 labels=("Flüssig", "Ruckelanfällig")),

C("Weniger Bewegung respektieren: `matchMedia`",
  "Animationen an Bildschirmgröße und Systemeinstellungen anpassen und beim Wechsel automatisch aufräumen.",
  """
const mm = gsap.matchMedia();

mm.add({
  isDesktop: "(min-width: 800px)",
  reduceMotion: "(prefers-reduced-motion: reduce)",
}, (context) => {
  const { isDesktop, reduceMotion } = context.conditions;
  gsap.from(".hero", {
    y: reduceMotion ? 0 : (isDesktop ? 80 : 30),
    autoAlpha: 0,
    duration: reduceMotion ? 0.2 : 1,
  });
});
""", """
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
const desktop = window.matchMedia("(min-width: 800px)");
let tween;

function setup() {
  if (tween) tween.revert();   // alte Animation entfernen
  tween = gsap.from(".hero", {
    y: reduce.matches ? 0 : (desktop.matches ? 80 : 30),
    autoAlpha: 0,
    duration: reduce.matches ? 0.2 : 1,
  });
}
reduce.addEventListener("change", setup);
desktop.addEventListener("change", setup);
setup();
""",
 ("`gsap.matchMedia()` ist ein Thermostat mit Fühlern: Es merkt, wenn sich Bildschirmbreite oder Systemeinstellung ändern, baut die alten Animationen ab und die passenden neu auf.",
  ["`mm.add()` bekommt Bedingungen als Media Queries und eine Funktion mit den Animationen.",
   "In `context.conditions` steht für jede Bedingung `true` oder `false`.",
   "Ändert sich eine Bedingung, werden alle Animationen und ScrollTrigger aus der Funktion zurückgesetzt und die Funktion läuft neu.",
   "`prefers-reduced-motion` ist eine Systemeinstellung für Menschen, denen Bewegung Schwindel oder Übelkeit verursacht. Respektieren heißt nicht unbedingt „gar keine Animation“, sondern: keine großen Bewegungen, eher kurze Überblendungen."],
  "Bei reduzierter Bewegung einfach alles abschalten, auch Animationen, die Zustände erklären. Ein kurzes Einblenden ist meist in Ordnung, große Sprünge, Parallax und Zoom-Effekte nicht.",
  "`gsap.matchMedia()` immer dann, wenn Animationen je nach Gerät oder Einstellung anders sein sollen. Es erspart dir das komplette Aufräumen von Hand.",
  "Wie testest du `prefers-reduced-motion`, ohne die Systemeinstellung zu ändern?",
  "In den Chrome-Entwicklertools unter „Rendering“ bei „Emulate CSS media feature prefers-reduced-motion“ den Wert `reduce` wählen."),
 [("gsap.matchMedia()", D+"GSAP/gsap.matchMedia()"), ("prefers-reduced-motion (MDN)", MDN+"Web/CSS/@media/prefers-reduced-motion")],
 labels=("Mit matchMedia", "Von Hand")),
]))
