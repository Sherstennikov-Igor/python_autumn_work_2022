# todo: Реализовать логику игры "Морской бой". Задано игровое поле 5 на 5 в виде двухмерного массива(список списков).
#  Значением 1 (единицей) обозначают однопалубный корабль в координатах i-ой строки и j-го столбца.
#  Написать игровую логику которая по вводу пары i,j  проверяет попадание и его фиксирует.
#  Для генерации случайных значений 0 и 1 в массиве использовать lambda выражение. Кол-во кораблей может быть случайное
#  в зависимости от генерации. Кол-во попыток пока не ограничивать.

# # Пример:
# game_field = []
# # нужно заменить статическую инициализацию списка на динамическую с помощью lambda выражения.
# row_one   = [0, 0, 0, 1, 0]
# row_two   = [0, 0, 0, 1, 0]
# row_three = [0, 1, 0, 0, 0]
# row_four  = [0, 0, 0, 1, 0]
# row_five  = [0, 0, 0, 1, 0]
#
# game_field.append(row_one)
# game_field.append(row_two)
# game_field.append(row_three)
# game_field.append(row_four)
# game_field.append(row_five)
# i = 1  # вхождение в первый массив
#
# j = 2  # вхождение в 4-ый элемент текущего массива
# # доступ к элементам двухмерного массива
# print(game_field[i][j])

from random import randint

game_field = []
rows = 5        # Число строк на поле
kolumns = 5     # Число колонок на поле

for row in range(0, rows):
    line = [(lambda: randint(0, 1))() for kol in range(0, kolumns)]
    game_field.append(line)


while any(pos == 1 for pos, *_ in game_field):
    for i in game_field: print(i)
    i, j = int(input("Наводка по Х: ")), int(input("Наводка по Y: "))
    if game_field[i][j] == 1:
        print("Есть пробитие")
        game_field[i][j] = "X"
    elif game_field[i][j] == "X" or game_field[i][j] == "*":
        print("Уже стреляли")
    else:
        print("Поле пустое")
        game_field[i][j] = "*"

print("Игра закончена")