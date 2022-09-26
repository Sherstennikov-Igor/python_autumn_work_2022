#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

coord_a = float(input("Введите координату точки А:"))
coord_b = float(input("Введите координату точки В:"))
coord_c = float(input("Введите координату точки С:"))

length_a_b = abs(coord_a-coord_c)
length_b_c = abs(coord_b-coord_c)
summ = length_a_b + length_b_c

print("Длина отрезка АС = ",length_a_b,"у.е.","\nДлина отрезка BC = ",length_b_c,"у.е.","\nСумма длин отрезков = ", summ,"у.е.")