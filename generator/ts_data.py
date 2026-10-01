H = "https://www.typescriptlang.org/docs/handbook/"
EV = H + "2/everyday-types.html"
NA = H + "2/narrowing.html"
OB = H + "2/objects.html"
FN = H + "2/functions.html"
GE = H + "2/generics.html"
UT = H + "utility-types.html"
RT = "https://react.dev/learn/typescript"
CFG = "https://www.typescriptlang.org/tsconfig/"

def C(t, d, k, a, e, l):
    return dict(t=t, d=d, k=k.strip("\n"), a=a.strip("\n"), e=e, l=l)

SECTIONS = []

# ---------------- GRUNDLAGEN ----------------
SECTIONS.append(("grundlagen", "Grundlagen", "basics", "Wie TypeScript Typen erkennt und wo du nachhelfen musst.", [
C("Typinferenz und Basistypen",
  "TypeScript erkennt den Typ meist selbst aus dem Wert (Inferenz). Annotieren musst du nur dort, wo es nichts abzuleiten gibt.",
  """
let name = "Lea";        // string
let age = 31;            // number
let isAdmin = false;     // boolean
const scores = [3, 5];   // number[]
""", """
let name: string = "Lea";
let age: number = 31;
let isAdmin: boolean = false;
const scores: number[] = [3, 5];
// gleichwertig: Array<number>
""",
 ("TypeScript ist wie ein aufmerksamer Kollege, der beim Lesen mitdenkt: Steht da `= \"Lea\"`, ist klar, dass das Text ist. Das muss niemand extra dazuschreiben.",
  ["Beim Zuweisen schaut TypeScript auf den Wert rechts und merkt sich den passenden Typ.",
   "Ab dann prüft es jede Verwendung: `age = \"alt\"` wird rot markiert, weil `age` eine `number` ist.",
   "Bei `const` wird der Typ sogar genauer: `const role = \"admin\"` hat den Typ `\"admin\"`, nicht nur `string`.",
   "Alle Typen verschwinden beim Kompilieren. Im ausgeführten JavaScript gibt es sie nicht mehr."],
  "Ein leeres Array ohne Typ anlegen: Bei `const ids = []` kann TypeScript nichts ableiten, und der Typ wird `any[]` oder `never[]`. Hier immer annotieren: `const ids: number[] = []`.",
  "Bei Variablen mit Startwert die Inferenz arbeiten lassen. Explizit annotieren, wenn es keinen Startwert gibt, der Startwert leer ist oder der Typ breiter sein soll als der erste Wert.",
  "Welchen Typ hat `x` bei `let x;` ohne Wert und ohne Annotation?",
  "TypeScript behandelt `x` zunächst als `any` und kann nichts prüfen. Darum Variablen ohne Startwert immer annotieren, z.B. `let x: string;`."),
 [("Typ-Annotationen", EV+"#type-annotations-on-variables"), ("Typinferenz", H+"type-inference.html"), ("Arrays", EV+"#arrays")]),

C("Tupel",
  "Ein Array mit fester Länge, bei dem jede Position einen eigenen Typ hat. Kennst du von `useState`.",
  """
const point = [10, 20] as const;

function useToggle() {
  const [on, setOn] = useState(false);
  return [on, () => setOn(!on)] as const;
}
""", """
const point: readonly [number, number] = [10, 20];

function useToggle(): [boolean, () => void] {
  const [on, setOn] = useState(false);
  const toggle = (): void => setOn(!on);
  return [on, toggle];
}
""",
 ("Ein Tupel ist wie ein Formular mit festen Feldern: Feld 1 ist immer der Wert, Feld 2 immer die Funktion. Ein normales Array ist eher ein Stapel, in dem jedes Blatt gleich aussieht.",
  ["`[10, 20]` allein wird als `number[]` erkannt, also als Liste beliebiger Länge.",
   "`as const` macht daraus ein unveränderliches Tupel mit genau diesen Positionen.",
   "Mit dem Rückgabetyp `[boolean, () => void]` legst du die Positionen ausdrücklich fest.",
   "Beim Auspacken mit `const [on, toggle] = useToggle()` kennt TypeScript dadurch für jede Variable den richtigen Typ."],
  "Ein Paar ohne Tupel-Typ zurückgeben: `return [on, toggle]` wird zu `(boolean | (() => void))[]`. Beim Auspacken ist dann jede Variable „boolean oder Funktion“, und `toggle()` lässt sich nicht aufrufen.",
  "`as const` ist schnell und praktisch für eigene Hooks. Der explizite Rückgabetyp dokumentiert die Schnittstelle besser und ist bei exportierten Funktionen die sauberere Wahl.",
  "Welchen Typ hat `const pair = [\"a\", 1]` ohne `as const`?",
  "`(string | number)[]`, also ein Array, in dem jedes Element string oder number sein kann. Die Positionen gehen verloren."),
 [("Tupel-Typen", OB+"#tuple-types"), ("const assertions", H+"release-notes/typescript-3-4.html#const-assertions")]),

C("`unknown` statt `any`",
  "`any` schaltet die Prüfung ab. `unknown` heißt: Typ noch unbekannt, erst prüfen, dann benutzen.",
  """
const data = JSON.parse(text) as User; // ungeprüft!
console.log(data.name);
""", """
const data: unknown = JSON.parse(text);

if (typeof data === "object" && data !== null && "name" in data) {
  console.log(data.name);
}
""",
 ("`any` ist ein Paket ohne Kontrolle, es geht einfach durch. `unknown` ist ein Paket, das am Zoll festgehalten wird, bis du nachgesehen hast, was drin ist.",
  ["`JSON.parse` gibt `any` zurück. TypeScript weiß nicht, was im Text stand.",
   "`as User` ist eine Behauptung: Du sagst dem Compiler „vertrau mir“. Geprüft wird dabei nichts.",
   "Mit `unknown` verlangt TypeScript eine Prüfung, bevor du auf Eigenschaften zugreifst.",
   "Jede Prüfung (`typeof`, `!== null`, `in`) engt den Typ weiter ein, bis der Zugriff sicher ist."],
  "`as` benutzen, um rote Unterstreichungen loszuwerden. Der Fehler verschwindet aus dem Editor, aber nicht aus dem Programm: Fehlt `name` wirklich, stürzt es zur Laufzeit ab.",
  "`as` nur, wenn du es wirklich besser weißt als der Compiler. Für Daten von außen (API, JSON, Formulare) `unknown` plus Prüfung, im Projekt am besten mit einer Bibliothek wie Zod (siehe Karte „Daten von außen prüfen“).",
  "Was passiert zur Laufzeit bei `const u = JSON.parse(\"{}\") as User; u.name.toUpperCase()`?",
  "Ein TypeError, weil `u.name` `undefined` ist. `as` hat nichts geprüft, sondern nur den Compiler beruhigt."),
 [("any", EV+"#any"), ("unknown", FN+"#unknown"), ("Type Assertions (as)", EV+"#type-assertions")]),
]))

