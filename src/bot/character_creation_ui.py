import telebot
from telebot import types
from src.core.character.races import RaceType
from src.core.character.classes import ClassType
from src.core.character.backgrounds import BackgroundType
from src.core.character.generator import CharacterGenerator

class CharacterCreationUI:
    def __init__(self, bot):
        self.bot = bot
        self.user_states = {}
    
    def start_character_creation(self, message):
        """Начало создания персонажа"""
        markup = types.ReplyKeyboardMarkup(row_width=2)
        
        # Динамическая генерация кнопок рас
        for race in RaceType:
            markup.add(types.KeyboardButton(race.value))
        
        self.bot.send_message(
            message.chat.id, 
            "🎲 Выберите расу вашего персонажа:", 
            reply_markup=markup
        )
        
        # Сохранение состояния пользователя
        self.user_states[message.from_user.id] = {
            'step': 'race_selection',
            'character_data': {}
        }
    
    def handle_race_selection(self, message):
        """Обработка выбора расы"""
        try:
            race = next(r for r in RaceType if r.value == message.text)
            
            # Генерация клавиатуры классов
            markup = types.ReplyKeyboardMarkup(row_width=2)
            for char_class in ClassType:
                markup.add(types.KeyboardButton(char_class.value))
            
            self.bot.send_message(
                message.chat.id, 
                f"Вы выбрали расу: {race.value}. Теперь выберите класс:", 
                reply_markup=markup
            )
            
            # Обновление состояния
            self.user_states[message.from_user.id]['step'] = 'class_selection'
            self.user_states[message.from_user.id]['character_data']['race'] = race
        
        except StopIteration:
            self.bot.send_message(
                message.chat.id, 
                "❌ Некорректный выбор расы. Попробуйте снова."
            )
    
    # Другие методы аналогичны
