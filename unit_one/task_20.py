#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла import_this.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

f = open("import_this.txt", "rt")

lines = f.readlines()
lines.reverse()
lines = [line.rstrip() for line in lines]
print("\n".join(lines))

f.close()
