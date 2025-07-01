import os
import telebot
import random
from dotenv import load_dotenv

from src.core.dice_roller import DiceRoller
from src.core.character_generator import CharacterGenerator
from src.database.database import CharacterDatabase
from src.bot.keyboards import CharacterKeyboards

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

db = CharacterDatabase()
user_characters = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, 
        "Привет! Я бот для D&D. Выбери действие:", 
        reply_markup=CharacterKeyboards.main_menu()
    )

@bot.message_handler(func=lambda m: m.text == "🎲 Бросок кубика")
def dice_roll_handler(message):
    bot.reply_to(
        message, 
        "Выберите тип кубика:", 
        reply_markup=CharacterKeyboards.dice_selection()
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('dice_'))
def dice_type_selection(call):
    dice_type = call.data.split('_')[1]
    bot.edit_message_text(
        f"Выбран кубик {dice_type}. Сколько бросков?", 
        call.message.chat.id, 
        call.message.message_id,
        reply_markup=CharacterKeyboards.dice_count()
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('count_'))
def final_dice_roll(call):
    count = call.data.split('_')[1]
    dice_type = call.message.text.split()[2]
    
    notation = f"{count}{dice_type}"
    result = DiceRoller.roll(notation)
    
    response = (
        f"🎲 Бросок {notation}:\n"
        f"Броски: {result['rolls']}\n"
        f"Итого: {result['total']}"
    )
    
    bot.edit_message_text(
        response, 
        call.message.chat.id, 
        call.message.message_id,
        reply_markup=CharacterKeyboards.main_menu()
    )

@bot.message_handler(func=lambda m: m.text == "🧙 Создать персонажа")
def create_character(message):
    ability_scores = DiceRoller.roll_ability_scores()
    character = CharacterGenerator.generate_character(ability_scores)
    
    user_characters[message.from_user.id] = character
    db.save_character(message.from_user.id, character)

    response = (
        f"📜 Создан персонаж:\n"
        f"Имя: {character['name']}\n"
        f"Раса: {character['race']}\n"
        f"Класс: {character['class']}"
    )
    bot.reply_to(
        message, 
        response, 
        reply_markup=CharacterKeyboards.character_actions()
    )

@bot.message_handler(func=lambda m: m.text == "📊 Характеристики")
def show_character_stats(message):
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
def show_inventory(message):
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
def add_inventory_item(message):
    bot.reply_to(message, "Введите название предмета:")
    bot.register_next_step_handler(message, process_item_addition)

def process_item_addition(message):
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

@bot.message_handler(func=lambda m: m.text == "🔙 Главное меню")
def return_to_main_menu(message):
    bot.reply_to(
        message, 
        "Возврат в главное меню:", 
        reply_markup=CharacterKeyboards.main_menu()
    )

def start_bot():
    print("🤖 D&D Бот запущен!")
    bot.polling(none_stop=True)
