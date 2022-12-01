import ifcopenshell
import os
from time import time

def insert_element(ifc_file):
    elements = ifc_file.by_type("IfcBuildingElement")
    for element in elements:
        cursor.execute(f'''INSERT INTO element(id_guid_element, class_ifc)
        VALUES('{element.get_info()["GlobalId"]}', '{element.is_a()}')''')

def open_ifc(path='.'):
    ''' Функция пакетной обработки IFC файлов'''
    files = sorted(os.listdir(path))
    for file in files:
        time_file = time()
        if file.endswith(".ifc"):
            print("Обработка файла", file)
            ifc_file = ifcopenshell.open(file)
            insert_element(ifc_file)
            print("\t\t\t\tЗатрачено времени", (time() - time_file))




# ifc_file = open_ifc()
#
#
# element = ifc_file.by_type("IfcBuildingElement")
# propertry_set = ifc_file.by_type("IFCPROPERTYSET")
#
# for i in propertry_set:
#     ss = i.get_info()
#     # print(ss)
#     print(ss["GlobalId"])
#     print(ss["Name"])
#     print(ss["HasProperties"])
#     # print(i.get_info(recursive=True))
#
# # print(ifc_file.by_id(823))
