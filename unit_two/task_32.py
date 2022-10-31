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
        self.id = rand(0, 100500)
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


    def __del__(self):
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} повержен")

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

class Battle:
    def __init__(self, char_1, char_2):
        self.char_1 = char_1
        self.char_2 = char_2
        print(f"В битву вступают {char_1.__repr__()} против {char_2.__repr__()}")
    def battle(self):
        while self.char_1.hp > 0 and self.char_2.hp > 0:
            hero - enemy_1


hero = Char("Ivan", 2, "Warrior", "Human")
enemy_1 = Char("Rat", 1, "Anumal", "Neutral")
enemy_2 = Char("Elephant", 1, "Anumal", "Neutral")

fight = Battle(hero, enemy_1)
fight.battle()

