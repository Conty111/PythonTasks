"""
Создайте программу выводящую информацию о системе вида:
Операционная система - ХХХ
Имя компьютера - ХХХ
Имя пользователя - ХХХ
"""
import os

print(f"Операционная система - {os.name}")
print(f"Имя компьютера - {os.uname().nodename}")
print(f"Имя пользователя - {os.getlogin()}")
