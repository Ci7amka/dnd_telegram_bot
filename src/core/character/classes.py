from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class ClassType(Enum):
    # Классы из Книги Игрока
    BARBARIAN = "Варвар"
    BARD = "Бард"
    CLERIC = "Жрец"
    DRUID = "Друид"
    FIGHTER = "Воин"
    MONK = "Монах"
    PALADIN = "Паладин"
    RANGER = "Следопыт"
    ROGUE = "Плут"
    SORCERER = "Чародей"
    WARLOCK = "Колдун"
    WIZARD = "Волшебник"

@dataclass
class CharacterClass:
    name: ClassType
    hit_die: int  # Кость хитов
    primary_abilities: List[str]
    saving_throws: List[str]
    
    # Начальные владения
    armor_proficiencies: List[str] = None
    weapon_proficiencies: List[str] = None
    tool_proficiencies: List[str] = None
    
    def calculate_hp(self, level: int) -> int:
        """Расчет хитов по уровням"""
        base_hp = self.hit_die
        for _ in range(1, level):
            base_hp += (self.hit_die // 2 + 1)
        return base_hp
    
    @classmethod
    def get_class_details(cls, class_type: ClassType):
        """Детали классов"""
        details = {
            ClassType.FIGHTER: {
                'hit_die': 10,
                'primary_abilities': ['strength', 'constitution'],
                'saving_throws': ['strength', 'constitution'],
                'armor_proficiencies': ['all', 'shields'],
                'weapon_proficiencies': ['simple', 'martial']
            },
            # Другие классы...
        }
        
        class_info = details.get(class_type, {})
        return cls(name=class_type, **class_info)
