from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict

class BackgroundType(Enum):
    ACOLYTE = "Послушник"
    CHARLATAN = "Плут"
    CRIMINAL = "Преступник"
    ENTERTAINER = "Артист"
    FOLK_HERO = "Народный герой"
    GUILD_ARTISAN = "Цеховой ремесленник"
    HERMIT = "Отшельник"
    NOBLE = "Дворянин"
    OUTLANDER = "Чужеземец"
    SAGE = "Мудрец"
    SAILOR = "Моряк"
    SOLDIER = "Солдат"
    URCHIN = "Беспризорник"

@dataclass
class Background:
    """
    Класс для предыстории персонажа
    """
    name: BackgroundType
    skill_proficiencies: List[str] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)
    equipment: List[str] = field(default_factory=list)
    feature: Dict[str, str] = field(default_factory=dict)
    personality_traits: List[str] = field(default_factory=list)
    ideals: List[str] = field(default_factory=list)
    bonds: List[str] = field(default_factory=list)
    flaws: List[str] = field(default_factory=list)

def create_background(background_type: BackgroundType) -> Background:
    """
    Фабрика для создания предысторий
    """
    background_configs = {
        BackgroundType.ACOLYTE: {
            'skill_proficiencies': ['Insight', 'Religion'],
            'languages': ['Two of your choice'],
            'equipment': ['Holy symbol', 'Prayer book', 'Incense', 'Vestments'],
            'feature': {
                'shelter_of_the_faithful': 'Получение помощи от религиозной организации'
            },
            'personality_traits': [
                'Я идеалистично предан своему божеству',
                'Я стараюсь помочь нуждающимся'
            ]
        },
        BackgroundType.CRIMINAL: {
            'skill_proficiencies': ['Deception', 'Stealth'],
            'equipment': ['Crowbar', 'Dark clothes', 'Thieves\' tools'],
            'feature': {
                'criminal_contact': 'Связи в преступном мире'
            }
        }
        # Можно добавить другие предыстории
    }
    
    config = background_configs.get(background_type, {})
    return Background(
        name=background_type,
        skill_proficiencies=config.get('skill_proficiencies', []),
        languages=config.get('languages', []),
        equipment=config.get('equipment', []),
        feature=config.get('feature', {}),
        personality_traits=config.get('personality_traits', [])
    )
