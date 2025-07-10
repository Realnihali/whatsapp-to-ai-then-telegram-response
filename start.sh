#!/usr/bin/env bash
set -e
python -m playwright install chromium      # Python layer browser
python whatsapp_bridge.py &                # run your Python bot
cd js_bridge && node index.js              # run Node/WhatsApp layer
