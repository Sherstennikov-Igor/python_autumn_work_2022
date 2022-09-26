#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.
import random

mass = []

for i in range (10):
    mass.append(random.randint(1,100))
print(mass)

print("Увеличение каждого элемента на 1 ")

index = 0
for i in mass:
    i = i + 1
    mass[index] = i
    index = index + 1
print(mass)



