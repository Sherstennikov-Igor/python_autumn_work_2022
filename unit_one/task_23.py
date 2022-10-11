# todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

line = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."         # Зашифрованная строка

# Генерация английского алфавита по символам юникода в диапазоне от 97 до 123
alphabet_EN = []
for i in range(97, 123):
    alphabet_EN.append(chr(i))

# Брутфорс всех вариантов сдвига по английскому алфавиту
for i in range(1, len(alphabet_EN)):
    res = []
    for symbol in line:
        if symbol in alphabet_EN:
            shift = alphabet_EN.index(symbol) - i
            res.append(alphabet_EN[shift])
        else:
            res.append(symbol)
    print("".join(res))
