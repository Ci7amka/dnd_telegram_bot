import random

def roll_dice(notation: str):
    """
    Бросок кубика с нотацией, например '2d6+3'
    """
    try:
        # Разбор нотации
        if '+' in notation:
            dice, modifier = notation.split('+')
            modifier = int(modifier)
        else:
            dice = notation
            modifier = 0

        count, sides = map(int, dice.split('d'))
        
        # Бросок кубиков
        rolls = [random.randint(1, sides) for _ in range(count)]
        total = sum(rolls) + modifier

        return {
            'rolls': rolls,
            'total': total,
            'modifier': modifier
        }
    except Exception as e:
        return f"Ошибка при броске: {str(e)}"
