import random
from typing import Dict, List

class DiceRoller:
    @staticmethod
    def roll(notation: str) -> Dict[str, any]:
        try:
            # Парсинг нотации (например, 2d6+3)
            if '+' in notation:
                dice, modifier = notation.split('+')
                modifier = int(modifier)
            elif '-' in notation:
                dice, modifier = notation.split('-')
                modifier = -int(modifier)
            else:
                dice, modifier = notation, 0

            count, sides = map(int, dice.split('d'))
            
            # Бросок кубиков
            rolls = [random.randint(1, sides) for _ in range(count)]
            total = sum(rolls) + modifier

            return {
                'rolls': rolls,
                'total': total,
                'modifier': modifier,
                'notation': notation
            }
        except Exception as e:
            raise ValueError(f"Неверный формат броска: {notation}")

    @staticmethod
    def roll_ability_scores() -> List[int]:
        """Генерация характеристик по классическим правилам D&D"""
        scores = []
        for _ in range(6):
            rolls = sorted([random.randint(1, 6) for _ in range(4)])
            scores.append(sum(rolls[1:]))
        return sorted(scores, reverse=True)
