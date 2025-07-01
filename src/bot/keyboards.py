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
    def modifier_selection():
        markup = types.InlineKeyboardMarkup()
        modifiers = [0, 1, 2, 3, 4, 5]
        row = []
        for mod in modifiers:
            row.append(types.InlineKeyboardButton(f"+{mod}", callback_data=f'mod_{mod}'))
            if len(row) == 3:
                markup.row(*row)
                row = []
        if row:
            markup.row(*row)
        return markup

    @staticmethod
    def character_creation_steps():
        markup = types.InlineKeyboardMarkup()
        steps = [
            ("🎲 Сгенерировать характеристики", "gen_stats"),
            ("📝 Выбрать имя", "choose_name"),
            ("🏰 Выбрать расу", "choose_race"),
            ("⚔️ Выбрать класс", "choose_class"),
            ("✅ Завершить создание", "finish_character")
        ]
        for text, callback in steps:
            markup.add(types.InlineKeyboardButton(text, callback_data=callback))
        return markup

    @staticmethod
    def character_actions(character=None):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("📊 Характеристики"),
            types.KeyboardButton("🎒 Инвентарь")
        )
        markup.add(
            types.KeyboardButton("➕ Добавить предмет"),
            types.KeyboardButton("🔄 Изменить персонажа")
        )
        return markup
