"""
Создайте матрицу размером 3х3 и выведите значения с индексами 1,2 и 3,3
"""
n, m = 3, 3
matr = [[i for i in range(n)] for _ in range(m)]
print(matr)
print(matr[0][1], matr[2][2])