# ---------------- FUNKTIONEN ----------------
SECTIONS.append(("funktionen", "Funktionen", "functions", "Parameter brauchen Typen, Rückgaben kann TypeScript oft selbst ableiten.", [
C("Funktionen typisieren",
  "Parameter brauchen immer Typen. Den Rückgabetyp leitet TypeScript ab, explizit ist er aber eine gute Dokumentation.",
  """
const add = (a: number, b: number) => a + b;

const formatPrice = (cents: number) =>
  `${(cents / 100).toFixed(2)} €`;
""", """
function add(a: number, b: number): number {
  return a + b;
}

type Formatter = (cents: number) => string;

const formatPrice: Formatter = function (cents) {
  return (cents / 100).toFixed(2) + " €";
};
""",
 ("Eine Funktionssignatur ist wie ein Steckdosenformat: Sie legt fest, welcher Stecker hineinpasst (Parameter) und was herauskommt (Rückgabe).",
  ["Parameter ohne Typ werden zu `any`. Mit `noImplicitAny` (Teil von `strict`) ist das ein Fehler.",
   "Den Rückgabetyp leitet TypeScript aus den `return`-Anweisungen ab.",
   "Ein expliziter Rückgabetyp wird geprüft: Gibst du versehentlich etwas anderes zurück, meldet TypeScript den Fehler direkt in der Funktion statt erst beim Aufrufer.",
   "Ein Funktionstyp wie `Formatter` beschreibt die ganze Signatur. Weist du eine Funktion zu, bekommen ihre Parameter die Typen automatisch."],
  "Einen Zweig ohne `return` vergessen. Ohne Rückgabetyp wird daraus still `string | undefined`, und der Fehler taucht erst weit entfernt beim Aufrufer auf. Mit `: string` meldet TypeScript ihn sofort an der richtigen Stelle.",
  "Kurz für kleine, lokale Hilfsfunktionen. Expliziter Rückgabetyp bei exportierten Funktionen, Services im Backend und allem, was andere benutzen.",
  "Braucht `n` in `[1, 2].map(n => n * 2)` eine Annotation?",
  "Nein. TypeScript weiß aus dem Array, dass `n` eine `number` ist (kontextuelle Typisierung). Annotieren musst du nur Parameter von Funktionen, die du selbst deklarierst."),
 [("Funktionen", EV+"#functions"), ("Funktionstypen", FN+"#function-type-expressions"), ("Kontextuelle Typisierung", EV+"#anonymous-functions")]),

C("Optionale Parameter und Defaults",
  "Ein `?` macht einen Parameter optional. Ein Default-Wert macht ihn ebenfalls optional und legt gleich den Typ fest.",
  """
function greet(name?: string) {
  return `Hi ${name ?? "Gast"}`;
}

function paginate(page = 1, size = 20) { ... }
""", """
function greet(name: string | undefined): string {
  if (name === undefined) {
    return "Hi Gast";
  }
  return "Hi " + name;
}

function paginate(page: number = 1, size: number = 20): void { ... }
""",
 ("Ein optionaler Parameter ist ein Feld mit dem Vermerk „darf leer bleiben“. Ein Default-Parameter ist ein vorausgefülltes Feld.",
  ["`name?: string` heißt: Der Parameter darf fehlen, sein Typ ist dann `string | undefined`.",
   "Darum musst du vor der Verwendung mit `??` oder `if` den `undefined`-Fall behandeln.",
   "`page = 1` macht den Parameter optional und leitet den Typ `number` aus dem Default ab.",
   "Achtung bei der ausführlichen Variante: `name: string | undefined` ist nicht optional. Der Aufrufer muss `greet(undefined)` schreiben, `greet()` ist dort ein Fehler."],
  "Optionale Parameter vor Pflichtparameter setzen: `(a?: string, b: number)` ist ein Fehler. Optionale Parameter müssen hinten stehen.",
  "`?` für Werte, die wirklich fehlen dürfen. Default-Werte, wenn es einen sinnvollen Standard gibt, denn dann musst du im Funktionskörper nichts mehr prüfen.",
  "Was ist beim Aufruf der Unterschied zwischen `(x?: number)` und `(x: number | undefined)`?",
  "Beim ersten darfst du `f()` schreiben. Beim zweiten musst du `f(undefined)` übergeben, weil der Parameter Pflicht ist."),
 [("Optionale Parameter", FN+"#optional-parameters")]),
]))

