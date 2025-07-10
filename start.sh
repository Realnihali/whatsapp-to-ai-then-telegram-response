#!/bin/bash
# install playwright chromium for python if needed
python -m playwright install chromium

# run Python bridge in background
python whatsapp_bridge.py &

# run Node WhatsApp layer
cd js_bridge && npm install && npm start
