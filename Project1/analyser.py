from data import DATA_OUTPUT, DATA_ANALYS
import random
import os
import time


def make_answer(response) -> list:
    output = []
    for word in response:
        value = check_text(word)
        if value:
            if DATA_OUTPUT[value] == "game":
                russian_game()
                output.append("Хорошая игра)))")
            elif DATA_OUTPUT[value] not in output:
                output.append(DATA_OUTPUT[value])
    if not output:
        output.append("Не понимаю вас...")
    return output


def check_text(text: str) -> str:
    for word in DATA_ANALYS.keys():
        if word in text.lower():
            return DATA_ANALYS[word]


def get_response() -> list:
    response = input("Что вы хотите?!\n").split()
    return response


def print_output(answer: list):
    for output in answer:
        if type(output) is str:
            print(f"{output}")
        else:
            for val in output.items():
                print(f"{val[0]}: {val[1]}")
        print()


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
