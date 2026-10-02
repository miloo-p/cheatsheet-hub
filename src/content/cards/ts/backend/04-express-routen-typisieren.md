---
title: "Express-Routen typisieren"
description: "Bei Inline-Handlern leitet TypeScript vieles selbst ab. In ausgelagerten Controllern gibst du die Typen an."
code:
  short: |-
    app.get("/users/:id", (req, res) => {
      const user = findUser(Number(req.params.id));
      if (!user) {
        res.status(404).json({ error: "Nicht gefunden" });
        return;
      }
      res.json(user);
    });
  long: |-
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
explain:
  picture: "Die Platzhalter von `Request` und `Response` sind wie beschriftete Ein- und Ausgänge einer Maschine: Was darf hinein (Parameter, Body), was kommt heraus (Antwort)."
  steps:
    - "Bei einem Inline-Handler leitet TypeScript `req.params.id` aus dem Pfad `\"/users/:id\"` ab. Der Typ ist immer `string`."
    - "Darum `Number(...)` vor der Suche: URL-Parameter sind Text, auch wenn sie wie Zahlen aussehen."
    - "In einem ausgelagerten Handler fehlt der Bezug zur Route. `Request<Params>` gibt die Parameter deshalb ausdrücklich an."
    - "`Request<Params, ResBody, ReqBody>` hat auch Platzhalter für Antwort und Body. Für einen POST-Body schreibst du z.B. `Request<{}, unknown, CreateUserDto>`."
    - "`Response<Body>` sorgt dafür, dass `res.json(...)` nur passende Daten akzeptiert."
  mistake: "Glauben, `Request<{}, unknown, CreateUserDto>` prüfe den Body. Auch hier ist der Typ nur eine Behauptung, der Body muss trotzdem validiert werden (siehe Karte „Daten von außen prüfen“)."
  when: "Inline reicht für einfache Routen. Explizite Typen, sobald Handler in eigene Dateien (Controller) wandern. Tipp: `res.status(...).json(...)` und danach ein separates `return;` vermeidet Typfehler bei neueren Express-Typen."
  question: "Welchen Typ hat `req.params.id` bei der Route `/users/:id`, auch wenn die ID eine Zahl ist?"
  answer: "`string`. Alles aus der URL ist Text. Umwandeln musst du selbst und dabei auf `NaN` prüfen."
links:
  - text: "Route-Parameter (Express)"
    url: "https://expressjs.com/en/guide/routing.html#route-parameters"
  - text: "Generics"
    url: "https://www.typescriptlang.org/docs/handbook/2/generics.html"
---
