import random


class Dice:
    def __init__(self, num_sides=6, num_dice=1):
        self.num_sides = num_sides
        self.num_dice = num_dice

    def roll(self):
        result = []
        for i in range(self.num_dice):
            result.append(random.randint(1, self.num_sides))
        return tuple(result)


# Пример использования:
dice = Dice(num_sides=6, num_dice=2)
print(dice.roll())  # вернет случайное число от 1 до 6 два раза