# ---------------- OBJEKTE ----------------
SECTIONS.append(("objekte", "Objekte", "objects", "Die Form von Daten beschreiben, die durch deine App und über die API fließen.", [
C("Objekttypen: `interface` und `type`",
  "Objekttypen kannst du direkt hinschreiben oder einmal benennen und wiederverwenden.",
  """
function printUser(user: { name: string; age: number }) {
  console.log(`${user.name} (${user.age})`);
}
""", """
interface User {
  name: string;
  age: number;
}
// oder: type User = { name: string; age: number };

function printUser(user: User): void {
  console.log(user.name + " (" + user.age + ")");
}
""",
 ("Ein Interface ist ein Steckbrief: Wer als `User` durchgehen will, muss mindestens diese Felder mit diesen Typen haben.",
  ["Ein Inline-Typ gilt nur an dieser einen Stelle.",
   "`interface` oder `type` geben der Form einen Namen, den du überall importieren kannst.",
   "TypeScript vergleicht nach Struktur, nicht nach Namen: Jedes Objekt mit `name` und `age` passt, egal wo es herkommt.",
   "Für Objekte sind `interface` und `type` fast austauschbar. `type` kann zusätzlich Unions benennen, ein `interface` kann nachträglich erweitert werden."],
  "Ein Objekt-Literal mit Extra-Feldern direkt übergeben: `printUser({ name: \"Lea\", age: 31, admin: true })` ist ein Fehler (Excess Property Check). Bei einer Variable mit Extra-Feldern prüft TypeScript das nicht.",
  "Inline für einmalige, kleine Typen. Sobald ein Typ zweimal vorkommt oder Frontend und Backend ihn teilen, benennen. Viele Teams nehmen `interface` für Objekte und `type` für alles andere.",
  "Darf man ein Objekt `{ name: \"Lea\", age: 31, city: \"Köln\" }` aus einer Variable an `printUser` übergeben?",
  "Ja. Es hat alle geforderten Felder, und Extra-Felder sind bei Variablen erlaubt. Nur direkt hingeschriebene Objekt-Literale werden auf Extra-Felder geprüft."),
 [("Objekttypen", EV+"#object-types"), ("Interfaces", EV+"#interfaces"), ("type vs. interface", EV+"#differences-between-type-aliases-and-interfaces"), ("Excess Property Checks", OB+"#excess-property-checks")]),

C("Optionale und `readonly` Felder",
  "`?` markiert Felder, die fehlen dürfen. `readonly` verbietet das Überschreiben nach dem Erstellen.",
  """
interface Todo {
  readonly id: number;
  title: string;
  dueDate?: string;
}

const label = todo.dueDate?.slice(0, 10) ?? "kein Datum";
""", """
interface Todo {
  readonly id: number;
  title: string;
  dueDate?: string;
}

let label: string;
if (todo.dueDate !== undefined) {
  label = todo.dueDate.slice(0, 10);
} else {
  label = "kein Datum";
}
""",
 ("`readonly` ist ein Feld mit dem Stempel „nicht ändern“, wie eine Kundennummer. `?` ist ein Feld, das auf dem Formular leer bleiben darf.",
  ["`dueDate?: string` heißt: Das Feld kann fehlen, beim Lesen ist es `string | undefined`.",
   "Vor der Benutzung erzwingt TypeScript eine Prüfung. Nach `!== undefined` weiß es, dass ein `string` vorliegt (Narrowing).",
   "`readonly id` erlaubt das Setzen beim Erstellen, aber `todo.id = 5` danach ist ein Fehler.",
   "`readonly` gilt nur beim Kompilieren. Im laufenden JavaScript ließe sich der Wert trotzdem ändern."],
  "Annehmen, `readonly` mache das Objekt komplett unveränderlich. Es schützt nur die Eigenschaft selbst: Bei `readonly tags: string[]` ist `todo.tags.push(\"x\")` weiterhin erlaubt. Dafür bräuchte es `readonly string[]`.",
  "Optional Chaining für schnelles Lesen. Die if-Variante, wenn im vorhandenen Fall mehr passieren soll als ein einzelner Ausdruck.",
  "Ist `todo.dueDate.length` ohne Prüfung erlaubt?",
  "Nein. `dueDate` könnte `undefined` sein, darum meldet TypeScript „possibly undefined“. Erst prüfen oder `?.` benutzen."),
 [("Optionale Felder", OB+"#optional-properties"), ("readonly", OB+"#readonly-properties"), ("Narrowing", NA)]),

C("Typen erweitern: `extends` und `&`",
  "Bestehende Typen um Felder ergänzen, statt alles doppelt zu schreiben.",
  """
type Admin = User & { permissions: string[] };
""", """
interface Admin extends User {
  permissions: string[];
}
""",
 ("Wie eine Weiterbildung, die auf einer Ausbildung aufbaut: Ein Admin kann alles, was ein User kann, plus Rechte vergeben.",
  ["`interface Admin extends User` übernimmt alle Felder von `User` und fügt neue hinzu.",
   "`User & { ... }` (Intersection) bildet einen Typ, der beide Teile gleichzeitig erfüllen muss. Das Ergebnis ist hier dasselbe.",
   "Überall, wo ein `User` erwartet wird, darf ein `Admin` übergeben werden, weil er alle User-Felder hat."],
  "Bei Konflikten verhalten sich beide unterschiedlich. Haben beide Teile ein Feld `id` mit verschiedenen Typen, meldet `extends` sofort einen Fehler, während `&` still den unmöglichen Typ `never` für `id` erzeugt.",
  "`extends` bei Interfaces, weil die Fehlermeldungen klarer sind. `&` mit `type`, z.B. um schnell ein Feld an einen vorhandenen Typ zu hängen.",
  "Darf man einen `Admin` an eine Funktion übergeben, die einen `User` erwartet? Und umgekehrt?",
  "Admin an User: ja, er hat alle nötigen Felder. User an Admin: nein, ihm fehlt `permissions`."),
 [("Typen erweitern", OB+"#extending-types"), ("Intersection Types", OB+"#intersection-types"), ("extends vs. Intersection", OB+"#interface-extension-vs-intersection")]),

C("Nachschlage-Objekte: `Record`",
  "Für Objekte, die wie Tabellen benutzt werden: beliebig viele Keys mit gleichem Werttyp.",
  """
const stock: Record<string, number> = { apple: 5, pear: 0 };

type Lang = "de" | "en";
const labels: Record<Lang, string> = { de: "Speichern", en: "Save" };
""", """
const stock: { [product: string]: number } = { apple: 5, pear: 0 };

const labels: { de: string; en: string } = {
  de: "Speichern",
  en: "Save",
};
""",
 ("Ein `Record` ist ein Wörterbuch: Links steht ein Stichwort, rechts immer dieselbe Art von Eintrag.",
  ["`Record<string, number>` heißt: Jeder String-Key hat einen Zahlenwert.",
   "Die Index-Signatur `{ [product: string]: number }` beschreibt dasselbe. Der Name `product` ist nur Dokumentation.",
   "Mit einer Union als Key-Typ wie `Record<Lang, string>` müssen alle Keys vorhanden sein. Fehlt `en`, meldet TypeScript einen Fehler.",
   "So vergisst du bei einer neuen Sprache oder einem neuen Status keine Übersetzung."],
  "Annehmen, jeder Key existiere: `stock[\"banana\"]` hat laut TypeScript den Typ `number`, ist zur Laufzeit aber `undefined`. Die Option `noUncheckedIndexedAccess` macht daraus `number | undefined` und erzwingt eine Prüfung.",
  "`Record` ist kürzer und gängiger. Die Index-Signatur brauchst du, wenn das Objekt zusätzlich feste Felder haben soll.",
  "Was passiert, wenn du in `labels` ein Feld `fr` ergänzt, ohne `Lang` zu ändern?",
  "Ein Fehler: `fr` ist kein erlaubter Key, weil `Lang` nur `\"de\"` und `\"en\"` enthält."),
 [("Record", UT+"#recordkeys-type"), ("Index-Signaturen", OB+"#index-signatures"), ("noUncheckedIndexedAccess", CFG+"#noUncheckedIndexedAccess")]),
]))

