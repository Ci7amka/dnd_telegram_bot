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
    
    def handle_class_selection(self, message):
        """Обработка выбора класса"""
        try:
            character_class = next(
                c for c in ClassType if c.value == message.text
            )
            
            # Генерация клавиатуры предысторий
            markup = types.ReplyKeyboardMarkup(row_width=2)
            for background in BackgroundType:
                markup.add(types.KeyboardButton(background.value))
            
            self.bot.send_message(
                message.chat.id, 
                f"Вы выбрали класс: {character_class.value}. Выберите предысторию:", 
                reply_markup=markup
            )
            
            # Обновление состояния
            self.user_states[message.from_user.id]['step'] = 'background_selection'
            self.user_states[message.from_user.id]['character_data']['class'] = character_class
        
        except StopIteration:
            self.bot.send_message(
                message.chat.id, 
                "❌ Некорректный выбор класса. Попробуйте снова."
            )
    
    def handle_background_selection(self, message):
        """Финализация создания персонажа"""
        try:
            background = next(
                b for b in BackgroundType if b.value == message.text
            )
            
            user_state = self.user_states.get(message.from_user.id, {})
            character_data = user_state.get('character_data', {})
            
            # Создание персонажа
            character = CharacterGenerator.generate_character(
                name=message.from_user.first_name,
                race=character_data.get('race'),
                character_class=character_data.get('class'),
                background=background
            )
            
            # Формирование детального описания
            response = self.format_character_description(character)
            
            self.bot.send_message(
                message.chat.id, 
                response
            )
            
            # Очистка состояния
            del self.user_states[message.from_user.id]
        
        except StopIteration:
            self.bot.send_message(
                message.chat.id, 
                "❌ Некорректный выбор предыстории. Попробуйте снова."
            )
    
    def format_character_description(self, character):
        """Форматирование описания персонажа"""
        return (
            f"🎉 Персонаж создан!\n\n"
            f"Имя: {character.name}\n"
            f"Раса: {character.race.name.value}\n"
            f"Класс: {character.character_class.name.value}\n"
            f"Предыстория: {character.background.name.value}\n\n"
            "Характеристики:\n"
            # Добавьте логику вывода характеристик
        )
