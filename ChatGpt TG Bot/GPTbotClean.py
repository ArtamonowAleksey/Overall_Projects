from openai import OpenAI
import telebot
from telebot import types
import re
import datetime as dt
import json


# Параметры подключения к Телеграм

TG_token = '8111486366:AAFaGuUpUM0M5QIcroMDqNh6EExP_8EulRk'
bot = telebot.TeleBot(TG_token)

# Параметры подключения к ChatGPT

openai_token = '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'

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_token
)

hi_message = "Привет.\n" \
             "Я ChatGPT"


# Стартовое сообщение бота.

@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, hi_message)


@bot.message_handler(content_types=['text'])
def get_text_message(message):

    
    if message.content_type == 'text':
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.text }]
    )
      
        bot.send_message(message.from_user.id, response.choices[0].message.content.strip())


bot.polling(none_stop=True, interval=5)