# ---------------- UNIONS ----------------
SECTIONS.append(("unions", "Unions und Narrowing", "unions", "Das Herzstück von TypeScript: Ein Wert kann mehreres sein, und Prüfungen engen es ein.", [
C("Union Types",
  "Ein Wert kann einer von mehreren Typen sein. Vor der Verwendung engst du ihn per Prüfung ein (Narrowing).",
  """
function formatId(id: string | number) {
  return typeof id === "number" ? id.toFixed(0) : id.toUpperCase();
}
""", """
type Id = string | number;

function formatId(id: Id): string {
  if (typeof id === "number") {
    return id.toFixed(0);     // hier: number
  }
  return id.toUpperCase();    // hier: string
}
""",
 ("Eine Union ist ein Paket mit dem Aufkleber „Buch ODER DVD“. Bevor du es benutzt, schaust du hinein. Danach weißt du genau, was du in der Hand hast.",
  ["Auf `string | number` darfst du nur benutzen, was beide Typen können, z.B. `toString()`.",
   "`typeof id === \"number\"` ist eine Prüfung, die TypeScript versteht.",
   "Im `if`-Zweig ist `id` daher eine `number`, und `toFixed` ist erlaubt.",
   "Nach dem `return` weiß TypeScript: Im Rest der Funktion kann `id` nur noch ein `string` sein."],
  "Direkt `id.toUpperCase()` aufrufen. TypeScript meldet, dass es `toUpperCase` auf `number` nicht gibt. Die Lösung ist eine Prüfung, kein `as string`.",
  "Ternär bei zwei kurzen Fällen. `if` mit frühem `return`, sobald pro Fall mehr passiert. Einen Alias wie `Id`, wenn die Union mehrfach vorkommt.",
  "Welchen Typ hat `id` im `else`-Zweig von `if (typeof id === \"string\")` bei `string | number | boolean`?",
  "`number | boolean`. TypeScript zieht nur den geprüften Typ ab."),
 [("Union Types", EV+"#union-types"), ("typeof Type Guards", NA+"#typeof-type-guards"), ("Type Aliases", EV+"#type-aliases")]),

C("Literal Types statt `enum`",
  "Statt beliebiger Strings nur eine feste Auswahl erlauben. Tippfehler fallen sofort auf.",
  """
type Status = "idle" | "loading" | "success" | "error";

let status: Status = "idle";
""", """
enum Status {
  Idle = "idle",
  Loading = "loading",
  Success = "success",
  Error = "error",
}

let status: Status = Status.Idle;
""",
 ("Ein Literal-Typ ist ein Dropdown statt eines Freitextfelds: Es gibt nur die vorgegebenen Einträge.",
  ["`\"idle\" | \"loading\" | ...` ist eine Union aus konkreten String-Werten.",
   "`status = \"laoding\"` (Tippfehler) wird sofort rot markiert.",
   "Der Editor schlägt beim Tippen die erlaubten Werte vor.",
   "Ein `enum` erzeugt zusätzlich echten JavaScript-Code, ein Objekt `Status`, das zur Laufzeit existiert. Literal-Typen verschwinden beim Kompilieren komplett."],
  "Eine Variable mit `let` ohne Annotation anlegen: `let s = \"idle\"` hat den Typ `string`, nicht `Status`, und passt nicht in eine Funktion, die `Status` erwartet. Mit `const` oder `let s: Status` klappt es.",
  "Literal-Unions sind heute der übliche Weg, weil sie einfach sind und direkt zu JSON-Daten aus der API passen. Enums siehst du in älteren Projekten und manchen Backend-Frameworks.",
  "Darf man einer Funktion mit Parameter `Status` direkt den String `\"success\"` übergeben, wenn `Status` ein String-Enum ist?",
  "Nein. Ein String-Enum erwartet `Status.Success`, ein normaler String wird abgelehnt. Bei der Literal-Union geht `\"success\"` direkt. Das ist ein Grund, warum viele Teams Unions bevorzugen."),
 [("Literal Types", EV+"#literal-types"), ("Enums", H+"enums.html")]),

C("Discriminated Unions",
  "Jede Variante hat ein gemeinsames Feld mit festem Wert. Daran erkennt TypeScript, welche Variante vorliegt.",
  """
type State =
  | { status: "loading" }
  | { status: "error"; message: string }
  | { status: "success"; data: Todo[] };

function render(state: State): string {
  switch (state.status) {
    case "loading": return "Lädt …";
    case "error":   return state.message;
    case "success": return `${state.data.length} Todos`;
  }
}
""", """
interface LoadingState { status: "loading"; }
interface ErrorState   { status: "error"; message: string; }
interface SuccessState { status: "success"; data: Todo[]; }

type State = LoadingState | ErrorState | SuccessState;

function render(state: State): string {
  if (state.status === "loading") {
    return "Lädt …";
  }
  if (state.status === "error") {
    return state.message;
  }
  return state.data.length + " Todos";
}
""",
 ("Wie Pakete mit farbigem Etikett: Rot heißt Fehler, und nur rote Pakete enthalten eine Fehlermeldung. Wer das Etikett liest, weiß genau, was drin ist.",
  ["Jede Variante hat das Feld `status` mit einem anderen festen Wert. Das ist der Diskriminator.",
   "Prüfst du `state.status === \"error\"`, schließt TypeScript alle anderen Varianten aus.",
   "Im Error-Zweig ist `state.message` deshalb erlaubt, im Loading-Zweig nicht.",
   "Widersprüchliche Zustände wie „lädt, hat aber schon Daten“ lassen sich gar nicht erst bauen."],
  "Den Zustand als ein Objekt mit lauter optionalen Feldern modellieren: `{ loading: boolean; error?: string; data?: Todo[] }`. Dann sind widersprüchliche Kombinationen möglich, und du musst überall `?.` schreiben.",
  "Die Kurzform für überschaubare Varianten. Einzelne Interfaces, wenn die Varianten groß sind oder einzeln wiederverwendet werden.",
  "Was passiert, wenn du im `switch` den Fall `\"success\"` vergisst und die Funktion den Rückgabetyp `string` hat?",
  "TypeScript meldet, dass die Funktion nicht in allen Fällen einen `string` zurückgibt. So findest du vergessene Varianten automatisch."),
 [("Discriminated Unions", NA+"#discriminated-unions"), ("Exhaustiveness Checking", NA+"#exhaustiveness-checking")]),

C("Eigene Type Guards",
  "Eigene Prüffunktionen, die TypeScript als Narrowing versteht. Praktisch, wenn dieselbe Prüfung mehrfach vorkommt.",
  """
if ("permissions" in user) {
  showAdminPanel(user.permissions);
}
""", """
function isAdmin(user: User | Admin): user is Admin {
  return "permissions" in user;
}

if (isAdmin(user)) {
  showAdminPanel(user.permissions);
}
""",
 ("Ein Type Guard ist ein Ausweis-Scanner: Er prüft einmal, und danach behandelt jeder die Person entsprechend ihrem Ausweis.",
  ["Der `in`-Operator prüft, ob ein Feld existiert, und TypeScript engt den Typ daraufhin ein.",
   "Lagerst du die Prüfung in eine Funktion mit Rückgabe `boolean` aus, geht dieses Wissen verloren.",
   "Der Rückgabetyp `user is Admin` (Type Predicate) sagt TypeScript: Liefert die Funktion `true`, ist `user` ein `Admin`.",
   "Im `if` danach ist `user.permissions` deshalb erlaubt."],
  "Eine falsche Prüfung schreiben. TypeScript glaubt dem Type Predicate blind: Prüft `isAdmin` das falsche Feld, ist der Typ trotzdem `Admin`, und der Fehler zeigt sich erst zur Laufzeit.",
  "`in` oder `typeof` direkt für einmalige Prüfungen. Ein eigener Type Guard, wenn die Prüfung mehrfach gebraucht wird oder komplexer ist, z.B. für `unknown`-Daten.",
  "Was ändert sich, wenn `isAdmin` nur `: boolean` statt `: user is Admin` zurückgibt?",
  "Die Funktion läuft gleich, aber TypeScript engt den Typ im `if` nicht mehr ein. `user.permissions` wäre dann ein Fehler."),
 [("in-Operator", NA+"#the-in-operator-narrowing"), ("Type Predicates", NA+"#using-type-predicates")]),

C("`null` und `undefined`",
  "Mit `strict` zwingt TypeScript dich, `null` und `undefined` zu behandeln. Das `!` schaltet diese Prüfung an einer Stelle ab.",
  """
const input = document.querySelector<HTMLInputElement>("#email")!;
input.value = "";

const name = user?.name ?? "Gast";
""", """
const input = document.querySelector<HTMLInputElement>("#email");
if (input === null) {
  throw new Error("#email fehlt im HTML");
}
input.value = "";

let name: string;
if (user !== undefined && user.name !== undefined) {
  name = user.name;
} else {
  name = "Gast";
}
""",
 ("`!` ist ein Versprechen an den Compiler: „Da ist ganz sicher etwas.“ Hältst du es nicht, stürzt das Programm zur Laufzeit trotzdem ab.",
  ["`querySelector` gibt `HTMLInputElement | null` zurück, weil das Element fehlen könnte.",
   "Das `!` am Ende (Non-null Assertion) entfernt `null` aus dem Typ, ohne etwas zu prüfen.",
   "Die ausführliche Variante prüft wirklich und wirft einen Fehler mit klarer Meldung.",
   "Nach der Prüfung weiß TypeScript, dass `input` nicht `null` ist."],
  "`!` überall verteilen, um Fehlermeldungen loszuwerden. Dann hast du im Grunde wieder JavaScript ohne Prüfung, und „Cannot read properties of null“ kommt zurück.",
  "`?.` und `??` für Werte, die legitim fehlen dürfen. `!` nur, wenn du es wirklich garantieren kannst. Eine echte Prüfung, wenn ein Fehlen ein Fehler im Programm wäre.",
  "Was ist der Unterschied zwischen `user?.name` und `user!.name`?",
  "`user?.name` prüft zur Laufzeit und ergibt `undefined`, wenn `user` fehlt. `user!.name` prüft nichts und stürzt ab, wenn `user` fehlt. Es beruhigt nur den Compiler."),
 [("null und undefined", EV+"#null-and-undefined"), ("Non-null Assertion (!)", EV+"#non-null-assertion-operator-postfix-"), ("strictNullChecks", CFG+"#strictNullChecks")]),
]))

