# todo: Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.
#
# Input             	            Output
#
# apple	                        aple
# 25.04.2022 Good morning !!	    godmrni


# Генерация английского алфавита по символам юникода в диапазоне от 97 до 123
alphabet_EN = []
# for i in range(65, 90):
#     alphabet_EN.append(chr(i))
for i in range(97, 123):
    alphabet_EN.append(chr(i))
print(alphabet_EN)

test_1 = "apple"
test_2 = "25.04.2022 Good morning !!"

res = []
for symbol in test_2.lower():
    if symbol in alphabet_EN:
        if symbol not in res:
            res.append(symbol)

print("".join(res))
