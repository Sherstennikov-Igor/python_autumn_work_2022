from random import randint as rand
from time import time, strftime


def time_count(func):
    def wrapper(*args, **kwargs):
        f = open("debug.log", "a")
        wrapper.count += 1
        res = func(*args, **kwargs)
        f.write("{0} была вызвана: {1} раз. Последний вызов {2}.\n".format(func.__name__, wrapper.count, strftime("%c")))
        return res
    wrapper.count = 0
    return wrapper



@time_count
def field_gen(rows=5, kolumns=5):
    res = [[rand(0, 1) for _ in range(kolumns)] for _ in range(rows)]
    return res


@time_count
def count_ship(field):
    digit = [digits for row in field for digits in row]
    return digit.count(1)


game_field = field_gen(3, 3)


print(f"Число кораблей {count_ship(game_field)}")

while count_ship(game_field):
    for i in game_field: print(i)
    i, j = int(input("Наводка по Х: ")), int(input("Наводка по Y: "))
    if game_field[i][j] == 1:
        print("Есть пробитие")
        game_field[i][j] = -1
    elif game_field[i][j] == -1 or game_field[i][j] == -2:
        print("Уже стреляли")
    else:
        print("Поле пустое")
        game_field[i][j] = -2

print(f"Все корабли потоплены.\nИгра окончена")

