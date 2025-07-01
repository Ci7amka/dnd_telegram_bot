import random
from typing import Dict, List

class DiceRoller:
    @staticmethod
    def roll(notation: str) -> Dict[str, any]:
        try:
            parts = notation.lower().split('d')
            count = int(parts[0]) if parts[0] else 1
            
            if '+' in parts[1]:
                sides, modifier = map(int, parts[1].split('+'))
            elif '-' in parts[1]:
                sides, modifier = map(int, parts[1].split('-'))
                modifier = -modifier
            else:
                sides, modifier = int(parts[1]), 0
            
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
        scores = []
        for _ in range(6):
            rolls = sorted([random.randint(1, 6) for _ in range(4)])
            scores.append(sum(rolls[1:]))
        return sorted(scores, reverse=True)
