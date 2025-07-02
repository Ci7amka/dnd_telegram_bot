import telebot
from telebot import types
from src.core.character.races import RaceType, SubRace
from src.core.character.classes import ClassType
from src.core.character.backgrounds import BackgroundType
from src.core.character.generator import CharacterGenerator

class CharacterCreationUI:
    def __init__(self, bot):
        self.bot = bot
        self.user_states = {}
    
    def start_creation_wizard(self, message):
        """Начало пошагового создания персонажа"""
        steps = [
            self.select_race,
            self.select_subrace,
            self.select_class,
            self.select_background,
            self.distribute_ability_scores,
            self.finalize_character
        ]
        
        # Инициализация состояния пользователя
        self.user_states[message.chat.id] = {
            'step': 0,
            'character_data': {}
        }
        
        # Первый шаг - выбор расы
        steps[0](message)
    
    def select_race(self, message):
        """Выбор расы персонажа"""
        markup = types.ReplyKeyboardMarkup(row_width=2)
        for race in RaceType:
            markup.add(types.KeyboardButton(race.value))
        
        self.bot.send_message(
            message.chat.id, 
            "Выберите расу вашего персонажа:", 
            reply_markup=markup
        )
    
    # Реализуйте остальные методы аналогично
