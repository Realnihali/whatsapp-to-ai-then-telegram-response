# index.py
from pyrogram import Client
import asyncio
import os

API_ID = 12345678  # Replace with your actual Telegram API ID
API_HASH = "your_api_hash"
BOT_TOKEN = "8096816657:AAEIGLl_DoC08As3bW8d8lZjqPDtA-TJXtc"
CHAT_ID = 1786564127

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message()
async def handler(client, message):
    await app.send_message(CHAT_ID, f"📩 New message: {message.text}")

app.run()
