---
title: "Lade-, Fehler- und Daten-Zustand"
description: "Jeder Request hat drei mögliche Ausgänge, und das UI sollte alle drei zeigen."
code:
  short: |-
    useEffect(() => {
      fetch("/api/todos")
        .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(setData)
        .catch(setError)
        .finally(() => setLoading(false));
    }, []);

    if (loading) return <Spinner />;
    if (error) return <p>Fehler: {error.message}</p>;
    return <TodoList todos={data} />;
  long: |-
    useEffect(function () {
      async function loadTodos() {
        try {
          const response = await fetch("/api/todos");
          if (response.ok === false) {
            throw new Error("HTTP " + response.status);
          }
          const todos = await response.json();
          setData(todos);
        } catch (err) {
          setError(err);
        } finally {
          setLoading(false);
        }
      }
      loadTodos();
    }, []);

    if (loading) {
      return <Spinner />;
    }
    if (error) {
      return <p>Fehler: {error.message}</p>;
    }
    return <TodoList todos={data} />;
lang:
  short: "jsx"
  long: "jsx"
explain:
  picture: "Jeder Request ist wie eine Bestellung: Sie ist unterwegs (Laden), sie ist schiefgegangen (Fehler) oder sie ist angekommen (Daten). Das UI braucht für jeden dieser drei Zustände eine eigene Ansicht."
  steps:
    - "Startzustand: `loading` ist `true`, es gibt keine Daten und keinen Fehler."
    - "`useEffect` mit leerem Abhängigkeits-Array `[]` startet den Request einmal nach dem ersten Render."
    - "Bei Erfolg landen die Daten per `setData` im State, bei einem Fehler per `setError`."
    - "`finally` setzt `loading` in beiden Fällen auf `false`."
    - "Die frühen `return`s beim Rendern sind Guard Clauses: erst Laden, dann Fehler, dann der Normalfall."
  mistake: "Die Effect-Funktion selbst `async` machen, also `useEffect(async () => ...)`. React erwartet als Rückgabe eine Cleanup-Funktion, kein Promise. Deshalb gibt es die innere `async function loadTodos()`."
  when: "Bei mehreren Schritten ist die `async/await`-Variante lesbarer. In größeren Projekten übernehmen Bibliotheken wie TanStack Query genau dieses Muster für dich."
  question: "Was passiert, wenn du `if (loading) return <Spinner />` weglässt und direkt `data.map(...)` renderst?"
  answer: "Beim ersten Render ist `data` noch `null`, und `data.map` wirft einen TypeError. Deshalb muss der Ladezustand zuerst abgefangen werden."
links:
  - text: "useEffect (EN)"
    url: "https://react.dev/reference/react/useEffect"
  - text: "Daten laden mit Effects (EN)"
    url: "https://react.dev/reference/react/useEffect#fetching-data-with-effects"
  - text: "try...catch...finally"
    url: "https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/try...catch"
---
