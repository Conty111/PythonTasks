lector = [["Фамилия"], ["Должность"], ["Количество студентов во всех группах"]]
for i in lector:
    a = input(f"{i[0]}: ")
    i.append(a)
print(lector)