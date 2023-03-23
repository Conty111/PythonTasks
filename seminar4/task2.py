import random

start = input()

if start == "game":
    while start != "off":
        print("Угадай число! У вас есть 3 попытки:")
        b = random.randint(0, 5)
        for i in range(3):
            a = input()
            if int(a) == b:
                print("Вы выиграли билет на концерт!")
                break
            else:
                print("Неа")
        else: 
            print('Попытки кончились.')
        print('Если хотите начать новую игру - введите "game". Чтобы выйти - введите "off".')
        start = input()
        while start != "off" and start != "game":
            start = input()
        