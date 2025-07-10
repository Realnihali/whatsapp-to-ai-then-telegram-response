#!/usr/bin/env bash
set -e
python -m playwright install-deps          # <‑‑ install all missing libs
python -m playwright install chromium      # ensure browser cache
python whatsapp_bridge.py &                # python layer
cd js_bridge && node index.js              # node layer
python -m playwright install-deps chromium firefox
