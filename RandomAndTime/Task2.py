"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""
import random

countryes = ("Russia", "Armenia", "USA", "Norway", "Sweden")
countryes_dict = dict()


def get_random(countryes_dict: dict) -> tuple:
    values = list(countryes_dict.items())
    a1 = random.choice(values)
    values.remove(a1)
    a2 = random.choice(values)
    if a1[1] > 0 and a2[1] > 0:
        return a1, a2
    return get_random(countryes_dict)


for country in countryes:
    count_people = int(input(f"Число участников сборной {country}: "))
    countryes_dict[country] = count_people

while sum(countryes_dict.values()) > 0:
    if input("Для продолжения введите что-либо, для окончания - off\n") != "off":
        a1, a2 = get_random(countryes_dict)
        countryes_dict[a1[0]] -= 1
        countryes_dict[a2[0]] -= 1

        print(f"\nПловец {a1[0]} - пловец {a2[0]}")
        print(f"Победил пловец из {random.choice([a1, a2])[0]}\n")
        print(f"У сборной {a1[0]} осталось {countryes_dict[a1[0]]} участников(-a)")
        print(f"У сборной {a2[0]} осталось {countryes_dict[a2[0]]} участников(-a)")
    else:
        break
print("Пока")
