from flask import Flask
import psycopg2

app = Flask(__name__)

connection = psycopg2.connect(user="postgres",
                              password="AsdAsd1988",
                              host="127.0.0.1",
                              port="5432",
                              database="Ifc_Element")

style_table = '''
.table_count {
  border-collapse: collapse;
  counter-reset: schetchik;  /* счётчик с названием "schetchik" работает в рамках класса .table_count */ 
}
.table_count tr {
  counter-increment: schetchik;  /* при встрече тега tr счётчик с названием "schetchik" увеличивается на единицу */ 
}
.table_count td,
.table_count tr:before {
  padding: .1em .5em;
  border: 1px solid #E7D5C0;
}
.table_count tr:before {
  content: counter(schetchik);  /* значение счётчика с названием "schetchik" записывается в первую клетку строки */ 
  display: table-cell;
  vertical-align: middle;
  color: #978777;
}'''

@app.route("/")
def index():
    menu_html = '''
    <html lang="ru" >
     <head>
       <meta charset="utf-8">
       <title>Информация по модели</title>
     </head>
     <body>
        <header>
            <h1 class="logo">Информация по модели</h1>
            <nav>
              <ul class="menu">
                <li><a href="/info/element">Вывод статистики по элементам</a></li>
                <li><a href="/info/propertyset">Вывод статистики по наборам свойств</a></li>
                <li><a href="/info/property">Вывод информации по свойствам элементов</a></li>
                <li><a href="/check/property">Проверка наличия свойств и наборов свойств</a></li>
              </ul>
            </nav>
        </header>
     </body>
    </html>'''
    return menu_html

@app.route("/info/element")
def info_element():
    # Формирование запроса в базу данных проекта
    cursor_element = connection.cursor()
    cursor_element.execute('''
                            SELECT class_ifc, count (class_ifc)
                            FROM element
                            GROUP BY class_ifc;
                            ''')
    element_info = cursor_element.fetchall()
    element_info_html = ""
    for line in element_info:
        element_info_html += f"<rt>\n<td>{line[0]}</td>\n<td>{line[1]}</td>\n</tr>"
    # Формирование HTML страницы
    element_html = f'''
    <html lang="ru" >
    <head>
    <meta charset="utf-8">
    <title>Статистика по элементам</title>
    </head>
    <body>
        <header>
        <h1 class="logo">Статистика по элементам</h1>
        <nav>
        <ul class="menu">
        <li><a href="/">Выход в меню</a></li>
        </ul>
        </nav>
        </header>
            <table class="table_count">
                <tbody>
                    {element_info_html}
                </tbody>
            </table>
    </body>
    <style>
        {style_table}
    </style> 
    </html>
    '''
    return element_html

@app.route("/info/propertyset")
def info_propertyset():
    # Формирование запроса в базу данных проекта
    cursor_Pset = connection.cursor()
    cursor_Pset.execute('''
    SELECT pset_name, count (pset_name)
    FROM propertyset
    GROUP BY pset_name;
    ''')
    Pset_info = cursor_Pset.fetchall()
    Pset_info_html = ""
    for line in Pset_info:
        Pset_info_html += f"<rt>\n<td>{line[0]}</td>\n<td>{line[1]}</td>\n</tr>"
    # Формирование HTML страницы
    propertyset_html = f'''
    <html lang="ru" >
    <head>
    <meta charset="utf-8">
    <title>Статистика по наборам свойств</title>
    </head>
    <body>
        <header>
        <h1 class="logo">Статистика по наборам свойств</h1>
        <nav>
        <ul class="menu">
        <li><a href="/">Выход в меню</a></li>
        </ul>
        </nav>
        </header>
            <table class="table_count">
                <tbody>
                {Pset_info_html}
                </tbody>
            </table>
    </body>
    <style>
    {style_table}
    </style> 
    </html>
    '''
    return propertyset_html

@app.route("/info/property")
def info_property():
    # Формирование запроса в базу данных проекта
    cursor_info = connection.cursor()
    cursor_info.execute('''
                        SELECT class_ifc, pset_name, prop_name, prop_value
                        FROM relation_element_pset
                        JOIN element ON relation_element_pset.id_element = element.id_guid_element
                        JOIN propertyset ON relation_element_pset.id_pset = propertyset.id_guid_pset
                        JOIN property ON propertyset.id_guid_pset = property.id_pset
                        ''')
    property_info = cursor_info.fetchall()
    property_info_html = ""
    for line in property_info:
        property_info_html += f"<rt>\n<td>{line[0]}</td>\n<td>{line[1]}</td><td>{line[2]}</td>\n<td>{line[3]}</td>\n</tr>"
    # Формирование HTML страницы
    property_html = f'''
    <html lang="ru" >
    <head>
    <meta charset="utf-8">
    <title>Статистика по свойствам</title>
    </head>
    <body>
        <header>
        <h1 class="logo">Вывод информации по свойствам</h1>
        <nav>
        <ul class="menu">
        <li><a href="/">Выход в меню</a></li>
        </ul>
        </nav>
        </header>
            <table class="table_count">
                <tbody>
                {property_info_html}
                </tbody>
            </table>
    </body>
    <style>
    {style_table}
    </style> 
    </html>
    '''
    return property_html

@app.route("/check/property")
def check_property():
    check_property_html = f'''
        <html lang="ru" >
        <head>
        <meta charset="utf-8">
        <title>Проверка наличия свойств</title>
        </head>
        <body>
            <header>
            <h1 class="logo">Проверка наличия свойстви и наборов свойств</h1>
            <nav>
            <ul class="menu">
            <li><a href="/">Выход в меню</a></li>
            </ul>
            </nav>
            <p> <span style="color: red"> Функционал находится в разработке </span> </p>
            </header>
        </body>
        </html>
        '''
    return check_property_html

if __name__ == "__main__":
    app.run()
