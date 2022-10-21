#todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 classwork/task3
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
#
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
#
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.
import pickle

status_menu = 0
secret = 0
lives = 0
my_digit = 1


def rand(start=0, end=100):
    from random import randint
    digit = randint(start, end)
    return digit


def new_game():
    global secret, lives, my_digit
    secret = rand()
    lives = 10
    my_digit = 999
    game_options()
    game_logic()


def menu():
    global status_menu
    print("1. Новая Игра\n"
          "2. Продолжить игру\n"
          "3. Сохранить игру\n"
          "4. Загрузить игру\n"
          "5. Сдаюсь"
          )
    status_menu = int(input("Выберите действие: "))
    match status_menu:
        case 1:
            new_game()
        case 2:
            print("Продолжаем угадывать")
            game_logic()
        case 3:
            game_save()
        case 4:
            game_load()
        case 5:
            game_out()


def game_options():
    global lives
    print("1. Easy game\n"
          "2. Normal mode\n"
          "3. Hard mode\n"
          )
    mode = int(input("Выберите режим: "))
    match mode:
        case 1: lives = 20
        case 2: lives = 10
        case 3: lives = 5
    print(f"Установлено количество жизней {lives}")


def game_out():
    global secret, my_digit
    my_digit = secret
    print(f"Загаданное число было {secret}.\nИгра окончена до скорой встречи!")


def save_file():
    try:
        with open("game_dump.pkl", "rb") as f:
            save_db = pickle.load(f)
            return save_db
    except:
        save_db = []
        with open("game_dump.pkl", "wb") as f:
            pickle.dump(save_db, f)
            return save_db


def game_save():
    from time import strftime
    save_db = save_file()
    save_name = input("Введите название игры:")
    save_point = {"save_name": save_name, "save_time": strftime("%c"), "secret": secret, "lives": lives, "last_digit": my_digit}
    save_db.append(save_point)
    with open('game_dump.pkl', 'wb') as f:
        pickle.dump(save_db, f)
    print("Прогресс успешно сохранен")
    game_logic()


def game_load():
    save_db = save_file()
    for save in save_db:
        save_info = f"{save['save_name']} {save['save_time']}"
        print(save_info)
    save_name = input("Введите имя cохранения: ")
    global secret, lives, my_digit
    for save in save_db:
        if save_name == save["save_name"]:
            secret = save["secret"]
            lives = save["lives"]
            my_digit = save["last_digit"]
            print(f"Игра восстановлена {save['save_name']}")
            compar()

    game_logic()


def death():
    global secret, lives, my_digit
    lives = lives - 1

def compar():
    if secret > my_digit:
        res = "меньше"
    else:
        res = "больше"
    print(f"{my_digit} {res} загаданного числа. У вас осталось {lives} попыток")


def game_logic():
    global secret, lives, my_digit
    while secret != my_digit:
        temp = input("Введите число или M для выхода в меню: ")
        if temp == "M":
            menu()
        else:
            my_digit = int(temp)
            if secret != my_digit:
                death()
                compar()
    print(f"____________________________________________\nПоздравляем вы угадали задуманное число было {secret}!")


menu()

# print("\n\n________\nСТАТИСТИКА ПОСЛЕ ИГРЫ\n________\n")
# print(f"Последнее действие в меню {status_menu}")
# print(f"Загаданное число было {secret}")
# print(f"Осталось жизней {lives}")
# print(f"Последнее загаданное число {my_digit}")
