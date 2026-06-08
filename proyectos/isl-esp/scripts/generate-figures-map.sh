#!/usr/bin/env bash
# Genera figures-map.json escaneando Figures/Chapter*/png/
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/generate-figures-map.py
