from telebot import types

class CharacterKeyboards:
    @staticmethod
    def main_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("🎲 Бросок кубика"),
            types.KeyboardButton("🧙 Создать персонажа")
        )
        return markup

    @staticmethod
    def character_actions():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("📊 Характеристики"),
            types.KeyboardButton("🎒 Инвентарь"),
            types.KeyboardButton("➕ Добавить предмет")
        )
        return markup
