M = "https://developer.mozilla.org/de/docs/Web/CSS/"
LEARN = "https://developer.mozilla.org/de/docs/Learn_web_development/Core/Styling_basics/"

def C(t, d, k, a, e, l):
    return dict(t=t, d=d, k=k.strip("\n"), a=a.strip("\n"), e=e, l=l)

SECTIONS = []

SECTIONS.append(("grundlagen", "Grundlagen", "basics", "Box Model, Kurzschreibweisen und Variablen: das Fundament jeder Regel.", [
C("Box Model: `box-sizing`",
  "Mit `border-box` zählen Padding und Rahmen zur angegebenen Breite. Ohne musst du selbst rechnen.",
  """
*, *::before, *::after {
  box-sizing: border-box;
}

.card {
  width: 300px;
  padding: 20px;
  border: 1px solid #ccc;
}
""", """
/* Standard: box-sizing: content-box */
.card {
  width: 258px; /* 300 - 2 × 20 Padding - 2 × 1 Rahmen */
  padding: 20px;
  border: 1px solid #ccc;
}
""",
 ("Stell dir einen Bilderrahmen vor. Bei `content-box` gibst du die Größe des Bildes an, und Passepartout und Rahmen kommen außen dazu. Bei `border-box` gibst du die Außenmaße des ganzen Rahmens an, und das Bild passt sich innen an.",
  ["Jedes Element besteht von innen nach außen aus Inhalt, Padding, Rahmen (border) und Außenabstand (margin).",
   "Standard ist `content-box`: `width` gilt nur für den Inhalt. Padding und Rahmen kommen obendrauf, aus 300px werden 342px.",
   "Mit `border-box` gilt `width` für Inhalt, Padding und Rahmen zusammen. Die Box ist genau 300px breit.",
   "Margin zählt in beiden Fällen nicht zur Breite."],
  "Zwei Spalten mit `width: 50%` und Padding nebeneinandersetzen. Mit `content-box` sind sie zusammen breiter als 100%, und die zweite rutscht in die nächste Zeile.",
  "Die globale `border-box`-Regel gehört an den Anfang fast jedes Stylesheets, die meisten CSS-Resets enthalten sie. Die Rechnung aus der ausführlichen Variante musst du verstehen, aber nicht benutzen.",
  "Wie breit ist `.box { width: 200px; padding: 10px; border: 5px solid; }` mit `content-box`?",
  "230px: 200 Inhalt + 2 × 10 Padding + 2 × 5 Rahmen. Mit `border-box` wären es genau 200px."),
 [("box-sizing", M+"box-sizing"), ("Das Box-Modell", M+"CSS_box_model/Introduction_to_the_CSS_box_model")]),

C("`margin` und `padding` kurz",
  "Ein bis vier Werte statt vier einzelner Eigenschaften. Die Reihenfolge läuft im Uhrzeigersinn.",
  """
.button {
  padding: 8px 16px;
  margin: 0 auto 24px;
}
""", """
.button {
  padding-top: 8px;
  padding-right: 16px;
  padding-bottom: 8px;
  padding-left: 16px;

  margin-top: 0;
  margin-right: auto;
  margin-bottom: 24px;
  margin-left: auto;
}
""",
 ("Die Werte laufen im Uhrzeigersinn, wie ein Zeiger, der oben bei 12 Uhr startet: oben, rechts, unten, links. Merkhilfe: TRBL, ausgesprochen „Trouble“.",
  ["Vier Werte: oben, rechts, unten, links.",
   "Drei Werte: oben, dann links und rechts gemeinsam, dann unten.",
   "Zwei Werte: oben und unten gemeinsam, dann links und rechts gemeinsam.",
   "Ein Wert: alle vier Seiten gleich.",
   "Fehlende Werte übernimmt die gegenüberliegende Seite. Darum gilt bei `0 auto 24px` das `auto` für links und rechts."],
  "Eine Kurzschreibweise nach einer Einzeleigenschaft setzen: Steht `padding: 8px` hinter `padding-left: 32px`, überschreibt es auch die linke Seite wieder mit 8px. Kurzschreibweisen setzen immer alle Teilwerte.",
  "Die Kurzform fast immer. Einzeleigenschaften, wenn du gezielt nur eine Seite ändern willst, z.B. in einem Hover-Zustand oder einer Media Query.",
  "Was bedeutet `margin: 10px 20px 30px`?",
  "Oben 10px, links und rechts 20px, unten 30px."),
 [("margin", M+"margin"), ("padding", M+"padding"), ("Kurzschreibweisen", M+"Shorthand_properties")]),

C("Container zentrieren",
  "Ein Block mit Maximalbreite wird mit automatischem Außenabstand links und rechts mittig gesetzt.",
  """
.container {
  max-width: 70rem;
  margin-inline: auto;
  padding-inline: 1rem;
}
""", """
.container {
  max-width: 70rem;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;
}
""",
 ("Zwei gleich starke Federn links und rechts drücken den Block in die Mitte. `auto` heißt: Nimm dir den restlichen Platz, und beide Seiten teilen ihn gerecht.",
  ["`max-width` begrenzt die Breite. Auf kleinen Bildschirmen wird der Container schmaler, auf großen nie breiter als 70rem.",
   "`margin-left: auto` und `margin-right: auto` verteilen den übrigen Platz gleichmäßig auf beide Seiten.",
   "`margin-inline` ist die logische Kurzform für beide Seiten in Schreibrichtung. In Sprachen, die von rechts nach links laufen, passt sie sich automatisch an.",
   "Das `padding-inline` sorgt dafür, dass der Text auf dem Handy nicht am Rand klebt."],
  "`margin: auto` bei einem Element ohne Breitenbegrenzung benutzen und erwarten, dass es sich zentriert. Ein Block-Element ist standardmäßig so breit wie sein Elternelement, es gibt also keinen Platz zum Verteilen.",
  "`margin-inline` und `padding-inline` sind kürzer und moderner. Die Varianten mit `left` und `right` stehen in älterem Code und funktionieren genauso.",
  "Zentriert `margin-inline: auto` einen Block auch vertikal?",
  "Nein. Im normalen Block-Layout wirkt `auto` nur horizontal. Für vertikales Zentrieren brauchst du Flexbox oder Grid."),
 [("margin-inline", M+"margin-inline"), ("Logische Eigenschaften", M+"CSS_logical_properties_and_values"), ("max-width", M+"max-width")]),

C("Custom Properties",
  "Werte einmal definieren und überall verwenden. Ändern musst du sie dann nur noch an einer Stelle.",
  """
:root {
  --brand: #2b5fae;
  --radius: 8px;
}

.button { background: var(--brand); border-radius: var(--radius); }
.link   { color: var(--brand); }
""", """
.button {
  background: #2b5fae;
  border-radius: 8px;
}

.link {
  color: #2b5fae;
}
""",
 ("Custom Properties sind wie Farbtöpfe mit Etikett. Statt jedes Mal den Farbton neu anzumischen, greifst du zum Topf „brand“. Tauschst du den Inhalt des Topfs, ändert sich die Farbe überall.",
  ["Eigenschaften, die mit `--` beginnen, sind selbst definierte Variablen.",
   "Auf `:root` (dem `<html>`-Element) definiert, gelten sie im ganzen Dokument, weil sie vererbt werden.",
   "`var(--brand)` setzt den Wert ein. Ein zweiter Wert dient als Ersatz: `var(--brand, blue)`.",
   "Variablen lassen sich für Bereiche überschreiben, z.B. `.dark { --brand: #8db4f2; }`. Alles darin nimmt dann automatisch den neuen Wert."],
  "Variablen in der Bedingung einer Media Query benutzen: `@media (width >= var(--bp))` funktioniert nicht. In den Regeln innerhalb der Media Query darfst du sie aber ganz normal verwenden.",
  "Custom Properties für alles, was mehrfach vorkommt: Farben, Abstände, Radien, Schriften. So funktionieren Dark Mode und Themes, auch auf diesen Spickzetteln.",
  "Welche Farbe hat ein `.link` innerhalb von `.dark`, wenn dort `--brand: white` gesetzt ist?",
  "Weiß. Die Variable wird vererbt, und innerhalb von `.dark` gilt der überschriebene Wert."),
 [("Custom Properties verwenden", M+"Using_CSS_custom_properties"), ("var()", M+"var")]),

C("Kurzformen: `border`, `background`, `font`",
  "Mehrere zusammengehörige Eigenschaften in einer Zeile.",
  """
.card {
  border: 1px solid #dde1e8;
  background: #fff url("dots.svg") no-repeat right top;
  font: 600 1rem/1.5 "IBM Plex Sans", sans-serif;
}
""", """
.card {
  border-width: 1px;
  border-style: solid;
  border-color: #dde1e8;

  background-color: #fff;
  background-image: url("dots.svg");
  background-repeat: no-repeat;
  background-position: right top;

  font-weight: 600;
  font-size: 1rem;
  line-height: 1.5;
  font-family: "IBM Plex Sans", sans-serif;
}
""",
 ("Eine Kurzschreibweise ist ein Bestellformular mit Sammelfeld: Du füllst eine Zeile aus, und das System verteilt die Angaben auf die einzelnen Felder.",
  ["`border` braucht Breite, Stil und Farbe. Ohne Stil wie `solid` ist kein Rahmen zu sehen.",
   "Bei `background` ist die Reihenfolge weitgehend frei. Der Browser erkennt an den Werten, was Farbe, Bild oder Position ist.",
   "`font` ist strenger: Schriftgröße und Schriftfamilie sind Pflicht und stehen am Ende, die Zeilenhöhe folgt mit Schrägstrich auf die Größe.",
   "Alles, was du in einer Kurzform weglässt, wird auf den Standardwert zurückgesetzt."],
  "`background: url(...)` schreiben, nachdem vorher `background-color` gesetzt war. Die Kurzform setzt die Farbe dabei auf transparent zurück. Dasselbe passiert bei `font`, das unter anderem die Zeilenhöhe zurücksetzt.",
  "`border` fast immer als Kurzform. Bei `background` und `font` sind Einzeleigenschaften oft sicherer und lesbarer, besonders wenn du nur einen Teil ändern willst.",
  "Warum ist bei `border: 2px red;` kein Rahmen zu sehen?",
  "Der Stil fehlt. Der Standardwert von `border-style` ist `none`, also wird nichts gezeichnet. Richtig ist z.B. `border: 2px solid red;`."),
 [("border", M+"border"), ("background", M+"background"), ("font", M+"font"), ("Kurzschreibweisen", M+"Shorthand_properties")]),

C("Relative Einheiten: `rem` und `em`",
  "`rem` und `em` passen sich an die Schriftgröße an. So wächst das Layout mit, wenn jemand die Schrift im Browser größer stellt.",
  """
.button {
  font-size: 1rem;
  padding: 0.5em 1em;
}
.button.large { font-size: 1.25rem; }
""", """
.button {
  font-size: 16px;
  padding: 8px 16px;
}
.button.large {
  font-size: 20px;
  padding: 10px 20px;
}
""",
 ("`px` ist ein Lineal mit festen Strichen. `rem` und `em` sind wie ein Gummiband, das sich mit der Schriftgröße mitdehnt.",
  ["`rem` bezieht sich auf die Schriftgröße des `<html>`-Elements, standardmäßig 16px. `1rem` ist also 16px.",
   "`em` bezieht sich auf die Schriftgröße des Elements selbst. Beim großen Button ist `1em` deshalb 20px.",
   "Darum wächst das Padding in der kurzen Variante automatisch mit. Die ausführliche Variante muss jeden Wert einzeln anpassen.",
   "Stellt jemand die Standardschrift im Browser auf 20px, wächst bei `rem` und `em` alles mit, bei `px` nicht."],
  "`em` für Schriftgrößen in verschachtelten Elementen benutzen. `font-size: 1.2em` in einer Liste in einer Liste wird mit jeder Ebene größer, weil es sich auf das Elternelement bezieht. Für Schriftgrößen ist `rem` berechenbarer.",
  "`rem` für Schriftgrößen und Layoutabstände, `em` für Abstände, die zur Schrift des Elements passen sollen (Button-Padding, Icons). `px` für Rahmen und feine Details.",
  "Wie groß ist `2rem`, wenn `html { font-size: 20px; }` gesetzt ist?",
  "40px. `rem` bezieht sich immer auf die Schriftgröße des `<html>`-Elements."),
 [("Werte und Einheiten", LEARN+"Values_and_units"), ("length", M+"length")]),
]))

