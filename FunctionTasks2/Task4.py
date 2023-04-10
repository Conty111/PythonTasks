"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def cacluate(*args) -> tuple:
    mean_value: float = sum(args)/len(args)
    return mean_value, list({float() for i in args if i > mean_value})


def main():
    print(cacluate(1, 2, 3, 2, 3, 2, 3))


if __name__ == "__main__":
    main()