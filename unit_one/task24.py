# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

# Генерация английского алфавита по символам юникода в диапазоне от 97 до 123
alphabet_EN = []
for i in range(97, 123):
    alphabet_EN.append(chr(i))
print(alphabet_EN)




text = ''' Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
'''

res = []

for symbol in text.split():
    if symbol.isnumeric() is True:
        if int(symbol) == 0:
            res.append(" ")
        else:
            res.append(alphabet_EN[int(symbol) - 1])
    else:
        res.append(symbol)

print(" ".join(res))