SECTIONS.append(("selektoren", "Selektoren und Zustände", "selectors", "Gezielt die richtigen Elemente treffen, ohne zusätzliche Klassen oder JavaScript.", [
C("Selektoren bündeln: `:is()` und `:where()`",
  "Gemeinsame Teile von Selektoren zusammenfassen, statt sie zu wiederholen.",
  """
.nav :is(a, button):hover {
  color: var(--brand);
}
""", """
.nav a:hover,
.nav button:hover {
  color: var(--brand);
}
""",
 ("`:is()` ist ein Oder-Platzhalter in einer Adresse: „In der Nav, ein Link oder ein Button, im Hover-Zustand.“",
  ["`:is(a, button)` trifft jedes Element, das zu einem der Selektoren in der Klammer passt.",
   "Die kurze und die ausführliche Variante treffen genau dieselben Elemente.",
   "Die Spezifität von `:is()` entspricht dem stärksten Selektor in der Klammer.",
   "`:where()` funktioniert gleich, hat aber immer die Spezifität 0. Seine Regeln lassen sich leicht überschreiben, was für Basis-Styles praktisch ist."],
  "Spezifität unterschätzen: `:is(#main, .content) p` hat die Spezifität einer ID, auch wenn das Element nur über `.content` getroffen wird. Spätere Regeln mit Klassen kommen dagegen nicht mehr an.",
  "`:is()` bei langen, sich wiederholenden Selektorlisten. `:where()` für Basis-Styles, die bewusst schwach sein sollen. Zwei, drei ausgeschriebene Selektoren sind oft genauso lesbar.",
  "Welche Regel gewinnt: `:where(.card) p { color: red }` oder ein späteres `p { color: blue }`?",
  "Blau. `:where()` zählt 0, also haben beide Regeln dieselbe Spezifität wie ein einfacher Element-Selektor, und die spätere gewinnt. Mit `:is()` gewänne Rot, weil die Klasse dann zählt."),
 [(":is()", M+":is"), (":where()", M+":where"), ("Spezifität", M+"Specificity")]),

C("Sichtbarer Fokus: `:focus-visible`",
  "Wer mit der Tastatur navigiert, braucht einen sichtbaren Fokus. `:focus-visible` zeigt ihn nur, wenn er wirklich gebraucht wird.",
  """
.button:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}
""", """
.button:focus {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}
.button:focus:not(:focus-visible) {
  outline: none;
}
""",
 ("Der Fokusring ist der Mauszeiger für Menschen, die mit der Tastatur navigieren. Ohne ihn ist die Seite für sie wie eine Maus ohne Zeiger.",
  ["`:focus` greift immer, wenn ein Element fokussiert ist, auch nach einem Mausklick.",
   "Viele finden den Ring nach einem Klick störend und entfernen ihn komplett. Das schadet allen, die mit der Tastatur arbeiten.",
   "`:focus-visible` greift nur, wenn der Browser einen sichtbaren Fokus für sinnvoll hält, typischerweise bei Navigation mit Tab.",
   "Die ausführliche Variante baut dasselbe Verhalten mit `:focus` und `:not()` nach. So wurde es gemacht, bevor alle Browser `:focus-visible` konnten."],
  "`outline: none` global setzen, ohne Ersatz. Dann sieht niemand mit Tastatur mehr, wo er sich auf der Seite befindet.",
  "Heute einfach `:focus-visible`, alle aktuellen Browser unterstützen es. Die ausführliche Variante brauchst du nur, um älteren Code zu verstehen.",
  "Wie prüfst du schnell, ob deine Seite einen sichtbaren Fokus hat?",
  "Klick in die Adresszeile und drück mehrmals Tab. Bei jedem Schritt muss erkennbar sein, welches Element gerade aktiv ist."),
 [(":focus-visible", M+":focus-visible"), (":focus", M+":focus"), ("outline", M+"outline")]),

C("Pseudo-Elemente: `::before` und `::after`",
  "Dekorative Elemente per CSS erzeugen, ohne zusätzliches HTML.",
  """
<!-- HTML -->
<label class="required">E-Mail</label>

/* CSS */
.required::after {
  content: " *";
  color: crimson;
}
""", """
<!-- HTML -->
<label>E-Mail <span class="star">*</span></label>

/* CSS */
.star {
  color: crimson;
}
""",
 ("Pseudo-Elemente sind unsichtbare Haken am Anfang und am Ende eines Elements. Mit `content` hängst du etwas daran auf.",
  ["`::before` erzeugt ein Kind ganz am Anfang des Inhalts, `::after` ganz am Ende.",
   "Ohne `content` wird gar nichts angezeigt. Für reine Deko-Formen reicht `content: \"\"`.",
   "Pseudo-Elemente sind standardmäßig `inline`. Für Breite und Höhe brauchen sie `display: block` oder `position: absolute`.",
   "Die ausführliche Variante braucht dafür in jedem Label ein zusätzliches `<span>`."],
  "Wichtige Inhalte per `content` einfügen. Screenreader lesen sie nicht zuverlässig vor, und man kann sie nicht markieren. Außerdem funktionieren Pseudo-Elemente nicht auf `<img>` und `<input>`.",
  "Pseudo-Elemente für Deko: Pfeile, Icons, Trennlinien, Pflichtfeld-Sternchen. Echtes HTML für alles, was Bedeutung trägt.",
  "Warum erscheint bei `.box::before { width: 20px; height: 20px; background: red; }` nichts?",
  "Es fehlt `content`. Ohne `content: \"\"` entsteht das Pseudo-Element gar nicht. Außerdem braucht es `display: block` oder `inline-block`, damit Breite und Höhe greifen."),
 [("::before", M+"::before"), ("::after", M+"::after"), ("content", M+"content")]),

C("Elternselektor: `:has()`",
  "Ein Element anhand seines Inhalts stylen. Früher ging das nur mit JavaScript.",
  """
.card:has(img) {
  padding-top: 0;
}
""", """
/* CSS */
.card.has-image {
  padding-top: 0;
}

// JavaScript
document.querySelectorAll(".card").forEach(card => {
  if (card.querySelector("img")) card.classList.add("has-image");
});
""",
 ("`:has()` ist der Elternselektor, auf den CSS jahrzehntelang gewartet hat: Er schaut ins Element hinein und fragt, ob etwas Bestimmtes darin steckt.",
  ["Selektoren gingen bisher nur von oben nach unten, vom Eltern- zum Kindelement.",
   "`.card:has(img)` dreht das um: Gestylt wird die Karte, aber nur, wenn sie ein Bild enthält.",
   "In der Klammer darf ein beliebiger Selektor stehen, auch mit Zuständen. `.field:has(input:invalid)` markiert ein ganzes Formularfeld, sobald die Eingabe ungültig ist.",
   "Die JavaScript-Variante muss nach jeder Änderung erneut laufen. `:has()` reagiert automatisch."],
  "`:has()` mit einem Nachfahren-Selektor verwechseln. `.card img` stylt das Bild, `.card:has(img)` stylt die Karte.",
  "Alle aktuellen Browser unterstützen `:has()`. JavaScript brauchst du dafür nur noch, wenn sehr alte Browser unterstützt werden müssen.",
  "Wie stylst du ein `<form>`, sobald irgendeine Checkbox darin angehakt ist?",
  "Mit `form:has(input[type=\"checkbox\"]:checked) { ... }`."),
 [(":has()", M+":has"), ("Pseudoklassen", M+"Pseudo-classes")]),

C("CSS Nesting",
  "Regeln ineinander schreiben wie in Sass, aber direkt im Browser.",
  """
.card {
  padding: 1rem;

  & h2 { margin: 0; }
  &:hover { border-color: var(--brand); }

  @media (width >= 48rem) {
    padding: 2rem;
  }
}
""", """
.card {
  padding: 1rem;
}
.card h2 {
  margin: 0;
}
.card:hover {
  border-color: var(--brand);
}
@media (width >= 48rem) {
  .card {
    padding: 2rem;
  }
}
""",
 ("Nesting ist wie eine Ordnerstruktur: Alles, was zur Karte gehört, liegt im Ordner `.card` statt verstreut auf dem Schreibtisch.",
  ["Verschachtelte Regeln gelten nur innerhalb des äußeren Selektors.",
   "`&` steht für den äußeren Selektor. `&:hover` wird zu `.card:hover`, `& h2` zu `.card h2`.",
   "Auch Media Queries dürfen verschachtelt werden. Die Regeln darin gelten dann für `.card`.",
   "Der Browser rechnet das intern in die flache Form der ausführlichen Variante um."],
  "Zu tief verschachteln. Fünf Ebenen erzeugen lange, sehr spezifische Selektoren, die später schwer zu überschreiben sind. Faustregel: höchstens zwei, drei Ebenen. Außerdem geht BEM-Verkettung wie `&__title` nur in Sass, nicht im nativen CSS.",
  "Nesting hält Zusammengehöriges beisammen und läuft in allen aktuellen Browsern. Flaches CSS ist weiterhin völlig in Ordnung und in vielen Projekten Standard.",
  "Was ergibt `.nav { & a { } }` als flacher Selektor?",
  "`.nav a`, also alle Links innerhalb von `.nav`."),
 [("CSS Nesting verwenden", M+"CSS_nesting/Using_CSS_nesting"), ("Nesting-Selektor &", M+"Nesting_selector")]),
]))

