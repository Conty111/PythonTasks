"""
Напишите программу, которая будет складывать числа, введенные поль-
зователем. Сигналом к окончанию ввода должна служить пустая строка.
Отобразите на экране сумму значений (или 0.0, если пользователь сразу
же пропустил ввод). Решите эту задачу с использованием рекурсии. В ва-
шей программе не должны присутствовать циклы.
Подсказка. В теле вашей рекурсивной функции должен производиться запрос одно-
го числа у пользователя, после чего должно быть принято решение о том, произво-
дить ли еще один рекурсивный вызов. Ваша функция не должна принимать аргумен-
тов, а возвращать будет числовое значе
"""


def calc(example: str) -> float:
    return sum(map(float, example.split()))


def calc2(count=0):
    string = input("Введите число:")
    if string:
        print(f"Сумма: {int(string) + count}")
        return calc2(count=int(string) + count)
    print("Пока")


def main():
    res = input("Введите числа через пробел: ")
    while res:
        print("Сумма:", calc(res))
        res = input("Введите числа через пробел: ")
    print("пока")


def main2():
    calc2()


if __name__ == "__main__":
    # main()
    main2()
