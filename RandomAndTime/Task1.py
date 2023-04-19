"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
import time

ALL_TIME = 15


def move_time() -> int:
    global ALL_TIME
    t1 = time.time()
    move = input()
    t2 = time.time()
    if move == "off":
        return "off"
    elif t2 - t1 <= 0:
        return "off"
    ALL_TIME -= t2 - t1
    return ALL_TIME


res = move_time()
print(res)

while ALL_TIME > 0 and res != "off":
    res = move_time()
    print(res)
