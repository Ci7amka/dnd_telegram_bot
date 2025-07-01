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
    def dice_selection():
        markup = types.InlineKeyboardMarkup()
        dice_types = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20']
        row = []
        for dice in dice_types:
            row.append(types.InlineKeyboardButton(dice, callback_data=f'dice_{dice}'))
            if len(row) == 3:
                markup.row(*row)
                row = []
        if row:
            markup.row(*row)
        return markup

    @staticmethod
    def dice_count():
        markup = types.InlineKeyboardMarkup()
        counts = [1, 2, 3, 4, 5]
        row = []
        for count in counts:
            row.append(types.InlineKeyboardButton(str(count), callback_data=f'count_{count}'))
            if len(row) == 3:
                markup.row(*row)
                row = []
        if row:
            markup.row(*row)
        return markup

    @staticmethod
    def character_actions():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("📊 Характеристики"),
            types.KeyboardButton("🎒 Инвентарь")
        )
        markup.add(
            types.KeyboardButton("➕ Добавить предмет"),
            types.KeyboardButton("🔙 Главное меню")
        )
        return markup