# ---------------- GENERICS ----------------
SECTIONS.append(("generics", "Generics", "generics", "Platzhalter für Typen. Klingt abstrakt, du benutzt sie aber ständig: Array<T>, Promise<T>, useState<T>.", [
C("Generische Funktionen",
  "Ein Typ-Parameter `<T>` ist ein Platzhalter, den TypeScript bei jedem Aufruf mit dem passenden Typ füllt.",
  """
function first<T>(items: T[]) {
  return items[0];
}

const n = first([1, 2, 3]);    // number
const s = first(["a", "b"]);   // string
""", """
function first<T>(items: T[]): T | undefined {
  return items[0];
}

const n = first<number>([1, 2, 3]);
const s = first<string>(["a", "b"]);
""",
 ("Generics sind wie eine Ausstechform: Die Form bleibt gleich, aber welchen Teig du hineindrückst, entscheidet der Aufrufer. Heraus kommt immer das Material, das hineinging.",
  ["`<T>` deklariert einen Typ-Platzhalter, wie ein Parameter, nur für Typen.",
   "`items: T[]` heißt: ein Array von irgendwas, aber alle Elemente vom selben Typ.",
   "Beim Aufruf mit `[1, 2, 3]` erkennt TypeScript `T = number` und setzt es überall ein.",
   "Dadurch ist der Rückgabetyp `number` statt `any`. Die Information geht nicht verloren."],
  "`any` statt Generics benutzen: `function first(items: any[]): any`. Das funktioniert, aber das Ergebnis ist ungeprüft, und `first([1, 2]).toUpperCase()` fällt nicht mehr auf.",
  "Den Typ meist ableiten lassen. Explizit `<number>` angeben, wenn TypeScript nichts ableiten kann, z.B. bei `useState<User | null>(null)` oder einem leeren Array.",
  "Warum ist `T | undefined` als Rückgabetyp in der ausführlichen Variante ehrlicher?",
  "Weil `items[0]` bei einem leeren Array `undefined` ist. Ohne `| undefined` behauptet der Typ, es komme immer ein `T` zurück."),
 [("Generics", GE), ("Typ-Variablen", GE+"#working-with-generic-type-variables")]),

C("Generic Constraints",
  "Mit `extends` legst du fest, was ein Typ-Parameter mindestens können muss.",
  """
function findById<T extends { id: number }>(items: T[], id: number) {
  return items.find(item => item.id === id);
}
""", """
interface HasId {
  id: number;
}

function findById<T extends HasId>(items: T[], id: number): T | undefined {
  return items.find(function (item: T): boolean {
    return item.id === id;
  });
}
""",
 ("Eine Einschränkung ist wie eine Stellenausschreibung: Bewerben darf sich jeder, aber eine ID ist Pflicht.",
  ["Ohne Einschränkung weiß TypeScript nichts über `T`. `item.id` wäre ein Fehler.",
   "`T extends HasId` heißt: `T` darf jeder Typ sein, der mindestens `id: number` hat.",
   "Darum ist `item.id` in der Funktion erlaubt.",
   "Der Rückgabetyp bleibt trotzdem der genaue Typ: Übergibst du `Todo[]`, kommt `Todo | undefined` zurück und nicht nur `HasId`."],
  "Den Parameter direkt als `HasId[]` typisieren statt generisch. Dann kommt `HasId | undefined` zurück, und `result.title` ist ein Fehler, obwohl es ein Todo war.",
  "Constraints immer dann, wenn deine generische Funktion auf bestimmte Felder zugreift. Typisch für Hilfsfunktionen in Repositories und Services.",
  "Darf man `findById([\"a\", \"b\"], 1)` aufrufen?",
  "Nein. Strings haben kein Feld `id: number`, also erfüllen sie die Einschränkung nicht."),
 [("Generic Constraints", GE+"#generic-constraints")]),

C("Generische Typen",
  "Auch Typen können Platzhalter haben. So beschreibst du eine Hülle einmal und füllst sie mit wechselndem Inhalt.",
  """
type ApiResponse<T> = { data: T; error: string | null };

const res: ApiResponse<User[]> = await getUsers();
""", """
interface ApiResponse<T> {
  data: T;
  error: string | null;
}

type UsersResponse = ApiResponse<User[]>;

const res: UsersResponse = await getUsers();
""",
 ("`ApiResponse<T>` ist ein Versandkarton mit Standardaufdruck (Daten, Fehlerfeld). Was drinliegt, steht auf dem Etikett: `<User[]>` oder `<Todo>`.",
  ["`ApiResponse<T>` definiert die Hülle mit einem Platzhalter `T` für den Inhalt.",
   "`ApiResponse<User[]>` setzt `T = User[]` ein. `data` hat jetzt den Typ `User[]`.",
   "Dieselbe Hülle funktioniert für jeden Endpunkt: `ApiResponse<Todo>`, `ApiResponse<number>` und so weiter.",
   "Du kennst das Muster schon: `Promise<User>` und `Array<string>` sind ebenfalls generische Typen."],
  "Für jeden Endpunkt ein eigenes, fast gleiches Interface anlegen (`UsersResponse`, `TodosResponse` …). Ändert sich das Antwortformat, musst du alle einzeln anpassen.",
  "Ein Alias wie `UsersResponse` lohnt sich, wenn der zusammengesetzte Typ oft vorkommt. Sonst `ApiResponse<User[]>` direkt schreiben.",
  "Welchen Typ hat `res.data[0].name`, wenn `res` vom Typ `ApiResponse<User[]>` ist?",
  "`string`, also der Typ von `User.name`. TypeScript reicht den Typ durch alle Ebenen durch."),
 [("Generische Typen", GE+"#generic-types"), ("Generische Objekttypen", OB+"#generic-object-types")]),
]))

