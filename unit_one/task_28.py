# todo 1: Для игры "Морской бой" файл sea_battle.py написать создание игрового поля nxn

# todo 2: В игровой матрице nxn найти кол-во всех 1

#  Задачи решить через генераторы списков (списковые включения)

from random import randint


def field_gen(rows=5, kolumns=5):
    res = []
    for row in range(0, rows):
        line = [(lambda: randint(0, 1))() for _ in range(0, kolumns)]
        res.append(line)
    return res


def count_ship(field):
    line = [digit for row in field for digit in row]
    return line.count(1)


game_field = field_gen(10, 10)
print(game_field)
print(count_ship(game_field))

print("\n\nАнализ статистики рандомайзера")
statistic = {}
count = []
mass = [(lambda: field_gen(10, 10))() for _ in range(100)]
for i in mass:
    count.append(count_ship(i))
print(count)

for res in count:
    if res not in statistic:
        statistic[res] = 1
    else:
        statistic[res] = statistic[res] + 1

print(sorted(statistic.items()))