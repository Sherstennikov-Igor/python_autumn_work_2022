# todo: Выполнить задания далее:
#Преобразуйте переменную age и foo в число
age = "23"
print(float(age))

foo = "23abc"

print ("\nПервый вариант преобразования строки:")
if foo.isdigit() == 1:
    print(float.fromhex(foo))
else:
    print ("Невозможно преобразовать строку в число.")

print ("\nВторой вариант преобразования строки:")
print(float.fromhex(foo),"\n")


#Преобразуйте переменную age в Boolean
age = "123abc" # исправлена синтаксическая ошибка. Добавлены кавычки
print(bool(age),"\n")


#Преобразуйте переменную flag в Boolean
flag = 1
print(bool(flag),"\n")


#Преобразуйте значение  в Boolean
str_one = "Privet"
str_two = ""

print(bool(str_one))
print(bool(str_two))


#Преобразуйте значение 0 и 1  в Boolean
print(bool(0))
print(bool(1))
