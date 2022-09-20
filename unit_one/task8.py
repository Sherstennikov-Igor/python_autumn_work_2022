#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
#A = 10
#B = 3
#C = 7
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

# Пример 2:
A = 2
B = 1
C = 1
# Итоговый результат должен быть:
# A = 2
# B = 7
# C = 10


print ("Вариант через условия")
if A >= B and A >= C:
    A = A
    if B > C:
        B = B
    else:
        B,C = C,B
elif B > C:
    if A > C:
        A, B, C = B, A, C
    else:
        A, B, C = B, C, A
elif B > A:
    A,B,C = C,B,A
else:
    A,B,C = C,A,B

print("A =",A,"\nB =",B,"\nC =",C)

print ("\nВариант через массив")

A = 4
B = 200
C = 10

list = []
list.append(A)
list.append(B)
list.append(C)
#reverse=False
list.sort(reverse=True)

print("A =",list[0],"\nB =",list[1],"\nC =",list[2])
