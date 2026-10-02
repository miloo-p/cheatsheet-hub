---
title: "Literal Types statt `enum`"
description: "Statt beliebiger Strings nur eine feste Auswahl erlauben. Tippfehler fallen sofort auf."
code:
  short: |-
    type Status = "idle" | "loading" | "success" | "error";

    let status: Status = "idle";
  long: |-
    enum Status {
      Idle = "idle",
      Loading = "loading",
      Success = "success",
      Error = "error",
    }

    let status: Status = Status.Idle;
explain:
  picture: "Ein Literal-Typ ist ein Dropdown statt eines Freitextfelds: Es gibt nur die vorgegebenen Einträge."
  steps:
    - "`\"idle\" | \"loading\" | ...` ist eine Union aus konkreten String-Werten."
    - "`status = \"laoding\"` (Tippfehler) wird sofort rot markiert."
    - "Der Editor schlägt beim Tippen die erlaubten Werte vor."
    - "Ein `enum` erzeugt zusätzlich echten JavaScript-Code, ein Objekt `Status`, das zur Laufzeit existiert. Literal-Typen verschwinden beim Kompilieren komplett."
  mistake: "Eine Variable mit `let` ohne Annotation anlegen: `let s = \"idle\"` hat den Typ `string`, nicht `Status`, und passt nicht in eine Funktion, die `Status` erwartet. Mit `const` oder `let s: Status` klappt es."
  when: "Literal-Unions sind heute der übliche Weg, weil sie einfach sind und direkt zu JSON-Daten aus der API passen. Enums siehst du in älteren Projekten und manchen Backend-Frameworks."
  question: "Darf man einer Funktion mit Parameter `Status` direkt den String `\"success\"` übergeben, wenn `Status` ein String-Enum ist?"
  answer: "Nein. Ein String-Enum erwartet `Status.Success`, ein normaler String wird abgelehnt. Bei der Literal-Union geht `\"success\"` direkt. Das ist ein Grund, warum viele Teams Unions bevorzugen."
links:
  - text: "Literal Types"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-types"
  - text: "Enums"
    url: "https://www.typescriptlang.org/docs/handbook/enums.html"
---
