import os
import telebot
from dotenv import load_dotenv
import sys  
import os  
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
# Импорт основных модулей
from src.bot.character_creation_ui import CharacterCreationUI
from src.core.character.races import RaceType
from src.core.character.classes import ClassType
from src.core.character.backgrounds import BackgroundType
from src.database.models import init_database

# Загрузка переменных окружения
load_dotenv()

# Инициализация базы данных
init_database()

# Создание бота
bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

# Инициализация UI создания персонажа
character_ui = CharacterCreationUI(bot)

# Обработчики команд
@bot.message_handler(commands=['start'])
def start_message(message):
    """Стартовое сообщение и начало создания персонажа"""
    bot.send_message(
        message.chat.id, 
        "Добро пожаловать в мир Dungeons & Dragons! 🎲🐉\n"
        "Создадим вашего уникального героя?"
    )
    character_ui.start_character_creation(message)

@bot.message_handler(commands=['help'])
def help_command(message):
    """Справочная информация"""
    help_text = (
        "🎮 Доступные команды:\n"
        "/start - Начать создание персонажа\n"
        "/help - Показать справку\n"
        "/character - Просмотр текущего персонажа\n"
        "/adventure - Начать приключение"
    )
    bot.send_message(message.chat.id, help_text)

# Обработчики выбора расы
@bot.message_handler(func=lambda message: message.text in [race.value for race in RaceType])
def handle_race_selection(message):
    character_ui.handle_race_selection(message)

# Обработчики выбора класса
@bot.message_handler(func=lambda message: message.text in [char_class.value for char_class in ClassType])
def handle_class_selection(message):
    character_ui.handle_class_selection(message)

# Обработчики выбора предыстории
@bot.message_handler(func=lambda message: message.text in [background.value for background in BackgroundType])
def handle_background_selection(message):
    character_ui.handle_background_selection(message)

# Дополнительные обработчики
@bot.message_handler(commands=['character'])
def show_character(message):
    """Показать текущего персонажа"""
    character_ui.display_current_character(message)

@bot.message_handler(commands=['adventure'])
def start_adventure(message):
    """Начать приключение"""
    character_ui.prepare_adventure(message)

# Обработка неизвестных команд
@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    bot.reply_to(
        message, 
        "🤔 Извините, я не понял вашу команду. "
        "Используйте /help для списка доступных команд."
    )

# Настройки бота и запуск
def main():
    try:
        print("🐉 D&D Telegram Bot запущен!")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")

if __name__ == '__main__':
    main()
