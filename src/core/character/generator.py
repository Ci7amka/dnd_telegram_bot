from typing import Optional
from .races import Race, RaceType, SubRace
from .classes import CharacterClass, ClassType
from .backgrounds import Background, BackgroundType

class CharacterGenerator:
    @classmethod
    def generate_character(
        cls, 
        name: str, 
        race: RaceType, 
        subrace: Optional[SubRace] = None,
        character_class: Optional[ClassType] = None,
        background: Optional[BackgroundType] = None
    ):
        """
        Полностью автоматизированный генератор персонажа
        
        Args:
            name (str): Имя персонажа
            race (RaceType): Раса персонажа
            subrace (Optional[SubRace]): Подраса
            character_class (Optional[ClassType]): Класс персонажа
            background (Optional[BackgroundType]): Предыстория
        
        Returns:
            Character: Сгенерированный персонаж
        """
        # Создание компонентов персонажа
        character_race = Race(
            name=race, 
            subrace=subrace
        )
        
        character_class = CharacterClass.get_class_details(
            character_class
        ) if character_class else None
        
        character_background = Background.get_background_details(
            background
        ) if background else None
        
        # Создание персонажа с расширенной логикой
        character = Character(
            name=name,
            race=character_race,
            character_class=character_class,
            background=character_background
        )
        
        # Автоматическая генерация характеристик
        character.generate_ability_scores()
        
        return character