SECTIONS.append(("flexbox", "Flexbox", "flex", "Eindimensionales Layout: Elemente in einer Reihe oder Spalte anordnen und verteilen.", [
C("Zentrieren",
  "Ein Element horizontal und vertikal in die Mitte setzen.",
  """
.hero {
  display: grid;
  place-items: center;
  min-height: 60vh;
}
""", """
.hero {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}
""",
 ("Flexbox hat zwei Achsen wie ein Kreuz: Die Hauptachse läuft in Leserichtung, die Querachse quer dazu. Zentrieren heißt, auf beiden Achsen in die Mitte zu rücken.",
  ["`display: flex` macht die Kinder zu Flex-Items, die in einer Reihe liegen.",
   "`justify-content: center` zentriert auf der Hauptachse, bei `row` also horizontal.",
   "`align-items: center` zentriert auf der Querachse, bei `row` also vertikal.",
   "`place-items: center` im Grid ist die Kurzform für `align-items` und `justify-items` zusammen. Ein Grid mit einem Kind braucht nur diese eine Zeile."],
  "Vertikales Zentrieren ohne Höhe erwarten. Ist der Container nur so hoch wie sein Inhalt, gibt es keinen Platz zum Zentrieren. Darum hier `min-height`.",
  "Grid mit `place-items` für ein einzelnes zentriertes Element. Flexbox, wenn mehrere Elemente in einer Reihe zentriert und verteilt werden sollen.",
  "Was ändert sich in der Flex-Variante, wenn du `flex-direction: column` ergänzt?",
  "Die Achsen tauschen: `justify-content` wirkt dann vertikal, `align-items` horizontal. Das Element bleibt trotzdem mittig, weil beide auf `center` stehen."),
 [("Flexbox-Grundlagen", M+"CSS_flexible_box_layout/Basic_concepts_of_flexbox"), ("place-items", M+"place-items"), ("justify-content", M+"justify-content"), ("align-items", M+"align-items")]),

C("Restplatz füllen: `flex: 1`",
  "Ein Element füllt den restlichen Platz. `flex` fasst drei Eigenschaften zusammen.",
  """
.layout  { display: flex; }
.sidebar { width: 16rem; }
.main    { flex: 1; }
""", """
.layout {
  display: flex;
}
.sidebar {
  width: 16rem;
}
.main {
  flex-grow: 1;
  flex-shrink: 1;
  flex-basis: 0%;
}
""",
 ("`flex-grow` ist der Hunger eines Elements nach freiem Platz. Wer `1` hat, nimmt sich, was übrig ist. Haben zwei Elemente je `1`, teilen sie fair.",
  ["`flex-basis` ist die Ausgangsgröße, bevor verteilt wird. Bei `flex: 1` ist sie `0`.",
   "`flex-grow: 1` heißt: Nimm dir einen Anteil vom freien Platz.",
   "`flex-shrink: 1` heißt: Wenn es eng wird, darfst du schrumpfen.",
   "Die Sidebar wächst nicht und behält ihre 16rem, `.main` bekommt den Rest."],
  "Sich wundern, dass lange Wörter oder Code-Blöcke ein Flex-Item trotz `flex: 1` breiter machen. Flex-Items schrumpfen standardmäßig nicht unter die Breite ihres Inhalts. Abhilfe: `min-width: 0` auf dem Item.",
  "Die Kurzform `flex: 1` ist Standard. Einzeleigenschaften, wenn du nur einen Teil steuern willst, z.B. `flex-shrink: 0` für ein Icon, das nie gestaucht werden soll.",
  "Zwei Elemente haben `flex: 1` und `flex: 2`. Wie wird der Platz verteilt?",
  "Im Verhältnis 1 zu 2: Das erste bekommt ein Drittel, das zweite zwei Drittel."),
 [("flex", M+"flex"), ("flex-grow", M+"flex-grow"), ("flex-basis", M+"flex-basis")]),

C("Abstände mit `gap`, Push mit `auto`",
  "Abstände zwischen Elementen mit `gap` statt Margins an jedem Kind. Ein `auto`-Margin schiebt Elemente an den Rand.",
  """
.nav {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.nav .logout { margin-left: auto; }
""", """
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
""",
 ("`gap` ist wie die Fugen zwischen Fliesen: Sie liegen nur zwischen den Fliesen, nie am Rand. Margins kleben dagegen an jeder einzelnen Fliese.",
  ["`gap` setzt den Abstand nur zwischen die Flex-Items, nicht davor oder dahinter.",
   "Mit Margins bekommt auch das letzte Element einen Abstand, den du extra wieder entfernen musst.",
   "`margin-left: auto` auf einem Flex-Item nimmt allen freien Platz links davon ein.",
   "Dadurch rutscht der Logout-Button ganz nach rechts, die anderen Links bleiben links."],
  "Bei umbrechenden Zeilen mit Margins arbeiten. Dann landen die Abstände am Zeilenende an der falschen Stelle. `gap` funktioniert auch über mehrere Zeilen korrekt, horizontal wie vertikal.",
  "`gap` immer in Flexbox und Grid. Margins nur noch, wenn ein einzelnes Element einen besonderen Abstand braucht.",
  "Was macht `gap: 1rem 2rem`?",
  "1rem Abstand zwischen den Zeilen und 2rem zwischen den Spalten. Es ist die Kurzform für `row-gap` und `column-gap`."),
 [("gap", M+"gap"), ("Ausrichtung in Flexbox", M+"CSS_flexible_box_layout/Aligning_items_in_a_flex_container")]),

C("Umbrechende Reihen: `flex-wrap`",
  "Elemente nebeneinander, die bei wenig Platz automatisch in die nächste Zeile umbrechen.",
  """
.cards {
  display: flex;
  flex-flow: row wrap;
  gap: 1rem;
}
.card { flex: 1 1 16rem; }
""", """
.cards {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  row-gap: 1rem;
  column-gap: 1rem;
}
.card {
  flex-grow: 1;
  flex-shrink: 1;
  flex-basis: 16rem;
}
""",
 ("Wie Bücher im Regal: Passt keins mehr in die Reihe, kommt das nächste aufs Brett darunter. `flex-grow` sorgt dafür, dass die Bücher einer Reihe die Lücke am Ende auffüllen.",
  ["`flex-wrap: wrap` erlaubt Umbrüche. Ohne werden alle Items in eine Zeile gequetscht.",
   "`flex-basis: 16rem` ist die Wunschbreite jedes Elements.",
   "Passen nicht mehr alle mit 16rem in die Zeile, bricht das letzte um.",
   "`flex-grow: 1` lässt die Elemente jeder Zeile wachsen, bis die Zeile voll ist."],
  "Die letzte Zeile sieht anders aus: Bleibt eine einzelne Karte übrig, wächst sie über die ganze Breite. Sollen alle Karten gleich breit sein, ist Grid mit `auto-fill` die bessere Wahl (siehe Grid).",
  "Flexbox mit Umbruch für Elemente unterschiedlicher Breite, z.B. Tags oder Buttons. Für gleichmäßige Kartenraster Grid.",
  "Welche zwei Eigenschaften fasst `flex-flow` zusammen?",
  "`flex-direction` und `flex-wrap`."),
 [("flex-wrap", M+"flex-wrap"), ("flex-flow", M+"flex-flow"), ("flex-basis", M+"flex-basis")]),
]))

