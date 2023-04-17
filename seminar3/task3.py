a = float(input())
b = float(input())
c = float(input())
if a < b < c:
    print("Акция! К оплате:", 0.5 * (a + b + c))
elif a > b > c:
    print("Акция! К оплате:", (a + b + c) / 3)
else:
    print("К оплате:", a + b + c)
