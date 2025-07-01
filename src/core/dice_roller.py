# src/core/dice_roller.py
import random
from typing import Dict, List

class DiceRoller:
    @staticmethod
    def roll(notation: str) -> Dict[str, any]:
        try:
            # Обработка различных форматов нотации
            notation = notation.lower()
            
            # Разбор количества кубиков
            if 'd' in notation:
                parts = notation.split('d')
                count = int(parts[0]) if parts[0] else 1
            else:
                count = 1
                parts = [1, notation]

            # Разбор сторон кубика и модификатора
            if '+' in parts[1]:
                sides, modifier = map(int, parts[1].split('+'))
            elif '-' in parts[1]:
                sides, modifier = map(int, parts[1].split('-'))
                modifier = -modifier
            else:
                sides = int(parts[1])
                modifier = 0

            # Выполнение бросков
            rolls = [random.randint(1, sides) for _ in range(count)]
            total = sum(rolls) + modifier

            return {
                'rolls': rolls,
                'total': total,
                'modifier': modifier,
                'notation': notation
            }
        except Exception as e:
            # Более информативное сообщение об ошибке
            raise ValueError(f"Неверный формат броска: {notation}. Ошибка: {str(e)}")

    @staticmethod
    def roll_ability_scores() -> List[int]:
        scores = []
        for _ in range(6):
            rolls = sorted([random.randint(1, 6) for _ in range(4)])
            scores.append(sum(rolls[1:]))
        return sorted(scores, reverse=True)
