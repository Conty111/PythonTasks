import os
import time
import random
import subprocess
# from threading import Thread


def russian_game():
    print("Русссская рулетка! Сыграем?)")
    print('''Правила игры таковы: угадайте случайное число от 1 до 6, и ваш компуктер останется жив!\nКоличество правильных чисел зависит от выбранного вами уровня сложности.''')
    value = input("1 - 1 патрон, 2 - 2 патрона и т.д. (Макс. уровень - 5)\n")
    while value:
        value = int(value)
        if value > 0 and value < 6:
            wrong_ans = [str(random.randint(1, 5)) for _ in range(value)]
            shoot = input("Итак, числа загаданы, на кону жизнь вашего компуктера. Выбирайте!\n")
            if shoot and shoot.isdigit():
                if shoot not in wrong_ans:
                    print("Повезло повезло")
                else:
                    for sec in range(5, 1, -1):
                        print(f"До выключения {sec}...")
                        time.sleep(1)
                    os.system("reboot")
            else:
                print('Не люблю жалких хитрецов... Пока')
                exit()
            value = input("1 - 1 патрон, 2 - 2 патрона и т.д. (Макс. уровень - 5)\n")
        else:
            print("Вы ввели что-то не то... Попробуйте ещё раз\n")
            value = input()


def ricroll():
    # while True:
        # x = subprocess.Popen(['/bin/curl', 'ascii.live/can-you-hear-me'], stdin=False)
        # x.wait()
    os.system('curl ascii.live/can-you-hear-me')