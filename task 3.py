import random
import collections


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


# Создаем объект класса Dice с двумя шестигранными костями
dice = Dice(num_sides=6, num_dice=2)

# Словарь для хранения статистики
stats = collections.Counter()

# Бросаем кости 100000 раз
for i in range(100000):
    roll = dice.roll()
    stats[sum(roll)] += 1

# Выводим результаты
for value, count in sorted(stats.items()):
    print(f'{value}: {count}')