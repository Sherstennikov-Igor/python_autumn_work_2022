# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html
# template = """
# <!DOCTYPE HTML>
# <html>
#  <head>
#   <title> ? </title>
#   <meta charset=?>
#  </head>
#  <body onload="alert(?)">
#
#   <p>?</p>
#
#  </body>
# </html>
# """

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

temp = open("template.txt", "rt")
f = open("index.html", "wt")

lines = temp.readlines()

for line in lines:
    flag = 0
    for key, var in page.items():
        if key in line:
            flag = 1
            piece = line.split("?")
            f.write(piece[0] + var + piece[1])
    if flag == 0:
        f.write(line)

temp.close()
f.close()
print("Создание файла выполнено")
