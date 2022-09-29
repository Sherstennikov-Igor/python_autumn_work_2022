# todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
# Цены хранятся в словаре:


prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}


def compute_bill(voucher):
    count = 0
    for key, var in voucher.items():
        count += var
    return count


summ = compute_bill(prices)

print(summ)
