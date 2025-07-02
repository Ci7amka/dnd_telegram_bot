from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional

class RaceType(Enum):
    HUMAN = "Человек"
    ELF = "Эльф"
    DWARF = "Дварф"
    HALFLING = "Полурослик"
    GNOME = "Гном"
    HALF_ELF = "Полуэльф"
    HALF_ORC = "Полуорк"
    DRAGONBORN = "Драконорожденный"
    TIEFLING = "Тифлинг"

@dataclass
class Race:
    """
    Расширенный класс для рас персонажей D&D
    """
    name: RaceType
    ability_score_increase: Dict[str, int] = field(default_factory=dict)
    age_range: tuple = (18, 80)
    alignment: str = "Нейтральный"
    size: str = "Средний"
    speed: int = 30
    languages: List[str] = field(default_factory=list)
    traits: Dict[str, str] = field(default_factory=dict)
    subraces: List[str] = field(default_factory=list)

def create_race(race_type: RaceType) -> Race:
    """
    Фабрика для создания рас с полной конфигурацией
    """
    race_configs = {
        RaceType.HUMAN: {
            'ability_score_increase': {
                'strength': 1, 'dexterity': 1, 'constitution': 1, 
                'intelligence': 1, 'wisdom': 1, 'charisma': 1
            },
            'age_range': (18, 80),
            'languages': ['Общий'],
            'traits': {
                'versatility': 'Бонус ко всем характеристикам'
            }
        },
        RaceType.ELF: {
            'ability_score_increase': {'dexterity': 2},
            'age_range': (100, 750),
            'languages': ['Общий', 'Эльфийский'],
            'traits': {
                'darkvision': 'Видение в темноте',
                'fey_ancestry': 'Преимущество против магического сна'
            },
            'subraces': ['Высший эльф', 'Лесной эльф', 'Темный эльф']
        },
        # Можно добавить другие расы
    }
    
    config = race_configs.get(race_type, {})
    return Race(
        name=race_type,
        ability_score_increase=config.get('ability_score_increase', {}),
        age_range=config.get('age_range', (18, 80)),
        languages=config.get('languages', []),
        traits=config.get('traits', {}),
        subraces=config.get('subraces', [])
    )

# Вспомогательные функции
def get_all_races() -> List[Race]:
    """
    Возвращает список всех рас
    """
    return [create_race(race_type) for race_type in RaceType]

def get_race_by_name(name: str) -> Optional[Race]:
    """
    Получение расы по имени
    """
    try:
        race_type = RaceType(name)
        return create_race(race_type)
    except ValueError:
        return None
