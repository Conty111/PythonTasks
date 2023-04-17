width = float(input("Введите ширину поверхности "))
height = float(input("Введите длину поверхности "))
rashod = float(input("Введите расход краски в кв.м/л "))
volume = int(input("Введите объём одной банки "))
reserve = int(input("Введите процент запаса "))

square = width * height
litr_count = (square / rashod) * (reserve / 100) + (square / rashod)
count_bak = litr_count // volume + 1

print(
    round(square, 2),
    round(litr_count, 2),
    int(count_bak),
    round(count_bak * volume - litr_count, 2),
    sep="\n",
)