# ---------------- UTILITY ----------------
SECTIONS.append(("utility", "Utility Types", "utility", "Neue Typen aus bestehenden ableiten, statt sie doppelt zu pflegen.", [
C("`Partial` und `Required`",
  "`Partial<T>` macht alle Felder optional. Ideal für PATCH-Requests, bei denen nur ein Teil geändert wird.",
  """
function updateUser(id: number, changes: Partial<User>) { ... }

updateUser(1, { age: 32 });
""", """
interface UserUpdate {
  name?: string;
  age?: number;
  email?: string;
}

function updateUser(id: number, changes: UserUpdate): void { ... }

updateUser(1, { age: 32 });
""",
 ("`Partial` ist ein Änderungsformular, auf dem du nur die Felder ausfüllst, die sich ändern sollen.",
  ["`Partial<User>` erzeugt einen neuen Typ, in dem jedes Feld von `User` ein `?` bekommt.",
   "Das Original-Interface bleibt unverändert.",
   "Kommt in `User` ein neues Feld dazu, ist es automatisch auch in `Partial<User>` enthalten.",
   "Das Gegenstück `Required<T>` entfernt alle `?` und macht jedes Feld zur Pflicht."],
  "Das von Hand geschriebene `UserUpdate` nicht pflegen. Bekommt `User` ein neues Feld `city`, fehlt es in `UserUpdate`, und niemand merkt es. Mit `Partial<User>` kann das nicht passieren.",
  "Fast immer die Utility-Type-Variante. Ein eigenes Interface nur, wenn bewusst nicht alle Felder änderbar sein sollen. Dann aber besser `Partial<Omit<User, \"id\">>`.",
  "Ist `{}` ein gültiger Wert für `Partial<User>`?",
  "Ja, weil alle Felder optional sind. Wenn ein leerer Update-Request nicht erlaubt sein soll, musst du das zusätzlich zur Laufzeit prüfen."),
 [("Partial", UT+"#partialtype"), ("Required", UT+"#requiredtype")]),

C("`Pick` und `Omit`",
  "Aus einem bestehenden Typ Felder herausnehmen (`Omit`) oder nur bestimmte behalten (`Pick`).",
  """
type PublicUser = Omit<User, "password">;
type UserPreview = Pick<User, "id" | "name">;
""", """
interface PublicUser {
  id: number;
  name: string;
  email: string;
}

interface UserPreview {
  id: number;
  name: string;
}
""",
 ("`Pick` ist eine Schere, die nur die markierten Felder ausschneidet. `Omit` ist ein Rotstift, der einzelne Felder durchstreicht.",
  ["Die Feldnamen gibst du als Literal-Union an: `\"id\" | \"name\"`.",
   "`Pick<User, \"id\" | \"name\">` baut einen Typ nur aus diesen Feldern.",
   "`Omit<User, \"password\">` baut einen Typ aus allen Feldern außer `password`.",
   "Beide bleiben mit `User` verbunden. Ändert sich ein Feldtyp in `User`, ändert er sich überall."],
  "Annehmen, `Omit` entferne das Feld auch zur Laufzeit. Typen verschwinden beim Kompilieren: Gibst du im Backend ein komplettes User-Objekt mit Passwort zurück, wird es trotzdem verschickt. Das Feld musst du selbst entfernen, z.B. per Destructuring.",
  "`Omit` für „alles außer sensiblen oder generierten Feldern“, `Pick` für kleine Vorschau-Typen. Ausgeschriebene Interfaces nur, wenn der Typ wirklich eigenständig ist.",
  "Welche Felder hat `Omit<User, \"id\" | \"password\">`, wenn `User` die Felder `id`, `name`, `email` und `password` hat?",
  "`name` und `email`."),
 [("Pick", UT+"#picktype-keys"), ("Omit", UT+"#omittype-keys")]),

C("`keyof` und `typeof`",
  "Typen aus vorhandenen Werten ableiten, statt sie doppelt zu pflegen.",
  """
const ROLES = { admin: "Administrator", user: "Benutzer" } as const;

type Role = keyof typeof ROLES;   // "admin" | "user"
""", """
type Role = "admin" | "user";

const ROLES: Record<Role, string> = {
  admin: "Administrator",
  user: "Benutzer",
};
""",
 ("`typeof` macht vom Objekt eine Blaupause, `keyof` liest daraus die Liste der Feldnamen ab.",
  ["`typeof ROLES` liefert im Typ-Kontext den Typ des Objekts mit all seinen Feldern.",
   "`keyof` davor macht daraus die Union der Keys: `\"admin\" | \"user\"`.",
   "Kommt im Objekt eine Rolle dazu, ist sie automatisch im Typ enthalten.",
   "Die ausführliche Variante geht den umgekehrten Weg: erst der Typ, dann das Objekt, das ihn erfüllen muss."],
  "`typeof` in TypeScript mit `typeof` in JavaScript verwechseln. In einer Bedingung wie `typeof x === \"string\"` ist es der JavaScript-Operator zur Laufzeit. Nach `type X =` ist es der TypeScript-Operator, der einen Typ liefert.",
  "Wert zuerst, wenn das Objekt die Quelle der Wahrheit ist, z.B. bei Konfigurationen. Typ zuerst, wenn der Typ von außen vorgegeben ist, z.B. durch die API oder die Datenbank.",
  "Welchen Typ hat `keyof User`, wenn `User` die Felder `id` und `name` hat?",
  "`\"id\" | \"name\"`."),
 [("keyof", H+"2/keyof-types.html"), ("typeof", H+"2/typeof-types.html")]),
]))

