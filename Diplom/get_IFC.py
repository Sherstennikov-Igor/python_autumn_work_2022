import ifcopenshell
import os
from time import time

def insert_element(ifc_file):
    elements = ifc_file.by_type("IfcBuildingElement")
    for element in elements:
        cursor.execute(f'''INSERT INTO element(id_guid_element, class_ifc)
        VALUES('{element.get_info()["GlobalId"]}', '{element.is_a()}')''')



files = sorted(os.listdir('.'))
for file in files:
    time_file = time()
    if file.endswith(".ifc"):
        print("Обработка файла", file)
        ifc_file = ifcopenshell.open(file)
        element = ifc_file.by_type("IfcBuildingElement")
        propertry_set = ifc_file.by_type("IFCPROPERTYSET")
        propertry = ifc_file.by_type("IFCPROPERTYSINGLEVALUE")


        #
        # print(ifc_file.by_id(341))


for i in element:
    print(i.get_info()["GlobalId"])
    ss = ifcopenshell.util.element.get_psets(i)
    print(ss)
    for pset, propertys in ss.items():
        # print(pset)
        for property, var in propertys.items():
            if property == "id":
                print(ifc_file.by_id(var).get_info()["GlobalId"], pset)

            else:
                print(property, var)

