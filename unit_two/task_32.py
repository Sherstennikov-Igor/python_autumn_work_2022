# todo: Реализовать класс "Игровой персонаж".
#  Класс должен содержать атрибуты(свойства): Идентификатор, Имя, Здоровье, урон, Тип персонажа, Раса.
#  Инициализация атрибутов(состояние объекта) должна происходить в конструкторе.
#  В классе реализовать метод изменения здоровья по нанесенному урону(параметр функции).
#  Заложить логику: При достижении порога здоровья персонаж погибает
#  В классе реализовать метод получения значения атрибута урона
#  При достижении порога здоровья персонаж погибает
#  Реализовать дандер __repr__ для отладки персонажа
#  Реализовать дандер вычитания __sub__()  написав логику "боя" которая срабатывает
#  в момент вычитания объектов класса obj1 - obj2 и заключается в вычитании из
#  здоровья первого объекта урона наносимого вторым объектом
from random import randint as rand

class Char:
    # counter = 0
    def __init__(self, name, lvl, char_type, race):
        self.id = 0
        self.name = name
        self.lvl = lvl
        self.max_hp = rand(5, 15) * lvl
        self.hp = self.max_hp
        self.dmg = rand(1, 4) * lvl
        self.char_type = char_type
        self.race = race
        self.xp_gen = self.hp
        # Char.counter += 1

    def kill(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            print(f"{self.name} повержен")
            self.__del__()
            # Char.counter -= 1
    def __sub__(self, other):
        print(f"{self.name} наносит {self.dmg} урона по {other.name}")
        other.kill(self.dmg)
        if other.hp > 0:
            print(f"У {other.name} осталось {other.hp} здоровья из {other.max_hp}")
            print(f"{other.name} наносит {other.dmg} урона по {self.name}")
            self.kill(other.dmg)
            print(f"У {self.name} осталось {self.hp} здоровья из {self.max_hp}")

    def __repr__(self):
        return f'''
        {self.name} {self.lvl} уровня. ID = {self.id}.
        Со здоровьем {self.hp} HP и уроном {self.dmg} единиц.
        Тип персонажа - {self.char_type}. Рассы - {self.race}.
                '''


hero = Char("Ivan", 2, "Warrior", "Human")
enemy_1 = Char("Rat", 3, "Anumal", "Neutral")
enemy_2 = Char("Elephant", 1, "Anumal", "Neutral")

print(f"Сражаются: {hero.__repr__()} Против {enemy_1.__repr__()}")

while hero.hp or enemy_1.hp:
    hero - enemy_1

# list_char = [Hero, enemy_1, enemy_2]
# while len(list_char) > 1:
#     print(f"Число героев до ударов {len(list_char)}")
#     list_char[0] - list_char[1]
#
#
#     if list_char[0].hp < 0:
#         print("Игра окончена!")
#         break
#     elif list_char[1].hp < 0:
#         list_char.pop(1)
#     print(f"Число героев после ударов {len(list_char)}")

