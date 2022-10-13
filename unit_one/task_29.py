# todo. Транспонирование матрицы, transpose(matrix)
# level:hight
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы.
# Решить с использованием списковых включений.

#
# Пример:
# transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||

matrix = [[1, 2, 3, 4], [4, 5, 6, 7]]

t_matrix_1 = []
for i in range(len(matrix[0])):
    temp = []
    for j in range(len(matrix)):
        temp.append(matrix[j][i])
    t_matrix_1.append(temp)
print(f"Вариант через циклы {t_matrix_1}")


t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(f"Вариант через генератор {t_matrix}")
