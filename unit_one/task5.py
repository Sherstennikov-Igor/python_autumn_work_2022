#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

number_1 = float(input("Введите первое число:"))
number_2 = float(input("Введите второе число:"))

summ = number_1 + number_2
subtract = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2
division_2, division_3 = divmod(number_1,number_2)
exponentiation = number_1 ** number_2


print ("Сумма = ", summ,"\nРазность = ", subtract,"\nПроизведение = ", multiplication,"\nДеление = ", division,"\nДеление с целочисленное = ", division_2,"\nДеление с остатком = ", division_3,"\nВозведение в степень = ", exponentiation)