SECTIONS.append(("grid", "Grid", "grid", "Zweidimensionales Layout: Zeilen und Spalten gleichzeitig planen.", [
C("Spalten mit `repeat()` und `fr`",
  "Ein Raster mit gleich breiten Spalten. `fr` steht für einen Anteil am freien Platz.",
  """
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}
""", """
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  row-gap: 1.5rem;
  column-gap: 1.5rem;
}
""",
 ("`fr` funktioniert wie Pizzastücke: `1fr 1fr 1fr` teilt die Pizza in drei gleiche Stücke, `2fr 1fr` gibt einer Spalte doppelt so viel.",
  ["`display: grid` macht das Element zum Raster, die Kinder werden automatisch auf die Zellen verteilt.",
   "`grid-template-columns` legt die Spalten fest. Zeilen entstehen automatisch nach Bedarf.",
   "`1fr` heißt: ein Anteil am Platz, der nach festen Größen und Abständen übrig bleibt.",
   "`repeat(3, 1fr)` ist die Kurzform für `1fr 1fr 1fr`. Bei 12 Spalten spart das viel Tipparbeit."],
  "Prozentwerte zusammen mit `gap` verwenden: `33.33% 33.33% 33.33%` plus Abstände wird zu breit. `fr` rechnet die Abstände automatisch heraus.",
  "`repeat()` ab drei gleichen Spalten. Ausgeschrieben, wenn die Spalten verschieden sind, z.B. `16rem 1fr` für Sidebar und Inhalt.",
  "Wie breit sind die Spalten bei `grid-template-columns: 200px 1fr 1fr` in einem 800px breiten Grid ohne gap?",
  "200px, 300px und 300px. Erst wird die feste Spalte abgezogen, die übrigen 600px werden auf zwei Anteile verteilt."),
 [("grid-template-columns", M+"grid-template-columns"), ("repeat()", M+"repeat"), ("Grid-Grundlagen", M+"CSS_grid_layout/Basic_concepts_of_grid_layout")]),

C("Responsives Grid ohne Media Query",
  "Das Grid berechnet selbst, wie viele Spalten passen. Ganz ohne Breakpoints.",
  """
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
  gap: 1rem;
}
""", """
.cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}
@media (width >= 36rem) {
  .cards { grid-template-columns: repeat(2, 1fr); }
}
@media (width >= 54rem) {
  .cards { grid-template-columns: repeat(3, 1fr); }
}
@media (width >= 72rem) {
  .cards { grid-template-columns: repeat(4, 1fr); }
}
""",
 ("Wie beim Fliesenlegen: Du sagst nur, wie groß eine Fliese mindestens sein soll, und der Fliesenleger rechnet selbst aus, wie viele in eine Reihe passen.",
  ["`minmax(16rem, 1fr)` heißt: Jede Spalte ist mindestens 16rem breit und darf wachsen.",
   "`auto-fill` legt so viele Spalten an, wie mit mindestens 16rem hineinpassen.",
   "Der übrige Platz wird über `1fr` gleichmäßig auf die Spalten verteilt.",
   "Wird das Fenster schmaler, fällt automatisch eine Spalte weg. Die Media-Query-Variante macht dasselbe in festen Stufen."],
  "`auto-fill` und `auto-fit` verwechseln. Bei wenigen Karten legt `auto-fill` leere Spalten an und die Karten bleiben schmal, `auto-fit` lässt die vorhandenen Karten in den freien Platz wachsen. Außerdem läuft das Grid auf Bildschirmen unter 16rem über. Abhilfe: `minmax(min(16rem, 100%), 1fr)`.",
  "`auto-fill` mit `minmax` für Kartenraster, Galerien und Produktlisten. Media Queries, wenn sich das Layout an bestimmten Breiten grundlegend ändern soll.",
  "Wie viele Spalten entstehen bei `repeat(auto-fill, minmax(200px, 1fr))` in einem 650px breiten Container ohne gap?",
  "Drei. Vier Spalten bräuchten mindestens 800px. Die drei Spalten werden dann auf je etwa 217px gestreckt."),
 [("repeat() mit auto-fill", M+"repeat"), ("minmax()", M+"minmax")]),

C("Seitenlayout mit `grid-template-areas`",
  "Das Seitenlayout als lesbare Skizze im CSS, statt mit Liniennummern.",
  """
.page {
  display: grid;
  grid-template-columns: 16rem 1fr;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
}
.page > header { grid-area: header; }
.page > aside  { grid-area: sidebar; }
.page > main   { grid-area: main; }
.page > footer { grid-area: footer; }
""", """
.page {
  display: grid;
  grid-template-columns: 16rem 1fr;
}
.page > header { grid-column: 1 / 3; grid-row: 1; }
.page > aside  { grid-column: 1;     grid-row: 2; }
.page > main   { grid-column: 2;     grid-row: 2; }
.page > footer { grid-column: 1 / 3; grid-row: 3; }
""",
 ("`grid-template-areas` ist ein Grundriss in ASCII-Art: Du zeichnest im CSS auf, welcher Raum wo liegt.",
  ["Jeder String in `grid-template-areas` ist eine Zeile, jedes Wort darin eine Zelle.",
   "Steht ein Name mehrfach nebeneinander, erstreckt sich der Bereich über diese Zellen.",
   "Mit `grid-area: header` legst du ein Element in den gleichnamigen Bereich.",
   "Die ausführliche Variante beschreibt dasselbe über Gitterlinien: `1 / 3` heißt von Linie 1 bis Linie 3, also über zwei Spalten."],
  "Nicht rechteckige Bereiche zeichnen, z.B. ein L aus `sidebar`. Dann ist die ganze Eigenschaft ungültig, und der Browser ignoriert sie ohne Fehlermeldung.",
  "Areas für Seitenlayouts, besonders responsiv: In einer Media Query zeichnest du einfach einen neuen Grundriss. Liniennummern für einzelne Elemente, die etwas überspannen sollen.",
  "Wie sieht der Grundriss fürs Handy aus, wenn alles untereinander stehen soll?",
  "`grid-template-columns: 1fr;` und `grid-template-areas: \"header\" \"main\" \"sidebar\" \"footer\";`. Die Elemente selbst musst du nicht anfassen."),
 [("Grid Template Areas", M+"CSS_grid_layout/Grid_template_areas"), ("grid-area", M+"grid-area")]),

C("Über alle Spalten: `1 / -1`",
  "Ein Element über mehrere oder alle Spalten strecken, egal wie viele Spalten es gibt.",
  """
.featured {
  grid-column: 1 / -1;
}
.wide {
  grid-column: span 2;
}
""", """
.featured {
  grid-column-start: 1;
  grid-column-end: -1;
}
.wide {
  grid-column-start: auto;
  grid-column-end: span 2;
}
""",
 ("Gitterlinien sind wie Hausnummern, die man von beiden Enden der Straße zählen kann: von vorne 1, 2, 3, von hinten -1, -2, -3. `1 / -1` heißt: von der ersten bis zur letzten Linie.",
  ["Ein Grid mit drei Spalten hat vier senkrechte Linien, nummeriert von 1 bis 4.",
   "Negative Zahlen zählen von hinten: `-1` ist immer die letzte Linie.",
   "`grid-column: 1 / -1` spannt das Element daher über alle Spalten, auch wenn `auto-fill` die Spaltenzahl ändert.",
   "`span 2` heißt: zwei Spalten breit, beginnend dort, wo das Element automatisch landen würde."],
  "`grid-column: 1 / 3` schreiben und erwarten, dass das bei vier Spalten immer noch die ganze Breite ist. Feste Liniennummern passen sich nicht an. Und `-1` zählt nur Linien, die im Template definiert sind, nicht automatisch erzeugte Zeilen.",
  "Die Kurzform `grid-column` fast immer. Die Einzeleigenschaften nur, wenn du gezielt Start oder Ende änderst.",
  "Über wie viele Spalten erstreckt sich `grid-column: 2 / 4`?",
  "Über zwei: von Linie 2 bis Linie 4, also die zweite und dritte Spalte."),
 [("grid-column", M+"grid-column"), ("Linienbasierte Platzierung", M+"CSS_grid_layout/Grid_layout_using_line-based_placement")]),
]))

