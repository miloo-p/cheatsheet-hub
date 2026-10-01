#!/usr/bin/env bash
# Baut alle Einzelseiten und daraus die gemeinsame Website in ../site
set -euo pipefail
cd "$(dirname "$0")"
python3 build_core.py     # HTML, CSS, TypeScript
python3 build_gsap.py
python3 build_three.py
python3 build_cro.py
python3 sitegen.py
rm -rf ../site && cp -r site ../site && rm -rf site
echo "Fertig: ../site"
