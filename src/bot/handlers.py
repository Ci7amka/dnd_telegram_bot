import telebot
import os
from dotenv import load_dotenv
from telebot.types import Message

from src.core.dice_roller import DiceRoller
from src.core.character_generator import CharacterGenerator
from src.database.sqlite_db import CharacterDatabase
from src.bot.keyboards import CharacterKeyboards

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

db = CharacterDatabase()
user_characters = {}

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.reply_to(
        message, 
        "Привет! Я бот для D&D. Выбери действие:", 
        reply_markup=CharacterKeyboards.main_menu()
    )

@bot.message_handler(func=lambda m: m.text == "🎲 Бросок кубика")
def dice_roll_handler(message: Message):
    bot.reply_to(message, "Какой бросок? (Например, 2d6+3)")

@bot.message_handler(func=lambda m: 'd' in m.text.lower())
def process_dice_roll(message: Message):
    try:
        result = DiceRoller.roll(message.text)
        response = (
            f"🎲 Бросок {result['notation']}:\n"
            f"Броски: {result['rolls']}\n"
            f"Модификатор: {result['modifier']}\n"
            f"Итого: {result['total']}"
        )
        bot.reply_to(message, response)
    except ValueError as e:
        bot.reply_to(message, str(e))

@bot.message_handler(func=lambda m: m.text == "🧙 Создать персонажа")
def create_character(message: Message):
    ability_scores = DiceRoller.roll_ability_scores()
    character = CharacterGenerator.generate_character(ability_scores)
    
    user_characters[message.from_user.id] = character
    db.save_character(message.from_user.id, character)

    response = (
        f"📜 Создан персонаж:\n"
        f"Имя: {character['name']}\n"
        f"Раса: {character['race']}\n"
        f"Класс: {character['class']}\n"
        f"Уровень: {character['level']}"
    )
    bot.reply_to(
        message, 
        response, 
        reply_markup=CharacterKeyboards.character_actions()
    )

@bot.message_handler(func=lambda m: m.text == "📊 Характеристики")
def show_character_stats(message: Message):
    character = user_characters.get(message.from_user.id)
    if not character:
        character = db.load_character(message.from_user.id)

    if character:
        stats = "\n".join([
            f"{stat}: {value}" 
            for stat, value in character['ability_scores'].items()
        ])
        bot.reply_to(message, f"🧬 Характеристики:\n{stats}")
    else:
        bot.reply_to(message, "Сначала создайте персонажа!")

@bot.message_handler(func=lambda m: m.text == "🎒 Инвентарь")
def show_inventory(message: Message):
    character = user_characters.get(message.from_user.id)
    if not character:
        character = db.load_character(message.from_user.id)

    if character:
        inventory = character.get('inventory', [])
        if inventory:
            inv_list = "\n".join(inventory)
            bot.reply_to(message, f"🎒 Инвентарь:\n{inv_list}")
        else:
            bot.reply_to(message, "Инвентарь пуст!")
    else:
        bot.reply_to(message, "Сначала создайте персонажа!")

@bot.message_handler(func=lambda m: m.text == "➕ Добавить предмет")
def add_inventory_item(message: Message):
    bot.reply_to(message, "Введите название предмета:")
    bot.register_next_step_handler(message, process_item_addition)

def process_item_addition(message: Message):
    character = user_characters.get(message.from_user.id)
    if not character:
        character = db.load_character(message.from_user.id)

    if character:
        item = message.text
        if 'inventory' not in character:
            character['inventory'] = []
        character['inventory'].append(item)
        
        user_characters[message.from_user.id] = character
        db.save_character(message.from_user.id, character)
        
        bot.reply_to(
            message, 
            f"✅ Предмет '{item}' добавлен в инвентарь!", 
            reply_markup=CharacterKeyboards.character_actions()
        )
    else:
        bot.reply_to(message, "Сначала создайте персонажа!")

def start_bot():
    print("🤖 D&D Бот запущен!")
    bot.polling(none_stop=True)
