from openai import OpenAI
import telebot
from telebot import types
import configparser

#Чтение файла конфигурации

config = configparser.ConfigParser()
config.read('/Users/aleksey.artamonov/Notebooks/Overall_Projects/ChatGpt_TG_Bot/ChatGPT_TG_Docker/config.ini')


# Параметры подключения к Телеграм

TG_token = config.get('Settings', 'tg_token')
bot = telebot.TeleBot(TG_token)

# Параметры подключения к ChatGPT

openai_token = config.get('Settings', 'openai_token')

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
    else:
        bot.send_message(message.from_user.id, "Я умею только в текст")

bot.polling(none_stop=True, interval=5)