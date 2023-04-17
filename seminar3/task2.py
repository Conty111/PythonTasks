time_buy = int(input("Время покупки (какой час): "))
cost = float(input("Сумма покупки: "))
if 10 <= time_buy <= 12:
    cost /= 2
elif 20 <= time_buy <= 22:
    cost /= 4
elif time_buy > 22 or time_buy < 8:
    print("Мы не работаем в это время")
print("К оплате:", cost)
