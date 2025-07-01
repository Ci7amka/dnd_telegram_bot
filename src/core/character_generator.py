import random

class CharacterGenerator:
    RACES = ['Человек', 'Эльф', 'Дварф', 'Полурослик', 'Полуорк']
    CLASSES = ['Воин', 'Маг', 'Жрец', 'Разбойник', 'Паладин']

    @classmethod
    def generate_character(cls, ability_scores):
        return {
            'name': cls.generate_name(),
            'race': random.choice(cls.RACES),
            'class': random.choice(cls.CLASSES),
            'level': 1,
            'ability_scores': {
                'Сила': ability_scores[0],
                'Ловкость': ability_scores[1],
                'Телосложение': ability_scores[2],
                'Интеллект': ability_scores[3],
                'Мудрость': ability_scores[4],
                'Харизма': ability_scores[5]
            },
            'hp': 10,
            'inventory': []
        }

    @staticmethod
    def generate_name():
        first_names = ['Арагорн', 'Леголас', 'Гимли', 'Фродо', 'Сэм']
        last_names = ['Странник', 'Лучник', 'Топорщик', 'Хранитель', 'Садовод']
        return f"{random.choice(first_names)} {random.choice(last_names)}"
 @classmethod  
    def generate_name(cls):  
        first_names = [  
            'Арагорн', 'Леголас', 'Гимли',   
            'Фродо', 'Сэм', 'Гэндальф'  
        ]  
        last_names = [  
            'Странник', 'Лучник', 'Топорщик',   
            'Хранитель', 'Садовод', 'Мудрый'  
        ]  
        return f"{random.choice(first_names)} {random.choice(last_names)}"  