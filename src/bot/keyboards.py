from telebot import types

def create_start_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎲 Бросок кубика")
    btn2 = types.KeyboardButton("🧙 Создать персонажа")
    markup.add(btn1, btn2)
    return markup
