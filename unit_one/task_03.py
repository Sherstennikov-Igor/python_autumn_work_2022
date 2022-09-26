# todo: Данные две переменные:
# Нужно обменять значения переменных местами. В итого age должен равнятся 25 а  temperature – 36.6:
age = 36.6
temperature = 25

print("\nПервый вариант. Через дополнительную переменную:") # Через дополнительную переменную
tmp = age
age = temperature
temperature = tmp
del(tmp)

print("age =",age)
print("temperature =",temperature)

print("\nВторой вариант. Через множественное присваивание:") # Через множественное присваивание

age = 39.9
temperature = 54

temperature, age = age, temperature

print("age =",age)
print("temperature =",temperature)
