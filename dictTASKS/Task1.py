"""
Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
"""
a = dict()
for i in range(11):
    a[i] = i**3
print(a)
