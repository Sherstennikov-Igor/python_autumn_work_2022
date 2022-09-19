# todo:  Создайте переменные, что бы вывести требуемый текст.

# задан нерабочий код
# требуемый вывод:
# Мой стек: python, javascript, php

programming_lang_1 = "python"
programming_lang_2 = "javascript"
programming_lang_3 = "php"

print("Мой стек: " + programming_lang_1 + ", " + programming_lang_2 + ", "+programming_lang_3)

#Вариант 2
print("\nВариант 2. Через вывод списка:")

list = []
list.append(programming_lang_1)
list.append(programming_lang_2)
list.append(programming_lang_3)

print("Мой стек:",", ".join(list))
