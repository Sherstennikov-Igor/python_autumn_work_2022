# #todo: Найти сумму элементов матрицы
# # Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# # Задачу решить с помощью генераторов.
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21
from functools import reduce

matrix = [[1, 2, 3, 5, 7], [4, 5, 6, 77]]

summ_1 = 0
for row in matrix:
    for did in row:
        summ_1 += did
print(f"Вариант через циклы {summ_1}")


summ = 0
# summ = [(lambda digit: digit + 1)(digit) for row in matrix for digit in row]
line = [digit for row in matrix for digit in row]
for i in line:
    summ += i
print(f"Вариант через генератор {summ}")

