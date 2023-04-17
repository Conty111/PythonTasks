games = []
a = input()
while a != "0":
    if a not in games:
        games.append(a)
    else:
        print("Эта игра уже записана")
    a = input()
games.sort()
print(games)
