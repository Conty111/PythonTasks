"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
from threading import Thread
import random
import os

def get_text(path: str) -> str:
    with open(path, "r+") as file:
        return file.readline()


def write_text(path: str, value: str):
    with open(path, "w+") as file:
        file.write(value)


def redact_files(path: str):
    print('Function started')
    # with open(path, "wt+") as file:
    #     file.write(f'ids:{random.randint(10000, 99999)}\n')
    write_text(path, get_text(path).replace('ids', 'id'))


if __name__ == "__main__":
    dir_path = os.getcwd()
    for i in range(10):
        th = Thread(target=redact_files, args=(f"{dir_path}/Threads/Files/file{i}.txt", ))
        th.start()