# ---------------- ASYNC & BACKEND ----------------
SECTIONS.append(("backend", "Async, API und Backend", "api", "Wo Frontend und Backend sich treffen und Typen am meisten helfen, aber auch am leichtesten lügen.", [
C("`Promise<T>` als Rückgabetyp",
  "Eine `async`-Funktion gibt immer ein Promise zurück. Der Typ beschreibt, was beim `await` herauskommt.",
  """
async function getUser(id: number) {
  const res = await fetch(`/api/users/${id}`);
  return (await res.json()) as User;
}
""", """
async function getUser(id: number): Promise<User> {
  const res: Response = await fetch("/api/users/" + id);
  if (!res.ok) {
    throw new Error("HTTP " + res.status);
  }
  const user: User = await res.json();
  return user;
}
""",
 ("`Promise<User>` ist ein Abholschein mit Aufdruck: „Hier bekommst du später einen User.“",
  ["`async` macht aus jedem Rückgabewert automatisch ein Promise. Aus `User` wird `Promise<User>`.",
   "`res.json()` liefert `Promise<any>`. TypeScript weiß nicht, was der Server schickt.",
   "Mit `as User` oder der Annotation `const user: User` legst du den Typ fest. Beides ist eine Behauptung, keine Prüfung.",
   "Wer `await getUser(1)` schreibt, bekommt ab dann einen typisierten `User`."],
  "Den Rückgabetyp als `User` statt `Promise<User>` angeben. TypeScript meldet einen Fehler, weil eine `async`-Funktion immer ein Promise zurückgibt.",
  "Expliziter Rückgabetyp `Promise<User>` bei allen API-Funktionen. Er dokumentiert, was der Aufrufer bekommt, und die ausführliche Variante prüft zusätzlich `res.ok`, was die kurze vergisst.",
  "Welchen Typ hat `const u = getUser(1)` ohne `await`?",
  "`Promise<User>`. Erst mit `await` bekommst du den `User` selbst."),
 [("Funktionen, die Promises zurückgeben", EV+"#functions-which-return-promises"), ("Rückgabetypen", EV+"#return-type-annotations")]),

C("Daten von außen prüfen",
  "Typen existieren nur beim Programmieren. Daten von außen müssen zur Laufzeit geprüft werden, sonst lügt der Typ.",
  """
import { z } from "zod";

const UserSchema = z.object({ id: z.number(), name: z.string() });
type User = z.infer<typeof UserSchema>;

const user = UserSchema.parse(await res.json());
""", """
interface User { id: number; name: string; }

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" && value !== null &&
    "id" in value && typeof value.id === "number" &&
    "name" in value && typeof value.name === "string"
  );
}

const data: unknown = await res.json();
if (!isUser(data)) {
  throw new Error("Ungültige Antwort");
}
const user = data; // ab hier: User
""",
 ("TypeScript ist die Gästeliste, die Laufzeitprüfung ist der Türsteher. Eine Liste allein hält niemanden auf, erst der Türsteher kontrolliert wirklich.",
  ["Was vom Server, aus einem Formular oder aus `localStorage` kommt, ist für TypeScript unbekannt.",
   "Die ausführliche Variante prüft jedes Feld von Hand und meldet das Ergebnis per Type Guard.",
   "Zod beschreibt die Form einmal als Schema. `parse` prüft zur Laufzeit und wirft einen Fehler, wenn etwas nicht passt.",
   "`z.infer` leitet den TypeScript-Typ aus dem Schema ab. So gibt es nur eine Quelle der Wahrheit."],
  "Im Backend `req.body as CreateUserDto` schreiben und glauben, die Eingabe sei damit geprüft. Jeder kann beliebiges JSON schicken. Gerade im Backend ist Validierung Pflicht.",
  "Für eine einzelne kleine Prüfung reicht ein Type Guard. Sobald es mehrere Endpunkte gibt, lohnt sich eine Bibliothek wie Zod, im Frontend wie im Backend.",
  "Warum reicht `const user: User = await res.json()` nicht als Prüfung?",
  "Weil `res.json()` `any` liefert und `any` zu jedem Typ passt. TypeScript prüft hier nichts, der Typ ist nur eine Behauptung."),
 [("Type Predicates", NA+"#using-type-predicates"), ("unknown", FN+"#unknown"), ("Zod", "https://zod.dev")]),

C("Typen teilen: DTOs",
  "Frontend und Backend nutzen dieselben Typen. Ändert sich das API-Format, zeigen beide Seiten sofort Fehler.",
  """
// shared/types.ts
export interface User { id: number; name: string; email: string; }
export type CreateUserDto = Omit<User, "id">;

// im Frontend und im Backend
import type { User, CreateUserDto } from "../shared/types";
""", """
// shared/types.ts
export interface User {
  id: number;
  name: string;
  email: string;
}

export interface CreateUserDto {
  name: string;
  email: string;
}

// im Frontend und im Backend
import { type User, type CreateUserDto } from "../shared/types";
""",
 ("Ein gemeinsamer Typ ist ein Vertrag, den beide Seiten unterschreiben. Ändert eine Seite den Vertrag, sieht die andere es sofort.",
  ["Die Typen liegen in einem Ordner, auf den beide Projekte zugreifen, z.B. in einem Monorepo.",
   "Ein DTO (Data Transfer Object) beschreibt, was über die Leitung geht. Beim Anlegen gibt es noch keine `id`, die vergibt die Datenbank.",
   "`Omit<User, \"id\">` leitet das DTO vom User ab, statt die Felder doppelt zu schreiben.",
   "`import type` importiert nur Typen. Der Import verschwindet beim Kompilieren komplett, es landet kein Code im Bundle."],
  "Typen im Frontend einfach abtippen. Benennt das Backend ein Feld um, z.B. `name` in `fullName`, kompiliert das Frontend weiter, zeigt aber `undefined` an.",
  "`Omit` hält das DTO automatisch synchron. Ein ausgeschriebenes DTO ist sinnvoll, wenn sich Eingabe und gespeichertes Objekt bewusst unterscheiden, z.B. Klartext-Passwort beim Registrieren und Hash in der Datenbank.",
  "Warum hat `CreateUserDto` keine `id`?",
  "Weil der Client beim Anlegen noch keine ID kennt. Die vergibt der Server oder die Datenbank."),
 [("Typ-Importe (import type)", H+"2/modules.html#typescript-specific-es-module-syntax"), ("Omit", UT+"#omittype-keys")]),

C("Express-Routen typisieren",
  "Bei Inline-Handlern leitet TypeScript vieles selbst ab. In ausgelagerten Controllern gibst du die Typen an.",
  """
app.get("/users/:id", (req, res) => {
  const user = findUser(Number(req.params.id));
  if (!user) {
    res.status(404).json({ error: "Nicht gefunden" });
    return;
  }
  res.json(user);
});
""", """
import { Request, Response } from "express";

type Params = { id: string };
type Body = User | { error: string };

function getUserHandler(req: Request<Params>, res: Response<Body>): void {
  const user = findUser(Number(req.params.id));
  if (!user) {
    res.status(404).json({ error: "Nicht gefunden" });
    return;
  }
  res.json(user);
}

app.get("/users/:id", getUserHandler);
""",
 ("Die Platzhalter von `Request` und `Response` sind wie beschriftete Ein- und Ausgänge einer Maschine: Was darf hinein (Parameter, Body), was kommt heraus (Antwort).",
  ["Bei einem Inline-Handler leitet TypeScript `req.params.id` aus dem Pfad `\"/users/:id\"` ab. Der Typ ist immer `string`.",
   "Darum `Number(...)` vor der Suche: URL-Parameter sind Text, auch wenn sie wie Zahlen aussehen.",
   "In einem ausgelagerten Handler fehlt der Bezug zur Route. `Request<Params>` gibt die Parameter deshalb ausdrücklich an.",
   "`Request<Params, ResBody, ReqBody>` hat auch Platzhalter für Antwort und Body. Für einen POST-Body schreibst du z.B. `Request<{}, unknown, CreateUserDto>`.",
   "`Response<Body>` sorgt dafür, dass `res.json(...)` nur passende Daten akzeptiert."],
  "Glauben, `Request<{}, unknown, CreateUserDto>` prüfe den Body. Auch hier ist der Typ nur eine Behauptung, der Body muss trotzdem validiert werden (siehe Karte „Daten von außen prüfen“).",
  "Inline reicht für einfache Routen. Explizite Typen, sobald Handler in eigene Dateien (Controller) wandern. Tipp: `res.status(...).json(...)` und danach ein separates `return;` vermeidet Typfehler bei neueren Express-Typen.",
  "Welchen Typ hat `req.params.id` bei der Route `/users/:id`, auch wenn die ID eine Zahl ist?",
  "`string`. Alles aus der URL ist Text. Umwandeln musst du selbst und dabei auf `NaN` prüfen."),
 [("Route-Parameter (Express)", "https://expressjs.com/en/guide/routing.html#route-parameters"), ("Generics", GE)]),
]))

