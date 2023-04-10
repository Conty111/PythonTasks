"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""
def get_cost(distance: int = 0) -> float:
    assert distance >= 0, "Расстояние не может быть отрицательным."
    return (distance // 140) * 0.25 + 4


def main():
    dist: int = -111
    print(f"Стоимость поездки за {dist} м: {get_cost(distance=dist)}$")


if __name__ == "__main__":
    main()