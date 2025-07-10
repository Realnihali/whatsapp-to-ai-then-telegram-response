#!/usr/bin/env bash
python -m playwright install chromium      # Python deps
python whatsapp_bridge.py &                # start Python AI layer
cd js_bridge && node index.js              # start Node WhatsApp layer
