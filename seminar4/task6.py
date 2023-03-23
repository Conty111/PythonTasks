a = int(input())

while a != 0:
    while a % 2 == 0:
        a /= 2
    print("К оплате:", a - a*0.15)
    a = int(input())