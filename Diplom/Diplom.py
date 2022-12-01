import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import ifcopenshell
import os
from time import time


def insert_element(ifc_file):
    elements = ifc_file.by_type("IfcBuildingElement")
    count_element = 0
    error_element = 0
    for element in elements:
        try:
            cursor.execute(f'''INSERT INTO element(id_guid_element, class_ifc)
            VALUES('{element.get_info()["GlobalId"]}', '{element.is_a()}')''')
            count_element += 1
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            error_element += 1
            continue

    print(f"В базу добавлено {count_element}.\n Ошибок добавления элементов {error_element}")


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
    cursor.execute('''SELECT * FROM element''')

#     cursor.execute('''SELECT id_guid_element, class_ifc, pset_name, prop_name, prop_value, prop_type
# FROM relation_element_pset
# JOIN element ON relation_element_pset.id_element = element.id_guid_element
# JOIN propertyset ON relation_element_pset.id_pset = propertyset.id_guid_pset
# JOIN property ON propertyset.id_guid_pset = property.id_pset''')

   # f'''INSERT INTO element(id_guid_element, class_ifc)
   #  VALUES('{}', '{}')'''
   #
   #  f'''INSERT INTO propertyset (id_guid_pset, pset_name)
   #  VALUES('{}', '{}')'''
   #
   #  f'''INSERT INTO property (id_pset, prop_name, prop_value, prop_type)
   #  VALUES('{}', '{}', '{}', '{}')'''
   #
   #  f'''INSERT INTO relation_element_pset (id_element, id_pset)
   #  VALUES('{}', '{}')'''

    record = cursor.fetchall()
    for lst in record:
        print(lst)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")