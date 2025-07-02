# src/core/character/races.py
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, List

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
    Базовый класс для рас персонажей D&D
    """
    name: RaceType
    subraces: Optional[List['SubRace']] = None
    
    # Базовые характеристики расы
    ability_score_increase: dict = None
    age: tuple = None
    alignment: str = None
    size: str = None
    speed: int = 30
    
    def __post_init__(self):
        if self.ability_score_increase is None:
            self.ability_score_increase = {}
        
        if self.subraces is None:
            self.subraces = []

class SubRace:
    """
    Подраса с дополнительными характеристиками
    """
    def __init__(self, name: str, parent_race: RaceType):
        self.name = name
        self.parent_race = parent_race

# Примеры создания рас
def create_human_race() -> Race:
    return Race(
        name=RaceType.HUMAN,
        ability_score_increase={
            "strength": 1,
            "dexterity": 1,
            "constitution": 1,
            "intelligence": 1,
            "wisdom": 1,
            "charisma": 1
        },
        age=(18, 80),
        alignment="Любой",
        size="Средний"
    )

def create_elf_race() -> Race:
    return Race(
        name=RaceType.ELF,
        subraces=[
            SubRace("Высший эльф", RaceType.ELF),
            SubRace("Лесной эльф", RaceType.ELF),
            SubRace("Темный эльф", RaceType.ELF)
        ],
        ability_score_increase={"dexterity": 2},
        age=(100, 750),
        alignment="Нейтрально-хаотичный",
        size="Средний"
    )

# Фабрика для создания рас
def race_factory(race_type: RaceType) -> Race:
    race_creators = {
        RaceType.HUMAN: create_human_race,
        RaceType.ELF: create_elf_race,
        # Добавьте другие расы
    }
    
    creator = race_creators.get(race_type)
    if creator:
        return creator()
    
    raise ValueError(f"Раса {race_type} не поддерживается")
