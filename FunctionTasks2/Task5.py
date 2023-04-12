"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""


def get_data(colors, count_colors, **kwargs):
    print(f"{colors} - {count_colors}")
    for key, item in kwargs.items():
        print(f"{key}: {item}")


def main():
    get_data(colors="Цвета", count_colors="5", red="111", blue="255")


if __name__ == "__main__":
    main()
