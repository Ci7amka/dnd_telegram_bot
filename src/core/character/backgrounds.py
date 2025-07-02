from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class BackgroundType(Enum):
    ACOLYTE = "Послушник"
    CHARLATAN = "Плут"
    CRIMINAL = "Преступник"
    ENTERTAINER = "Артист"
    FOLK_HERO = "Народный герой"
    GUILD_ARTISAN = "Ремесленник гильдии"
    HERMIT = "Отшельник"
    NOBLE = "Дворянин"
    SAGE = "Мудрец"
    SAILOR = "Моряк"
    SOLDIER = "Солдат"
    URCHIN = "Беспризорник"

@dataclass
class Background:
    name: BackgroundType
    skill_proficiencies: List[str]
    tool_proficiencies: List[str] = None
    languages: List[str] = None
    equipment: List[Dict] = None
    feature: str = None
    
    @classmethod
    def get_background_details(cls, background_type: BackgroundType):
        """Детали предысторий"""
        details = {
            BackgroundType.ACOLYTE: {
                'skill_proficiencies': ['insight', 'religion'],
                'tool_proficiencies': [],
                'languages': ['any_two'],
                'equipment': [
                    {'holy_symbol': 1},
                    {'prayer_book': 1},
                    {'prayer_vestments': 1},
                    {'common_clothes': 1}
                ],
                'feature': 'Shelter of the Faithful'
            },
            # Другие предыстории...
        }
        
        bg_info = details.get(background_type, {})
        return cls(name=background_type, **bg_info)
