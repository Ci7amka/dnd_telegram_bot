import os
from dotenv import load_dotenv
from src.database.database import DatabaseManager
from src.bot.handlers import start_bot

def main():
    # Загрузка переменных окружения
    load_dotenv()
    
    # Инициализация базы данных
    db_manager = DatabaseManager()
    db_manager.init_models()
    
    # Запуск бота
    start_bot()

if __name__ == "__main__":
    main()
