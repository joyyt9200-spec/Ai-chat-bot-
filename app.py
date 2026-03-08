import telebot
import openai
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_KEY

@bot.message_handler(func=lambda m: True)
def chat(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":message.text}]
    )
    bot.reply_to(message, response.choices[0].message.content)

bot.infinity_polling()
