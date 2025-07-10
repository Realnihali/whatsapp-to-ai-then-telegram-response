import asyncio
from telethon import TelegramClient
from pywhatkit.core import core, log
from pywhatkit.whats import sendwhatmsg_instantly
from datetime import datetime
import os

TELEGRAM_API_ID = 123456  # Replace with your Telegram API ID
TELEGRAM_API_HASH = 'your_api_hash'  # Replace with your Telegram API hash
TELEGRAM_BOT_TOKEN = '8096816657:AAEIGLl_DoC08As3bW8d8lZjqPDtA-TJXtc'
TELEGRAM_CHAT_ID = 1786564127

WHATSAPP_CONTACT = '+919876543210'  # Replace with AI contact number

from telethon.sync import TelegramClient

client = TelegramClient('session', TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def main():
    await client.start(bot_token=TELEGRAM_BOT_TOKEN)
    await client.send_message(TELEGRAM_CHAT_ID, "🤖 Bridge Started. Awaiting messages...")

    @client.on(events.NewMessage)
    async def handler(event):
        if event.is_private:
            msg = event.raw_text.strip()
            try:
                sendwhatmsg_instantly(WHATSAPP_CONTACT, msg, wait_time=10, tab_close=True)
                await event.respond("✅ Sent to WhatsApp.")
            except Exception as e:
                await event.respond(f"❌ Error: {str(e)}")

    print("Bot running...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
