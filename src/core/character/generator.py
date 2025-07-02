from typing import Optional
from .races import Race, RaceType, create_race
from .classes import CharacterClass, ClassType, create_character_class
from .backgrounds import Background, BackgroundType, create_background

class CharacterGenerator:
    def __init__(self):
        self.race: Optional[Race] = None
        self.character_class: Optional[CharacterClass] = None
        self.background: Optional[Background] = None
    
    def set_race(self, race_type: RaceType):
        """Установка расы персонажа"""
        self.race = create_race(race_type)
    
    def set_class(self, class_type: ClassType):
        """Установка класса персонажа"""
        self.character_class = create_character_class(class_type)
    
    def set_background(self, background_type: BackgroundType):
        """Установка предыстории персонажа"""
        self.background = create_background(background_type)
    
    def generate_character(self, 
                           race_type: RaceType, 
                           class_type: ClassType, 
                           background_type: BackgroundType):
        """
        Полная генерация персонажа
        """
        self.set_race(race_type)
        self.set_class(class_type)
        self.set_background(background_type)
        
        # Здесь можно добавить логику генерации характеристик
        return {
            'race': self.race,
            'class': self.character_class,
            'background': self.background
        }
