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
from random import choices


class Char:
    # counter = 0
    def __init__(self, name, lvl, char_type, race, dodge):
        self.id = rand(0, 100500)
        self.name = name
        self.lvl = lvl
        self.max_hp = rand(20, 30) * lvl
        self.hp = self.max_hp
        self.base_dmg = rand(2, 4) * lvl
        self.char_type = char_type
        self.race = race
        self.xp_gen = self.hp
        self.dodge = dodge
        # Char.counter += 1

    def kill(self, dmg):
        self.hp -= dmg

    def __del__(self):
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} повержен")

    def dmg_range(self, char_type):
        match char_type:
            case "Warrior":
                dmg = self.base_dmg*rand(1, 3)
            case "Mage":
                dmg = self.base_dmg
            case "Anumal":
                dmg = self.base_dmg*rand(1, 2)
            case "LoL":
                dmg = self.base_dmg*rand(-100, 100)
        return dmg

    def __sub__(self, other):
        hit_dmg = self.dmg_range(self.char_type)
        dodge = choices([0, 1], weights=[1 - other.dodge / 100, other.dodge / 100])[0]
        if dodge:
            print(f"{self.name} пытается нанести удар по {other.name}\n"
                  f"Но подлый {other.name} увернулся от удара")
        else:
            print(f"{self.name} наносит {hit_dmg} урона по {other.name}")
            other.kill(hit_dmg)
        if other.hp > 0:
            print(f"У {other.name} осталось {other.hp} здоровья из {other.max_hp}")
            hit_dmg = other.dmg_range(other.char_type)
            dodge = choices([0, 1], weights=[1 - self.dodge / 100, self.dodge / 100])[0]
            if dodge:
                print(f"{other.name} пытается нанести удар по {self.name}\n"
                      f"Но храбрый {self.name} увернулся от удара")
            else:
                self.kill(hit_dmg)
                print(f"{other.name} наносит {hit_dmg} урона по {self.name}\n"
                      f"У {self.name} осталось {self.hp} здоровья из {self.max_hp}")

    def __repr__(self):
        return f'''
        {self.name} {self.lvl} уровня. ID = {self.id}.
        Со здоровьем {self.hp} HP и базовым уроном {self.base_dmg} единиц.
        Тип персонажа - {self.char_type}. Рассы - {self.race}.
                '''


class Battle:
    def __init__(self, char_1, char_2):
        self.char_1 = char_1
        self.char_2 = char_2
        print(f"В битву вступают {char_1.__repr__()} против {char_2.__repr__()}")

    def battle(self):
        while self.char_1.hp > 0 and self.char_2.hp > 0:
            self.char_1 - self.char_2


hero = Char("Ivan", 2, "Warrior", "Human", 50)
enemy_1 = Char("Rat", 1, "Anumal", "Neutral", 30)
enemy_2 = Char("Elephant", 4, "Anumal", "Neutral", 0)

fight = Battle(hero, enemy_2)
fight.battle()
