import os
import sys
import logging
from dotenv import load_dotenv
import telebot

# Локальные импорты
from src.bot.character_creation_ui import CharacterCreationUI
from src.database.models import init_database
from src.core.character.races import RaceType
from src.core.character.classes import ClassType

# Настройка логирования
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

def main():
    try:
        # Инициализация базы данных
        db_session = init_database()
        
        # Получение токена бота из переменных окружения
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        if not bot_token:
            raise ValueError("Токен Telegram бота не найден!")
        
        # Инициализация бота
        bot = telebot.TeleBot(bot_token)
        
        # Создание UI для работы с персонажами
        character_ui = CharacterCreationUI(bot)
        
        logger.info("🤖 Бот D&D запущен!")
        bot.polling(none_stop=True)
        
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}")

if __name__ == '__main__':
    main()
