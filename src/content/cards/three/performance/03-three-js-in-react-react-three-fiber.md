---
title: "Three.js in React: React Three Fiber"
description: "React Three Fiber beschreibt Szenen als JSX-Komponenten. Darunter läuft ganz normales Three.js."
labels:
  - "React Three Fiber"
  - "Vanilla Three.js"
code:
  short: |-
    import { Canvas, useFrame } from "@react-three/fiber";
    import { OrbitControls } from "@react-three/drei";
    import { useRef } from "react";

    function Box() {
      const ref = useRef();
      useFrame((state, delta) => { ref.current.rotation.y += delta; });
      return (
        <mesh ref={ref}>
          <boxGeometry args={[1, 1, 1]} />
          <meshStandardMaterial color="hotpink" />
        </mesh>
      );
    }

    export default function App() {
      return (
        <Canvas camera={{ position: [0, 0, 4] }}>
          <ambientLight intensity={0.5} />
          <directionalLight position={[3, 3, 3]} />
          <Box />
          <OrbitControls />
        </Canvas>
      );
    }
  long: |-
    import * as THREE from "three";
    import { OrbitControls } from "three/addons/controls/OrbitControls.js";

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.1, 100);
    camera.position.z = 4;
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(innerWidth, innerHeight);
    document.body.appendChild(renderer.domElement);

    scene.add(new THREE.AmbientLight(0xffffff, 0.5));
    const light = new THREE.DirectionalLight(0xffffff);
    light.position.set(3, 3, 3);
    scene.add(light);

    const box = new THREE.Mesh(
      new THREE.BoxGeometry(1, 1, 1),
      new THREE.MeshStandardMaterial({ color: "hotpink" })
    );
    scene.add(box);
    const controls = new OrbitControls(camera, renderer.domElement);

    const timer = new THREE.Timer();
    renderer.setAnimationLoop((t) => {
      timer.update(t);
      box.rotation.y += timer.getDelta();
      renderer.render(scene, camera);
    });
    // + Resize und Aufräumen von Hand
lang:
  short: "jsx"
explain:
  picture: "React Three Fiber ist eine Übersetzung: Jedes JSX-Element entspricht einer Three.js-Klasse. `<mesh>` wird zu `new THREE.Mesh()`, `<boxGeometry args={[1, 1, 1]}>` zu `new THREE.BoxGeometry(1, 1, 1)`."
  steps:
    - "`<Canvas>` erzeugt Szene, Kamera, Renderer und Render-Schleife und kümmert sich um Resize und Pixeldichte."
    - "Elementnamen sind die Klassennamen in camelCase. `args` sind die Konstruktor-Parameter, andere Props werden als Eigenschaften gesetzt, z.B. `position={[1, 0, 0]}`."
    - "`useFrame` läuft in jedem Bild und bekommt die Delta-Zeit. Dort gehören laufende Animationen hin, nicht in `useState`, denn ein Re-Render pro Bild wäre viel zu langsam."
    - "Beim Unmount räumt Fiber Geometrien und Materialien automatisch auf."
    - "Die Bibliothek `@react-three/drei` liefert fertige Helfer wie OrbitControls, Umgebungslicht oder einen GLTF-Hook."
  mistake: "Animationen über React-State steuern, z.B. `setRotation(r => r + 0.01)` in jedem Bild. Das löst 60 Re-Renders pro Sekunde aus. Werte im `useFrame` direkt über `ref.current` ändern."
  when: "React Three Fiber, wenn dein Projekt ohnehin React ist und die 3D-Szene mit dem Rest der App zusammenspielen soll. Vanilla Three.js für eigenständige Szenen und um zu verstehen, was darunter passiert. Die Konzepte dieses Zettels gelten in beiden Fällen."
  question: "Wie schreibst du `new THREE.SphereGeometry(1, 32, 16)` in React Three Fiber?"
  answer: "`<sphereGeometry args={[1, 32, 16]} />` innerhalb eines `<mesh>`."
links:
  - text: "React Three Fiber (EN)"
    url: "https://r3f.docs.pmnd.rs/getting-started/introduction"
  - text: "drei (EN)"
    url: "https://drei.docs.pmnd.rs/"
---
