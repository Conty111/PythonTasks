category = input("Категория товара: ")

if category == "продукты":
    cost = int(input("Сумма: "))
    if cost < 100:
        print("Попробуйте нашу выпечку!")
    elif 100 <= cost < 500:
        print("Как насчёт орехов в шоколаде?")
    else:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома!")
