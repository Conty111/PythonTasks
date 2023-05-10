"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open("second_answer.txt", "w+") as text:
    second_sentence = "но у меня не получается"
    text.write(second_sentence)

with open("answer.txt", "r+") as text2:
    first_sentence = text2.readline()
        
with open("third_answer.txt", "w+") as text3:
    text3.write("\n".join([first_sentence, second_sentence]))