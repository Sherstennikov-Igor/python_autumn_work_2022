import os
from time import time
import ifcopenshell
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def open_file_ifc(path='.'):
    """Функция пакетной обработки IFC файлов"""
    files = sorted(os.listdir(path))
    for file in files:
        time_file = time()
        if file.endswith(".ifc"):
            print("Обработка файла", file)
            ifc_file = ifcopenshell.open(file)
            insert_db(ifc_file)
            print("\t\t\t\tЗатрачено времени на чтение файлов", (time() - time_file))


def insert_db(ifc_file):
    elements = ifc_file.by_type("IfcBuildingElement")
    for element in elements:
        insert_element_db(element)
        guid_element = element.get_info()["GlobalId"]
        psets = ifcopenshell.util.element.get_psets(element)
        for pset, propertys in psets.items():
            guid_pset = ifc_file.by_id(propertys["id"]).get_info()["GlobalId"]
            insert_property_set(guid_pset, pset)
            insert_relation(guid_element, guid_pset)
            for prop, var in propertys.items():
                insert_property_set(guid_pset, pset)
                if prop != "id":
                    insert_property(guid_pset, prop, var)


def insert_element_db(element):
    """ Функция вставки элементов в БД и подсчета числа вставленных и их дубликатов вставки по GUID"""
    global count_element, count_error_element, error_element
    try:
        cursor.execute(f'''INSERT INTO element(id_guid_element, class_ifc)
            VALUES('{element.get_info()["GlobalId"]}', '{element.is_a()}')''')
        count_element += 1
    except:
        count_error_element += 1
        error_element.append(element.get_info()["GlobalId"])


def insert_property_set(guid_pset, pset_name):
    """Функция вставки наборов атрибутов в БД и подсчета числа вставленных и их дубликатов вставки по GUID"""
    global count_property_set, count_error_property_set, error_property_set
    try:
        cursor.execute(f'''INSERT INTO propertyset (id_guid_pset, pset_name)
        VALUES('{guid_pset}', '{pset_name}')''')
        count_property_set += 1
    except:
        count_error_property_set += 1
        error_property_set.append(guid_pset)


def insert_property(id_pset, prop_name, prop_value):
    """Функция вставки свойств в БД и подсчета числа вставленных и их дубликатов вставки"""
    global count_property, count_error_property
    try:
        cursor.execute(f'''INSERT INTO property (id_pset, prop_name, prop_value)
        VALUES('{id_pset}', '{prop_name}', '{prop_value}')''')
        count_property += 1
    except:
        count_error_property += 1


def insert_relation(id_element, id_pset):
    """Функция вставки взаимосвизей между элементами и наборами свойств"""
    global count_relation, count_error_relation
    try:
        cursor.execute(f'''INSERT INTO relation_element_pset (id_element, id_pset)
        VALUES('{id_element}', '{id_pset}')''')
        count_relation += 1
    except:
        count_error_relation += 1


def statistic():
    """Функция вывода статистики по результатам работы вставки данных в БД"""
    time_statistic = time()
    if count_element:
        print(f"В базу добавлено {count_element}"
              f" из {count_element + count_error_element} элементов.")
    if count_error_element > 0:
        print(f"В базе уже содержатся {count_error_element}"
              f" из {count_element + count_error_element} импортируемых элементов.\n"
              f"GUID элементов содержащихся в базе:\n{error_element}")

    if count_property_set:
        print(f"В базу добавлено {count_property_set}"
              f" из {count_property_set + count_error_property_set} наборов параметров.")
    if count_error_property_set > 0:
        print(f"В базе уже содержатся {count_error_property_set}"
            f" из {count_property_set + count_error_property_set} импортируемых наборов параметров.\n"
            f"GUID наборов параметров содержащихся в базе:\n{error_property_set}")

    if count_property:
        print(f"В базу добавлено {count_property}"
              f" из {count_property + count_error_property} параметров.")
    if count_error_property > 0:
        print(f"В базе уже содержатся {count_error_property}"
              f" из {count_property + count_error_property} импортируемых параметров.\n")

    if count_relation:
        print(f"В базу добавлено {count_relation}"
              f" из {count_relation + count_error_property_set} связей элементов и наборов параметров.")
    if count_error_relation > 0:
        print(f"В базе уже содержатся {count_error_property_set}"
              f" из {count_relation + count_error_property_set} импортируемых связей элементов и наборов параметров.\n")
    print("\t\t\t\tЗатрачено времени на вставку в базу", (time() - time_statistic))

count_element = 0
count_error_element = 0
error_element = []

count_property_set = 0
count_error_property_set = 0
error_property_set = []

count_property = 0
count_error_property = 0

count_relation = 0
count_error_relation = 0

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
    open_file_ifc()
    statistic()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
