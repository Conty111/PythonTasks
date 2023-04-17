a = int(input())

if (a % 10) % 2 == 0 and sum(map(int, str(a))):
    print("YES")
else:
    print("NO")
