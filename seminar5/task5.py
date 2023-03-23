a = list(map(int, input().split()))
if a == list(range(a[0], a[-1] + 1)):
    print("YES")
else:
    print("NO")