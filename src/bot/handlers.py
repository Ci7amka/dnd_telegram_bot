import telebot
import os
import random
from dotenv import load_dotenv
from telebot.types import Message, CallbackQuery

from src.core.dice_roller import DiceRoller
from src.core.character_generator import CharacterGenerator
from src.database.sqlite_db import CharacterDatabase
from src.bot.keyboards import CharacterKeyboards

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

db = CharacterDatabase()
user_states = {}
user_characters = {}

# Состояния для создания персонажа
CHARACTER_CREATION_STATES = {
    'waiting_for_name': 'name',
    'waiting_for_race': 'race',
    'waiting_for_class': 'class'
}

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    user_id = message.from_user.id
    bot.reply_to(
        message, 
        "Привет! Я бот для D&D. Выбери действие:", 
        reply_markup=CharacterKeyboards.main_menu()
    )
    # Очистка предыдущих состояний
    if user_id in user_states:
        del user_states[user_id]
    if user_id in user_characters:
        del user_characters[user_id]

@bot.message_handler(func=lambda m: m.text == "🎲 Бросок кубика")
def dice_roll_handler(message: Message):
    bot.reply_to(
        message, 
        "Выберите тип кубика:", 
        reply_markup=CharacterKeyboards.dice_selection()
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('dice_'))
def dice_type_selection(call: CallbackQuery):
    dice_type = call.data.split('_')[1]
    bot.edit_message_text(
        f"Выбран кубик {dice_type}. Сколько бросков?", 
        call.message.chat.id, 
        call.message.message_id,
        reply_markup=CharacterKeyboards.dice_count()
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('count_'))
def dice_count_selection(call: CallbackQuery):
    count = call.data.split('_')[1]
    dice_type = call.message.text.split()[-2]
    bot.edit_message_text(
        f"Выбрано {count} кубиков {dice_type}. Модификатор:", 
        call.message.chat.id, 
        call.message.message_id,
        reply_markup=CharacterKeyboards.modifier_selection()
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('mod_'))
def final_dice_roll(call: CallbackQuery):
    modifier = int(call.data.split('_')[1])
    dice_info = call.message.text.split()
    count = int(dice_info[1])
    dice_type = dice_info[3]

    # Выполнение броска
    notation = f"{count}{dice_type}"
    if modifier > 0:
        notation += f"+{modifier}"
    
    result = DiceRoller.roll(notation)
    
    response = (
        f"🎲 Бросок {notation}:\n"
        f"Броски: {result['rolls']}\n"
        f"Модификатор: +{result['modifier']}\n"
        f"Итого: {result['total']}"
    )
    
    bot.edit_message_text(
        response, 
        call.message.chat.id, 
        call.message.message_id,
        reply_markup=CharacterKeyboards.main_menu()
    )
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda m: m.text == "🧙 Создать персонажа")
def start_character_creation(message: Message):
    user_id = message.from_user.id
    bot.reply_to(
        message, 
        "Создание персонажа. Выберите шаг:", 
        reply_markup=CharacterKeyboards.character_creation_steps()
    )

@bot.callback_query_handler(func=lambda call: call.data == 'gen_stats')
def generate_character_stats(call: CallbackQuery):
    user_id = call.from_user.id
    ability_scores = DiceRoller.roll_ability_scores()
    
    # Сохраняем характеристики во временном состоянии
    if user_id not in user_characters:
        user_characters[user_id] = {}
    
    user_characters[user_id]['ability_scores'] = {
        'Сила': ability_scores[0],
        'Ловкость': ability_scores[1],
        'Телосложение': ability_scores[2],
        'Интеллект': ability_scores[3],
        'Мудрость': ability_scores[4],
        'Харизма': ability_scores[5]
    }

    response = "Сгенерированы характеристики:\n" + "\n".join([
        f"{stat}: {value}" for stat, value in user_characters[user_id]['ability_scores'].items()
    ])

    bot.edit_message_text(
        response, 
        call.message.chat.id, 
        call.message.message_id,
        reply_markup=CharacterKeyboards.character_creation_steps()
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data == 'choose_name')
def choose_character_name(call: CallbackQuery):
    user_id = call.from_user.id
    
    # Предлагаем случайное имя
    suggested_name = CharacterGenerator.generate_name()
    
    bot.edit_message_text(
        f"Предлагаемое имя: {suggested_name}\n"
        "Отправьте своё имя или оставьте это как есть.", 
        call.message.chat.id, 
        call.message.message_id
    )
    
    # Устанавливаем состояние ожидания имени
    user_states[user_id] = CHARACTER_CREATION_STATES['waiting_for_name']
    user_characters[user_id]['name'] = suggested_name
    
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda m: user_states.get(m.from_user.id) == 'name')
def save_character_name(message: Message):
    user_id = message.from_user.id
    user_characters[user_id]['name'] = message.text or user_characters[user_id]['name']
    
    del user_states[user_id]
    
    bot.reply_to(
        message, 
        f"Имя сохранено: {user_characters[user_id]['name']}", 
        reply_markup=CharacterKeyboards.character_creation_steps()
    )

# Остальные методы остаются прежними...

def start_bot():
    print("🤖 D&D Бот запущен!")
    bot.polling(none_stop=True)
