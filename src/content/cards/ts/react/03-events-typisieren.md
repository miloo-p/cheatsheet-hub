---
title: "Events typisieren"
description: "Inline-Handler bekommen ihren Typ automatisch. Lagerst du den Handler aus, musst du den Event-Typ angeben."
code:
  short: |-
    <input onChange={e => setName(e.target.value)} />

    <form onSubmit={e => { e.preventDefault(); save(); }}>
  long: |-
    function handleChange(event: React.ChangeEvent<HTMLInputElement>): void {
      setName(event.target.value);
    }

    function handleSubmit(event: React.FormEvent<HTMLFormElement>): void {
      event.preventDefault();
      save();
    }

    <input onChange={handleChange} />
    <form onSubmit={handleSubmit}>
lang:
  short: "tsx"
  long: "tsx"
explain:
  picture: "Ein Inline-Handler steht direkt am Gerät und weiß, woher das Signal kommt. Ein ausgelagerter Handler sitzt in einem anderen Raum und braucht einen Zettel, von welchem Gerät die Nachricht stammt."
  steps:
    - "Im JSX weiß TypeScript, dass `onChange` an einem `<input>` hängt, und gibt `e` den passenden Typ."
    - "In einer eigenen Funktion fehlt dieser Zusammenhang. Ohne Annotation wäre `event` `any`."
    - "`React.ChangeEvent<HTMLInputElement>` heißt: ein Change-Event von einem Input-Element."
    - "Darum kennt `event.target` die Eigenschaft `value`."
  mistake: "Den nativen DOM-Typ `Event` statt des React-Typs benutzen. React übergibt eigene Event-Objekte, und `event.target.value` ist bei `Event` nicht bekannt."
  when: "Inline für Einzeiler, ausgelagert, sobald der Handler mehr tut. Tipp: Fahr im Editor mit der Maus über `e` im Inline-Handler. Dort steht der exakte Typ, den du kopieren kannst."
  question: "Welchen Event-Typ braucht ein `onChange` an einem `<select>`?"
  answer: "`React.ChangeEvent<HTMLSelectElement>`. In den spitzen Klammern steht immer das Element, an dem der Handler hängt."
links:
  - text: "DOM-Events typisieren (EN)"
    url: "https://react.dev/learn/typescript#typing-dom-events"
---
