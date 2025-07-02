from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Dict

class RaceType(Enum):
    # Основные расы из Книги Игрока
    HUMAN = "Человек"
    ELF = "Эльф"
    DWARF = "Гном"
    HALFLING = "Полурослик"
    DRAGONBORN = "Драконорожденный"
    GNOME = "Гном"
    HALF_ELF = "Полуэльф"
    HALF_ORC = "Полуорк"
    TIEFLING = "Тифлинг"

class SubRace(Enum):
    # Подрасы с уникальными бонусами
    HIGH_ELF = "Высший эльф"
    WOOD_ELF = "Лесной эльф"
    HILL_DWARF = "Холмовой гном"
    MOUNTAIN_DWARF = "Горный гном"
    LIGHTFOOT_HALFLING = "Легконогий полурослик"
    STOUT_HALFLING = "Коренастый полурослик"

@dataclass
class Race:
    name: RaceType
    subrace: SubRace = None
    
    # Расовые бонусы
    ability_bonuses: Dict[str, int] = None
    
    # Расовые особенности
    traits: List[str] = None
    
    def __post_init__(self):
        # Базовые бонусы для рас
        default_bonuses = {
            RaceType.HUMAN: {
                'strength': 1, 'dexterity': 1, 
                'constitution': 1, 'intelligence': 1, 
                'wisdom': 1, 'charisma': 1
            },
            RaceType.ELF: {'dexterity': 2},
            RaceType.DWARF: {'constitution': 2},
            RaceType.HALFLING: {'dexterity': 2}
        }
        
        if not self.ability_bonuses:
            self.ability_bonuses = default_bonuses.get(
                self.name, {}
            )
        
        # Базовые особенности
        default_traits = {
            RaceType.ELF: [
                "Ночное зрение",
                "Иммунитет к магическому сну",
                "Преимущество против очарования"
            ],
            RaceType.DWARF: [
                "Сопротивление яду",
                "Владение боевыми топорами",
                "Каменная живучесть"
            ]
        }
        
        if not self.traits:
            self.traits = default_traits.get(
                self.name, []
            )
