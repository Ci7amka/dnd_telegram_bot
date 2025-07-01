import os
import telebot
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Получение токена
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Создание бота
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я D&D бот для ролевых игр!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

def start_bot():
    print("Бот запущен!")
    bot.polling(none_stop=True)
