# #todo: Найти сумму элементов матрицы
# # Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# # Задачу решить с помощью генераторов.
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21


matrix = [[1, 2, 3, 5, 7], [4, 5, 6, 77]]

summ_1 = 0
for row in matrix:
    for did in row:
        summ_1 += did
print(f"Вариант через циклы {summ_1}")


def matr_summ(matr):
    digit = [digits for rows in matr for digits in rows]
    return sum(digit)


print(f"Вариант через генератор {matr_summ(matrix)}")