# ---------------- REACT ----------------
SECTIONS.append(("react", "React mit TypeScript", "react", "Die drei Stellen, an denen du in React-Komponenten am häufigsten Typen schreibst.", [
C("Props typisieren",
  "Props sind ein Objekt, also typisierst du sie wie jedes andere Objekt.",
  """
function Button({ label, onClick, variant = "primary" }: {
  label: string;
  onClick: () => void;
  variant?: "primary" | "secondary";
}) {
  return <button className={variant} onClick={onClick}>{label}</button>;
}
""", """
interface ButtonProps {
  label: string;
  onClick: () => void;
  variant?: "primary" | "secondary";
}

function Button(props: ButtonProps) {
  const variant = props.variant ?? "primary";
  return (
    <button className={variant} onClick={props.onClick}>
      {props.label}
    </button>
  );
}
""",
 ("Das Props-Interface ist die Bedienungsanleitung der Komponente: Darin steht, was man einstecken muss und was optional ist.",
  ["Eine Komponente bekommt genau einen Parameter: das Props-Objekt.",
   "Die Typ-Annotation steht hinter dem ganzen Destructuring-Muster, nicht hinter einzelnen Props.",
   "Optionale Props bekommen ein `?`. Ein Default im Destructuring liefert den Standardwert.",
   "Wer `<Button />` ohne `label` benutzt, bekommt sofort einen Fehler im Editor."],
  "Typen direkt ins Destructuring schreiben: `({ label: string })`. Das ist JavaScript-Syntax fürs Umbenennen und erzeugt eine Variable namens `string`. Der Typ gehört hinter die Klammer: `({ label }: { label: string })`.",
  "Inline bei sehr kleinen Komponenten. Ein benanntes Interface wie `ButtonProps`, sobald es mehr als zwei, drei Props sind oder andere Komponenten die Props weiterreichen.",
  "Wie typisierst du die Prop `children`?",
  "Mit `children: React.ReactNode`. Das erlaubt Text, Elemente, Listen und `null`."),
 [("React mit TypeScript"+" (EN)", RT+"#typescript-with-react-components"), ("children typisieren (EN)", RT+"#typing-children")]),

C("`useState` typisieren",
  "Bei eindeutigen Startwerten leitet React den Typ ab. Startet der State leer, musst du ihn angeben.",
  """
const [count, setCount] = useState(0);              // number
const [user, setUser] = useState<User | null>(null);
""", """
const [count, setCount] = useState<number>(0);

type MaybeUser = User | null;
const [user, setUser] = useState<MaybeUser>(null);
""",
 ("Der Startwert ist das erste Teil in einer Kiste. Liegt eine Zahl drin, weiß jeder: Hier kommen Zahlen rein. Ist die Kiste leer, musst du draufschreiben, was hineingehört.",
  ["`useState(0)` erkennt `number` aus dem Startwert. `setCount(\"a\")` wäre ein Fehler.",
   "`useState(null)` würde nur den Typ `null` ableiten, und `setUser(user)` wäre später verboten.",
   "Mit `useState<User | null>(null)` sagst du: Startet als `null`, darf später ein `User` sein.",
   "Vor der Benutzung musst du darum `null` ausschließen, z.B. mit `if (!user) return ...`."],
  "`useState([])` für eine Liste. Das leere Array wird als `never[]` erkannt, und `setTodos([todo])` schlägt fehl. Richtig ist `useState<Todo[]>([])`.",
  "Typ ableiten lassen, wenn der Startwert ihn eindeutig zeigt. Explizit bei `null`, leeren Arrays und Unions wie `useState<Status>(\"idle\")`.",
  "Welchen Typ hat `status` bei `const [status, setStatus] = useState(\"idle\")`?",
  "`string`, nicht `\"idle\"`. Willst du nur bestimmte Werte erlauben, brauchst du `useState<Status>(\"idle\")`."),
 [("useState typisieren (EN)", RT+"#typing-usestate"), ("useState-Referenz (EN)", "https://react.dev/reference/react/useState")]),

C("Events typisieren",
  "Inline-Handler bekommen ihren Typ automatisch. Lagerst du den Handler aus, musst du den Event-Typ angeben.",
  """
<input onChange={e => setName(e.target.value)} />

<form onSubmit={e => { e.preventDefault(); save(); }}>
""", """
function handleChange(event: React.ChangeEvent<HTMLInputElement>): void {
  setName(event.target.value);
}

function handleSubmit(event: React.FormEvent<HTMLFormElement>): void {
  event.preventDefault();
  save();
}

<input onChange={handleChange} />
<form onSubmit={handleSubmit}>
""",
 ("Ein Inline-Handler steht direkt am Gerät und weiß, woher das Signal kommt. Ein ausgelagerter Handler sitzt in einem anderen Raum und braucht einen Zettel, von welchem Gerät die Nachricht stammt.",
  ["Im JSX weiß TypeScript, dass `onChange` an einem `<input>` hängt, und gibt `e` den passenden Typ.",
   "In einer eigenen Funktion fehlt dieser Zusammenhang. Ohne Annotation wäre `event` `any`.",
   "`React.ChangeEvent<HTMLInputElement>` heißt: ein Change-Event von einem Input-Element.",
   "Darum kennt `event.target` die Eigenschaft `value`."],
  "Den nativen DOM-Typ `Event` statt des React-Typs benutzen. React übergibt eigene Event-Objekte, und `event.target.value` ist bei `Event` nicht bekannt.",
  "Inline für Einzeiler, ausgelagert, sobald der Handler mehr tut. Tipp: Fahr im Editor mit der Maus über `e` im Inline-Handler. Dort steht der exakte Typ, den du kopieren kannst.",
  "Welchen Event-Typ braucht ein `onChange` an einem `<select>`?",
  "`React.ChangeEvent<HTMLSelectElement>`. In den spitzen Klammern steht immer das Element, an dem der Handler hängt."),
 [("DOM-Events typisieren (EN)", RT+"#typing-dom-events")]),
]))
