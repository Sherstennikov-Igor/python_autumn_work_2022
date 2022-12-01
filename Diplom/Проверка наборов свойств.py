import ifcopenshell
import os
import time
import ifcopenshell.util
import ifcopenshell.util.element

time_start = time.time()


def count_elem(x_elements):
    ifc_class_dict = {}
    for x_element in x_elements:
        ifc_class = x_element.is_a()
        if ifc_class in ifc_class_dict.keys():
            ifc_class_dict[ifc_class] += 1
        else:
            ifc_class_dict[ifc_class] = 1
    x = ''''''
    for key, value in ifc_class_dict.items():
        x = x + "\t\t" + str(key) + " - " + str(value) + " шт.;\n"
    return x


Pset_dict = {"IfcWall": {"Местоположение": ["Номер корпуса", "Номер секции", "Этаж", "efefe"],
             "Маркировка": ["Позиция", "Обозначение", "Наименование"],
             "Геометрические параметры": ["Толщина", "Длина", "Объем", "Высота"],
             "Пожарные параметры": ["Предел огнестойкости", "Тип противопожарной преграды", "Класс пожарной опасности"],
             "Строительные параметры": ["Материал", "Наружная", "Тестовый параметр для стен"],
             "Тестовый набор для стен": ["khihj"]},
           "IfcDoor": {"Местоположение": ["Номер корпуса", "Номер секции", "Этаж"],
             "Маркировка": ["Позиция", "Обозначение", "Наименование"],
             "Геометрические параметры": ["Высота", "Высота в свету", "Высота порога", "Процент остекления", "Ширина", "Ширина в свету", "Тестовый параметр для дверей"],
             "Пожарные параметры": ["Аварийный выход", "Предел огнестойкости", "Тип противопожарной преграды", "Эвакуационный выход"],
             "Строительные параметры": ["Материал"],
             "Тестовый набор для дверей": ["khihj"]}
           }

path = '../python_autumn_2022'
files = sorted(os.listdir(path))

# print(f)

B_elements = []         # Элементы каркаса здания


for file in files:
    time_file = time.time()
    if file.endswith(".ifc"):
        print("Обработка файла", file)
        ifc_file = ifcopenshell.open(file)




        B_elements = ifc_file.by_type("IfcBuildingElement")         # Элементы каркаса здания

#
# for i in B_elements:
#      print(i)

for i in B_elements:
    ifc_class = i.is_a()                            # Получение класса IFC элемента
    Psets = Pset_dict.get(ifc_class)        # Получение требуемого набора параметров и свойств для класса IFC из словаря
    Data = ifcopenshell.util.element.get_psets(i)  # Выводит словарь свойств для элемента "Pset" : {"Prop" : "var"}
    # print(Data)
    for Pset, Props in Psets.items():
        if Pset not in Data.keys():
            print(f"Элемент {i.is_a()} не содержит требуемого набора параметров {Pset}")
        else:
            for Prop in Props:
                if Prop not in Data.get(Pset):
                    print(f"Для элемента {i.is_a()} набор атрибутов {Pset} не содержит требуемого свойства {Prop}")
