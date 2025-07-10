import telebot
from flask import Flask
from threading import Thread

# Telegram config
bot_token = "8096816657:AAEIGLl_DoC08As3bW8d8lZjqPDtA-TJXtc"
chat_id = "1786564127"
bot = telebot.TeleBot(bot_token)

# Sample reply to test
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(chat_id, "🤖 Bot is live and working!")

# Flask app to keep Railway service alive
app = Flask('')

@app.route('/')
def home():
    return "Bot is running"

def run():
    app.run(host='0.0.0.0', port=8080)

# Run Flask + Bot in threads
def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
bot.polling(non_stop=True)
