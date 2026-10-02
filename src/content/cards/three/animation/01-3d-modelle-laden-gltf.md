---
title: "3D-Modelle laden: GLTF"
description: "GLTF bzw. GLB ist das Standardformat fürs Web, quasi das JPG für 3D. Blender exportiert es direkt."
code:
  short: |-
    import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

    const loader = new GLTFLoader();
    const gltf = await loader.loadAsync("/models/robot.glb");

    scene.add(gltf.scene);

    // enthaltene Animationen abspielen
    const mixer = new THREE.AnimationMixer(gltf.scene);
    mixer.clipAction(gltf.animations[0]).play();
    // im Loop: mixer.update(delta);
explain:
  picture: "Eine GLB-Datei ist ein Umzugskarton mit allem drin: Formen, Materialien, Texturen, Knochen und Animationen. Der Loader packt ihn aus und stellt alles fertig in die Szene."
  steps:
    - "`.gltf` ist ein JSON mit separaten Dateien für Texturen und Daten, `.glb` packt alles in eine einzige Binärdatei. Fürs Web ist `.glb` meist praktischer."
    - "`loadAsync` gibt ein Promise zurück und funktioniert mit `await`."
    - "`gltf.scene` ist eine Gruppe mit dem ganzen Modell, die du direkt in deine Szene hängst."
    - "Animationen aus Blender stecken in `gltf.animations`. Der `AnimationMixer` spielt sie ab und braucht in jedem Bild `mixer.update(delta)`."
    - "Große Modelle lassen sich mit Draco oder Meshopt komprimieren. Dafür gibt es passende Decoder für den Loader."
  mistake: "Die Datei mit einem relativen Pfad laden, der im Build nicht mehr stimmt. In Vite gehören Modelle in den Ordner `public/` und werden mit `/models/…` geladen. Und: Riesige, unkomprimierte Modelle ausliefern. Ein 50-MB-Modell ist auf dem Handy eine Minute Ladezeit."
  when: "GLB für alles, was aus einem 3D-Programm kommt. Eingebaute Geometrien nur für einfache Formen und Prototypen. Prüfen und optimieren kannst du Modelle vorab im Browser-Tool gltf.report."
  question: "Warum gibt es zu dieser Karte keine Live-Demo?"
  answer: "Weil die Spickzettel-Seite aus Sicherheitsgründen keine externen Dateien nachladen darf. Ein Modell müsste von einem fremden Server kommen. In deinem eigenen Projekt funktioniert der Code genau so."
links:
  - text: "Load a .GLTF (Manual)"
    url: "https://threejs.org/manual/#en/load-gltf"
  - text: "GLTFLoader"
    url: "https://threejs.org/docs/#GLTFLoader"
  - text: "AnimationMixer"
    url: "https://threejs.org/docs/#AnimationMixer"
  - text: "gltf.report (EN)"
    url: "https://gltf.report/"
---
