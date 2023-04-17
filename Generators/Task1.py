"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""
string = input()
ans = (let for let in string if let.isalpha())
for letter in ans:
    print(letter, end="")
