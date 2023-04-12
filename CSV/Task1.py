"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""
import csv

if __name__ == "__main__":
    with open("CSV/Task1.csv", mode="r+", encoding="UTF-8") as text:
        table = csv.reader(text, delimiter=";")
        for i in table:
            print(i[0], i[1])
