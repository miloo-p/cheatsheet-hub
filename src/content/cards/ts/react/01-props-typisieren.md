---
title: "Props typisieren"
description: "Props sind ein Objekt, also typisierst du sie wie jedes andere Objekt."
code:
  short: |-
    function Button({ label, onClick, variant = "primary" }: {
      label: string;
      onClick: () => void;
      variant?: "primary" | "secondary";
    }) {
      return <button className={variant} onClick={onClick}>{label}</button>;
    }
  long: |-
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
lang:
  short: "tsx"
  long: "tsx"
explain:
  picture: "Das Props-Interface ist die Bedienungsanleitung der Komponente: Darin steht, was man einstecken muss und was optional ist."
  steps:
    - "Eine Komponente bekommt genau einen Parameter: das Props-Objekt."
    - "Die Typ-Annotation steht hinter dem ganzen Destructuring-Muster, nicht hinter einzelnen Props."
    - "Optionale Props bekommen ein `?`. Ein Default im Destructuring liefert den Standardwert."
    - "Wer `<Button />` ohne `label` benutzt, bekommt sofort einen Fehler im Editor."
  mistake: "Typen direkt ins Destructuring schreiben: `({ label: string })`. Das ist JavaScript-Syntax fürs Umbenennen und erzeugt eine Variable namens `string`. Der Typ gehört hinter die Klammer: `({ label }: { label: string })`."
  when: "Inline bei sehr kleinen Komponenten. Ein benanntes Interface wie `ButtonProps`, sobald es mehr als zwei, drei Props sind oder andere Komponenten die Props weiterreichen."
  question: "Wie typisierst du die Prop `children`?"
  answer: "Mit `children: React.ReactNode`. Das erlaubt Text, Elemente, Listen und `null`."
links:
  - text: "React mit TypeScript (EN)"
    url: "https://react.dev/learn/typescript#typescript-with-react-components"
  - text: "children typisieren (EN)"
    url: "https://react.dev/learn/typescript#typing-children"
---
