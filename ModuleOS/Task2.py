"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""
import os

os.mkdir(os.getcwd() + "/target")
os.chdir(os.getcwd() + "/target")
for i in range(1, 11):
    os.mkdir(os.getcwd() + f"/{i}")