import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import ifcopenshell
import os
from time import time
#
def insert_property_set(guid_pset, pset_name):
    global count_property_set, count_error_property_set, error_property_set
    try:
        cursor.execute(f'''INSERT INTO propertyset (id_guid_pset, pset_name)
        VALUES('{guid_pset}', '{pset_name}')''')
        count_property_set += 1
    except:
        count_error_property_set += 1
        error_property_set.append(guid_pset)

def insert_element_db(element):
    global count_element, count_error_element, error_element
    try:
        cursor.execute(f'''INSERT INTO element(id_guid_element, class_ifc)
            VALUES('{element.get_info()["GlobalId"]}', '{element.is_a()}')''')
        count_element += 1
    except:
        count_error_element += 1
        error_element.append(element.get_info()["GlobalId"])

def statistic():
    if count_element:
        print(f"В базу добавлено {count_element} элементов.")
    if count_error_element > 0:
        print(f"В базе уже содержатся {count_error_element} импортируемых элементов.\n"
              f"GUID элементов содержащихся в базе:\n{error_element}")
    if count_property_set:
        print(f"В базу добавлено {count_property_set} наборов параметров.")
    if count_error_property_set > 0:
        print(f"В базе уже содержатся {count_error_property_set} импортируемых наборов параметров.\n"
              f"GUID наборов параметров содержащихся в базе:\n{error_property_set}")

def insert_db(ifc_file):
    elements = ifc_file.by_type("IfcBuildingElement")
    for element in elements:
        insert_element_db(element)
        psets = ifcopenshell.util.element.get_psets(element)
        for pset, propertys in psets.items():
            guid_pset = ifc_file.by_id(propertys["id"]).get_info()["GlobalId"]
            insert_property_set(guid_pset, pset)
            # for property, var in propertys.items():
            #     if property != "id":
            #         print(property, var)

def open_ifc(path='.'):
    ''' Функция пакетной обработки IFC файлов'''
    files = sorted(os.listdir(path))
    for file in files:
        time_file = time()
        if file.endswith(".ifc"):
            print("Обработка файла", file)
            ifc_file = ifcopenshell.open(file)
            insert_db(ifc_file)
            print("\t\t\t\tЗатрачено времени", (time() - time_file))


count_element = 0
count_error_element = 0
error_element = []

count_property_set = 0
count_error_property_set = 0
error_property_set = []

#
#  f'''INSERT INTO property (id_pset, prop_name, prop_value, prop_type)
#  VALUES('{}', '{}', '{}', '{}')'''
#
#  f'''INSERT INTO relation_element_pset (id_element, id_pset)
#  VALUES('{}', '{}')'''


try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  password="AsdAsd1988",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Ifc_Element")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
     # Выполнение SQL-запроса
    open_ifc()
    statistic()
    cursor.execute('''SELECT * FROM element''')
#     cursor.execute('''SELECT id_guid_element, class_ifc, pset_name, prop_name, prop_value, prop_type
# FROM relation_element_pset
# JOIN element ON relation_element_pset.id_element = element.id_guid_element
# JOIN propertyset ON relation_element_pset.id_pset = propertyset.id_guid_pset
# JOIN property ON propertyset.id_guid_pset = property.id_pset''')

    record = cursor.fetchall()
    # for lst in record:
    #     print(lst)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")