SECTIONS.append(("position", "Positionierung", "position", "Elemente aus dem normalen Fluss lösen: überlagern, festhalten, stapeln.", [
C("Überlagern mit `inset`",
  "Ein Element exakt über ein anderes legen, z.B. ein Overlay über ein Bild.",
  """
.card { position: relative; }

.card .overlay {
  position: absolute;
  inset: 0;
}
""", """
.card {
  position: relative;
}
.card .overlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
""",
 ("`position: relative` beim Elternelement schlägt einen Nagel ein. `position: absolute` beim Kind hängt es an diesem Nagel auf, statt am Rand der ganzen Seite.",
  ["`position: absolute` nimmt das Element aus dem normalen Fluss. Die anderen Elemente verhalten sich, als gäbe es es nicht.",
   "Positioniert wird relativ zum nächsten Vorfahren, dessen `position` nicht `static` ist. Darum `position: relative` auf `.card`.",
   "`top`, `right`, `bottom` und `left` auf 0 ziehen das Element an alle vier Kanten, es füllt die Karte komplett aus.",
   "`inset: 0` ist die Kurzform dafür und folgt derselben Reihenfolge wie `margin`."],
  "`position: relative` beim Elternelement vergessen. Dann orientiert sich das Overlay am nächsthöheren positionierten Element, oft an der ganzen Seite, und bedeckt plötzlich alles.",
  "`inset` ist kürzer und läuft in allen aktuellen Browsern. Einzelwerte, wenn du nur an einer Ecke positionierst, z.B. ein Badge mit `top: 0.5rem; right: 0.5rem`.",
  "Was bedeutet `inset: 1rem 2rem`?",
  "Oben und unten 1rem, rechts und links 2rem Abstand zum Bezugselement, wie bei `margin`."),
 [("inset", M+"inset"), ("position", M+"position")]),

C("Kleben bleiben: `sticky`",
  "Ein Header, der beim Scrollen oben stehen bleibt.",
  """
.site-header {
  position: sticky;
  top: 0;
}
""", """
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
}
body {
  padding-top: 4rem; /* Höhe des Headers */
}
""",
 ("Ein Sticky-Element ist wie ein Post-it, das normal mitläuft, bis es oben am Bildschirmrand ankommt. Dort bleibt es kleben, solange sein Elternelement sichtbar ist.",
  ["`position: sticky` verhält sich zunächst wie ein normales Element im Fluss.",
   "Erreicht es beim Scrollen die Schwelle aus `top: 0`, bleibt es dort haften.",
   "Es klebt nur innerhalb seines Elternelements. Scrollt das Elternelement aus dem Bild, nimmt es den Header mit.",
   "`position: fixed` klebt dagegen immer am Fenster und nimmt keinen Platz im Fluss ein. Darum braucht die ausführliche Variante das `padding-top` auf `body`, sonst verschwindet der Seitenanfang unter dem Header."],
  "Sticky scheint nicht zu funktionieren, weil ein Vorfahre `overflow: hidden` oder `overflow: auto` hat. Dann klebt das Element an diesem Container statt am Fenster. Ebenfalls häufig: Der Schwellenwert `top` fehlt.",
  "`sticky` für Header, Tabellenköpfe und Inhaltsverzeichnisse. `fixed` für Elemente, die unabhängig vom Layout immer sichtbar sein sollen, z.B. einen Chat-Button unten rechts.",
  "Warum bleibt ein Sticky-Header nicht stehen, wenn er das einzige Kind eines niedrigen `<div>` ist?",
  "Weil er nur innerhalb seines Elternelements kleben kann. Ist das Elternelement nicht höher als der Header, hat er keinen Weg, den er zurücklegen könnte."),
 [("position", M+"position")]),

C("Ebenen ordnen: `z-index` und `isolation`",
  "Ebenen ordnen, ohne dass sich `z-index`-Werte quer durch die Seite ins Gehege kommen.",
  """
.card {
  isolation: isolate;
}
.card .badge {
  position: absolute;
  z-index: 1;
}
""", """
.card {
  position: relative;
  z-index: 0;
}
.card .badge {
  position: absolute;
  z-index: 1;
}
""",
 ("Ein Stapelkontext ist wie ein Ordner auf dem Schreibtisch. Die Blätter im Ordner kannst du beliebig sortieren, aber der Ordner liegt als Ganzes im Stapel. Ein Blatt mit `z-index: 9999` kommt nicht aus seinem Ordner heraus.",
  ["`z-index` wirkt nur bei positionierten Elementen sowie bei Flex- und Grid-Items.",
   "Bestimmte Eigenschaften erzeugen einen neuen Stapelkontext, z.B. `position` mit `z-index`, `opacity` unter 1, `transform` oder `isolation: isolate`.",
   "Alle `z-index`-Werte innerhalb eines Kontexts gelten nur dort.",
   "`isolation: isolate` erzeugt diesen Kontext ohne Nebenwirkungen. Die ausführliche Variante braucht dafür `position` und `z-index`."],
  "`z-index` immer weiter erhöhen (`999`, `99999`), weil ein Element nicht nach vorne kommt. Meist liegt es in einem Stapelkontext, der als Ganzes weiter hinten liegt. Dann helfen höhere Zahlen nie.",
  "`isolation: isolate` für Komponenten, deren interne Ebenen nicht mit dem Rest der Seite kollidieren sollen. Kleine Werte wie 1, 2, 3 reichen fast immer, am besten zentral als Custom Properties.",
  "Ein Dropdown mit `z-index: 100` liegt hinter einem Element mit `z-index: 2`. Woran liegt das wahrscheinlich?",
  "Ein Vorfahre des Dropdowns bildet einen eigenen Stapelkontext mit niedrigerem `z-index` als 2. Das Dropdown kann diesen Kontext nicht verlassen."),
 [("z-index", M+"z-index"), ("isolation", M+"isolation"), ("Stapelkontext", M+"CSS_positioned_layout/Stacking_context")]),
]))

