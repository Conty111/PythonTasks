""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""
import os

os.mkdir(os.getcwd() + "/task4")
os.chdir(os.getcwd() + "/task4")
with open("answer.txt", mode="+w") as txt:
    txt.write("я выполнил задание")
