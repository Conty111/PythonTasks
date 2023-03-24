food = input("Что желаете?")
if food.lower() == "завтрак":
    print("Рекомендуем кашу")
elif food.lower() == "обед" or food.lower() == "ужин":
    mnoga_or_no = input("Плотно/не плотно?")
    if mnoga_or_no.lower() == "плотно":
        print("Съешьте плов")
    else:
        print("Покушайте котлетку с пюрешкой")