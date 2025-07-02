from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Dict, Optional

class ClassType(Enum):
    WARRIOR = "Воин"
    WIZARD = "Волшебник"
    ROGUE = "Плут"
    CLERIC = "Жрец"
    BARD = "Бард"
    DRUID = "Друид"
    PALADIN = "Паладин"
    RANGER = "Следопыт"
    SORCERER = "Чародей"
    WARLOCK = "Колдун"
    MONK = "Монах"
    BARBARIAN = "Варвар"

@dataclass
class CharacterClass:
    """
    Расширенный класс для классов персонажей D&D
    """
    name: ClassType
    hit_dice: int = 8  # По умолчанию к8
    primary_abilities: List[str] = field(default_factory=list)
    saving_throws: List[str] = field(default_factory=list)
    armor_proficiencies: List[str] = field(default_factory=list)
    weapon_proficiencies: List[str] = field(default_factory=list)
    skill_proficiencies: List[str] = field(default_factory=list)
    equipment: List[str] = field(default_factory=list)
    special_abilities: Dict[str, str] = field(default_factory=dict)

def create_character_class(class_type: ClassType) -> CharacterClass:
    """
    Фабрика для создания классов персонажей с полной конфигурацией
    """
    class_configs = {
        ClassType.WARRIOR: {
            'hit_dice': 10,
            'primary_abilities': ['Strength', 'Constitution'],
            'saving_throws': ['Strength', 'Constitution'],
            'armor_proficiencies': ['Light', 'Medium', 'Heavy', 'Shields'],
            'weapon_proficiencies': ['Simple', 'Martial'],
            'skill_proficiencies': ['Athletics', 'Intimidation'],
            'equipment': [
                'Chain mail', 
                'Martial weapon', 
                'Shield', 
                'Adventurer\'s pack'
            ],
            'special_abilities': {
                'fighting_style': 'Выберите специализацию боевого стиля',
                'second_wind': 'Восстановление части здоровья в бою'
            }
        },
        ClassType.WIZARD: {
            'hit_dice': 6,
            'primary_abilities': ['Intelligence'],
            'saving_throws': ['Intelligence', 'Wisdom'],
            'armor_proficiencies': [],
            'weapon_proficiencies': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs'],
            'skill_proficiencies': ['Arcana', 'History'],
            'equipment': [
                'Quarterstaff', 
                'Component pouch', 
                'Spellbook', 
                'Scholar\'s pack'
            ],
            'special_abilities': {
                'spellcasting': 'Способность использовать магические заклинания',
                'arcane_recovery': 'Восстановление части магических ячеек'
            }
        },
        ClassType.ROGUE: {
            'hit_dice': 8,
            'primary_abilities': ['Dexterity', 'Intelligence'],
            'saving_throws': ['Dexterity', 'Intelligence'],
            'armor_proficiencies': ['Light armor'],
            'weapon_proficiencies': ['Simple', 'Hand crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
            'skill_proficiencies': ['Stealth', 'Sleight of Hand', 'Deception'],
            'equipment': [
                'Rapier', 
                'Shortbow', 
                'Leather armor', 
                'Thieves\' tools'
            ],
            'special_abilities': {
                'sneak_attack': 'Дополнительный урон по незащищенной цели',
                'cunning_action': 'Дополнительное действие в бою'
            }
        },
        ClassType.CLERIC: {
            'hit_dice': 8,
            'primary_abilities': ['Wisdom'],
            'saving_throws': ['Wisdom', 'Charisma'],
            'armor_proficiencies': ['Light', 'Medium', 'Shields'],
            'weapon_proficiencies': ['Simple weapons'],
            'skill_proficiencies': ['Religion', 'Medicine'],
            'equipment': [
                'Mace', 
                'Scale mail', 
                'Light crossbow', 
                'Holy symbol'
            ],
            'special_abilities': {
                'divine_magic': 'Заклинания божественной магии',
                'turn_undead': 'Изгнание нежити'
            }
        }
        # Можно добавить остальные классы по аналогии
    }
    
    config = class_configs.get(class_type, {})
    return CharacterClass(
        name=class_type,
        hit_dice=config.get('hit_dice', 8),
        primary_abilities=config.get('primary_abilities', []),
        saving_throws=config.get('saving_throws', []),
        armor_proficiencies=config.get('armor_proficiencies', []),
        weapon_proficiencies=config.get('weapon_proficiencies', []),
        skill_proficiencies=config.get('skill_proficiencies', []),
        equipment=config.get('equipment', []),
        special_abilities=config.get('special_abilities', {})
    )

# Вспомогательные функции
def get_all_classes() -> List[CharacterClass]:
    """
    Возвращает список всех классов
    """
    return [create_character_class(class_type) for class_type in ClassType]

def get_class_by_name(name: str) -> Optional[CharacterClass]:
    """
    Получение класса по имени
    """
    try:
        class_type = ClassType(name)
        return create_character_class(class_type)
    except ValueError:
        return None