SECTIONS.append(("responsive", "Responsive Design", "responsive", "Layouts, die sich an Bildschirm und verfügbaren Platz anpassen.", [
C("Media Queries, mobile-first",
  "Erst die Handy-Version schreiben, dann für größere Bildschirme erweitern.",
  """
.nav { flex-direction: column; }

@media (width >= 48rem) {
  .nav { flex-direction: row; }
}
""", """
.nav {
  flex-direction: column;
}

@media screen and (min-width: 48rem) {
  .nav {
    flex-direction: row;
  }
}
""",
 ("Mobile-first ist wie Kofferpacken: Erst das Nötigste ins Handgepäck, und wenn mehr Platz da ist, kommt Zusätzliches dazu.",
  ["Die Regeln außerhalb der Media Query gelten für alle Bildschirme, also auch fürs Handy.",
   "Die Media Query ergänzt Regeln ab einer Mindestbreite.",
   "`width >= 48rem` ist die neue Bereichsschreibweise und bedeutet dasselbe wie `min-width: 48rem`.",
   "`screen` beschränkt auf Bildschirme. Weil `all` der Standard ist, lässt man es meist weg."],
  "Das Viewport-Meta-Tag im HTML vergessen: `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">`. Ohne es tut das Handy so, als sei es etwa 980px breit, und deine Media Queries für kleine Bildschirme greifen nicht.",
  "Die Bereichsschreibweise ist kürzer und bei Spannen wie `(30rem <= width < 60rem)` viel lesbarer. Alle aktuellen Browser können sie. `min-width` steht in fast jedem älteren Projekt.",
  "Warum ist es sinnvoll, Breakpoints in `rem` oder `em` statt in `px` anzugeben?",
  "Wenn jemand die Schrift im Browser vergrößert, greifen die Breakpoints entsprechend früher. Das Layout bricht dann um, bevor der Text gequetscht wird."),
 [("@media", M+"@media"), ("Media Queries verwenden", M+"CSS_media_queries/Using_media_queries")]),

C("Fließende Größen: `clamp()`",
  "Schriftgrößen und Abstände, die mit dem Bildschirm wachsen, aber Grenzen einhalten.",
  """
h1 {
  font-size: clamp(1.75rem, 1rem + 3vw, 3rem);
}
""", """
h1 {
  font-size: 1.75rem;
}
@media (width >= 40rem) {
  h1 { font-size: 2.25rem; }
}
@media (width >= 64rem) {
  h1 { font-size: 3rem; }
}
""",
 ("`clamp()` ist ein Thermostat mit Unter- und Obergrenze: Dazwischen regelt es frei, aber es wird nie kälter als das Minimum und nie wärmer als das Maximum.",
  ["`clamp(MIN, WUNSCH, MAX)` nimmt den Wunschwert, solange er zwischen den Grenzen liegt.",
   "Der Wunschwert `1rem + 3vw` wächst mit der Fensterbreite, weil `1vw` ein Prozent der Viewport-Breite ist.",
   "Auf dem Handy greift das Minimum 1.75rem, auf großen Bildschirmen das Maximum 3rem.",
   "Die Media-Query-Variante springt in Stufen, `clamp()` wächst stufenlos."],
  "Nur `vw` als Wunschwert nehmen, z.B. `clamp(1rem, 4vw, 3rem)`. Reine `vw`-Werte reagieren schlecht auf Browser-Zoom. Ein `rem`-Anteil wie in `1rem + 3vw` hält die Schrift zoombar.",
  "`clamp()` für Überschriften, Abschnittsabstände und Container-Padding. Media Queries, wenn sich nicht nur Größen, sondern das Layout ändert.",
  "Welchen Wert ergibt `clamp(10px, 50px, 30px)`?",
  "30px. Der Wunschwert 50px liegt über dem Maximum, also greift die Obergrenze."),
 [("clamp()", M+"clamp"), ("min()", M+"min"), ("max()", M+"max")]),

C("Bilder: `aspect-ratio` und `object-fit`",
  "Bilder in einem festen Seitenverhältnis anzeigen, ohne sie zu verzerren.",
  """
.thumb {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}
""", """
/* HTML: <div class="thumb"><img src="..."></div> */
.thumb {
  position: relative;
  padding-top: 56.25%; /* 9 / 16 = 0.5625 */
}
.thumb img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
""",
 ("`object-fit: cover` ist wie ein Foto, das im Bilderrahmen so weit vergrößert wird, bis kein Rand mehr frei bleibt. Was übersteht, wird abgeschnitten, aber nichts wird gestaucht.",
  ["`aspect-ratio: 16 / 9` berechnet die Höhe aus der Breite.",
   "Ohne `object-fit` würde das Bild auf genau diese Fläche gestreckt und verzerrt.",
   "`object-fit: cover` füllt die Fläche und schneidet den Überstand ab. `contain` zeigt dagegen das ganze Bild, mit freien Rändern.",
   "Die ausführliche Variante ist der alte Padding-Trick: Prozentwerte bei `padding-top` beziehen sich auf die Breite, deshalb ergibt 56.25% genau 16:9."],
  "Bildern im HTML keine `width` und `height` geben. Dann weiß der Browser vor dem Laden nicht, wie viel Platz er reservieren soll, und die Seite springt, sobald das Bild erscheint (Layout Shift).",
  "`aspect-ratio` heute immer. Den Padding-Trick musst du nur in älterem Code erkennen.",
  "Welches Seitenverhältnis ergibt `padding-top: 100%`?",
  "1:1, also ein Quadrat, weil das Padding 100% der Breite beträgt."),
 [("aspect-ratio", M+"aspect-ratio"), ("object-fit", M+"object-fit")]),

C("Container Queries",
  "Eine Komponente reagiert auf den Platz ihres Containers statt auf die Bildschirmbreite.",
  """
.card-list { container-type: inline-size; }

@container (width >= 30rem) {
  .card { flex-direction: row; }
}
""", """
/* Pro Einsatzort eine eigene Regel */
.main .card {
  flex-direction: row;
}

@media (width < 64rem) {
  .main .card {
    flex-direction: column;
  }
}

.sidebar .card {
  flex-direction: column;
}
""",
 ("Eine Media Query fragt: Wie groß ist das Zimmer? Eine Container Query fragt: Wie groß ist der Tisch, auf dem ich stehe? Für eine Karte ist der Tisch die wichtigere Frage.",
  ["`container-type: inline-size` macht ein Element zum Container, dessen Breite abgefragt werden kann.",
   "`@container (width >= 30rem)` greift, wenn dieser Container mindestens 30rem breit ist, egal wie breit der Bildschirm ist.",
   "Dieselbe Karte sieht in der schmalen Sidebar anders aus als im breiten Hauptbereich, ganz ohne Zusatzregeln.",
   "Die ausführliche Variante muss jeden Einsatzort einzeln kennen und mit eigenen Selektoren oder Media Queries behandeln."],
  "Den Container selbst in seiner Container Query stylen wollen. Eine Container Query kann nur die Elemente darin verändern. Außerdem braucht die Abfrage `container-type` auf einem Vorfahren, sonst greift sie nie.",
  "Container Queries für wiederverwendbare Komponenten wie Karten oder Widgets. Media Queries für das Seitenlayout als Ganzes.",
  "Warum passen Container Queries so gut zu React-Komponenten?",
  "Weil eine Komponente nicht wissen muss, wo sie eingebaut wird. Sie passt sich dem verfügbaren Platz an, ob in Sidebar, Modal oder Hauptbereich."),
 [("Container Queries", M+"CSS_containment/Container_queries"), ("container-type", M+"container-type")]),
]))

SECTIONS.append(("animation", "Übergänge und Animation", "motion", "Bewegung, die Zustandswechsel verständlich macht, und Rücksicht auf alle, die keine wollen.", [
C("Übergänge: `transition`",
  "Weiche Übergänge zwischen zwei Zuständen, z.B. beim Hover.",
  """
.button {
  transition: background-color 200ms ease-out, transform 200ms ease-out;
}
.button:hover {
  background-color: var(--brand-dark);
  transform: translateY(-2px);
}
""", """
.button {
  transition-property: background-color, transform;
  transition-duration: 200ms, 200ms;
  transition-timing-function: ease-out, ease-out;
  transition-delay: 0s, 0s;
}
.button:hover {
  background-color: var(--brand-dark);
  transform: translateY(-2px);
}
""",
 ("Ohne `transition` springt das Licht wie bei einem Kippschalter von aus auf an. Mit `transition` ist es ein Dimmer, der in festgelegter Zeit hochfährt.",
  ["Die `transition` steht auf dem Grundzustand, nicht auf `:hover`. So gilt sie für Hin- und Rückweg.",
   "`transition-property` legt fest, welche Eigenschaften weich wechseln.",
   "`duration` ist die Dauer, `timing-function` die Kurve. `ease-out` startet schnell und bremst sanft ab.",
   "In der Kurzform steht jede Eigenschaft mit ihren Werten, mehrere werden mit Komma getrennt."],
  "`transition: all` benutzen. Dann animiert auch, was nicht animieren soll, z.B. Layout-Änderungen, und das kann ruckeln. Besser gezielt `transform`, `opacity` und Farben animieren, die laufen am flüssigsten.",
  "Die Kurzform pro Eigenschaft ist üblich. Einzeleigenschaften, wenn du z.B. nur die Dauer in einer Variante änderst.",
  "Was passiert, wenn die `transition` nur in `.button:hover` steht?",
  "Beim Hineinfahren gibt es einen weichen Übergang, beim Verlassen springt der Button sofort zurück, weil die Regel dann nicht mehr gilt."),
 [("transition", M+"transition"), ("CSS-Übergänge verwenden", M+"CSS_transitions/Using_CSS_transitions")]),

C("Animationen und reduzierte Bewegung",
  "Mehrstufige Animationen mit `@keyframes`, abgeschaltet für alle, die im System weniger Bewegung eingestellt haben.",
  """
@keyframes fade-in {
  from { opacity: 0; transform: translateY(8px); }
}

.toast { animation: fade-in 300ms ease-out both; }

@media (prefers-reduced-motion: reduce) {
  .toast { animation: none; }
}
""", """
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
""",
 ("`@keyframes` ist ein Daumenkino: Du zeichnest Anfangs- und Endbild, und der Browser malt die Bilder dazwischen.",
  ["`@keyframes fade-in` definiert eine Animation mit Namen. `from` ist der Start, `to` das Ende.",
   "Fehlt `to`, nimmt der Browser den normalen Zustand des Elements als Ende. Darum reicht in der Kurzform `from`.",
   "`animation` verbindet Element und Keyframes: Name, Dauer, Kurve und Füllmodus.",
   "`both` sorgt dafür, dass der Startzustand schon vor Beginn gilt und der Endzustand danach erhalten bleibt.",
   "`prefers-reduced-motion` erkennt, ob jemand im Betriebssystem weniger Bewegung eingestellt hat, z.B. wegen Schwindel."],
  "Den Namen der Animation falsch schreiben. Es gibt keine Fehlermeldung, die Animation läuft einfach nicht. Und `prefers-reduced-motion` vergessen: Große Bewegungen können bei manchen Menschen Übelkeit auslösen.",
  "`transition` für Wechsel zwischen zwei Zuständen. `@keyframes` für alles, was von selbst startet, sich wiederholt oder mehr als zwei Stufen hat.",
  "Wie lässt du eine Animation endlos laufen?",
  "Mit `infinite` in der Kurzform, z.B. `animation: spin 1s linear infinite;`, oder mit `animation-iteration-count: infinite`."),
 [("animation", M+"animation"), ("@keyframes", M+"@keyframes"), ("prefers-reduced-motion", M+"@media/prefers-reduced-motion"), ("CSS-Animationen verwenden", M+"CSS_animations/Using_CSS_animations")]),
]))
