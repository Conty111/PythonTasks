"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def get_IMT(weight: float, height: float) -> float:
    index = weight / (height ** 2)
    assert index > 0, "Incorrect values"
    if index < 18.5:
        return f"Недостаточный вес (ИМТ - {index})"
    elif index > 25:
        return F"Избыточный вес (ИМТ - {index})"
    return f"Ваш ИМТ ({index}) в норме"


if __name__ == "__main__":
    height: float = float(input('Введите рост: '))
    weight: float = float(input('Введите вес: '))
    print(get_IMT(weight=weight, height=height))
