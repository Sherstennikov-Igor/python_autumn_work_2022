# todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#  функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#  чтобы каждая функция выполняла одно универсальное действие.

import random
# Начальные данные
words = ["колибри", "селекция", "бисер", "камикадзе"]                       # Список слов
desc_ = ["Эта птица может летать спиной вперед",
         "Противовес «естественного отбора», созданный человеком",
         "Предмет, совершенно не интересующий свиней",
         "С японского это слово переводится как «Божественный ветер»"]      # Список описания слов

lives = 5                                                                   # Количество "жизней"
letter = ""                                                                 # Переменная для ввода букв

# Определение функций


def tablo():                                                                # Функция вывода табло
    global letter
    if ("".join(answer)) == secret and lives > 0:
        print("\n", " ".join(answer))
        print("Игра окончена\nПоздравляем!!! Вы угадали загаданно слово")
    elif lives == 0:
        print("\nК сожалению, вы проиграли! ((")
        print("Загаданное слово было:", secret)
    else:
        print("\n", " ".join(answer))
        letter = input("Введите букву: ")


def life(live):                                                             # Функция "Смерти"
    global lives
    lives = live - 1
    print("Нет такой буквы. Вращайте барабан. У вас осталось ", lives, "попыток!")


def serch(word, symbol):                                                    # Функция поиска вхожденией буквы в слово
    global answer
# Случай единичного вхождение буквы
    if list(word).count(symbol) == 1:
        ind = list(word).index(symbol)
        answer[ind] = symbol
# Случай множественного вхождения буквы
    else:
        start = 0
        for n in range(list(word).count(symbol)):
            ind = list(word).index(symbol, start, len(word))
            start = ind + 1
            answer[ind] = symbol


# Генератор рандомного выбора слова
pik = random.randint(0, len(words)-1)
secret = words[pik]
print(desc_[pik])

answer = list("X"*len(words[pik]))          # "Поле" задание ответа

# "Тело" игры
while ("".join(answer)) != secret and lives > 0:
    tablo()
    if letter not in secret:
        life(lives)
    else:
        serch(secret, letter)
tablo()
