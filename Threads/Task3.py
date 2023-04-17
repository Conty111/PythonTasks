"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import time
from threading import Thread


def faster():
    while True:
        time.sleep(3)
        print("Быстрее!")


if __name__ == "__main__":
    th = Thread(target=faster, daemon=True)
    th.start()
    code = input("Введите код от бомбы!!!  ")
    if code == "12345":
        print("Разминировано")
    else:
        print("Пока пока, бум")
