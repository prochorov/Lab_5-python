import random


class Dice:
    def __init__(self, num_sides=6, num_dice=1, seed=None):
        self.num_sides = num_sides
        self.num_dice = num_dice
        self.rng = random.Random(seed)

    def roll(self):
        result = []
        for i in range(self.num_dice):
            result.append(self.rng.randint(1, self.num_sides))
        return tuple(result)


# Пример использования:
dice1 = Dice(num_sides=6, num_dice=2, seed=42)
dice2 = Dice(num_sides=6, num_dice=2, seed=42)
print(dice1.roll())  # вернет то же самое, что и dice2.roll()
print(dice2.roll())  # вернет то же самое, что и dice1.roll()
