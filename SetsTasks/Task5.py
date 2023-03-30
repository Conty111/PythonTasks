"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
6
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English, Japenese]
1 - [English]
"""
languages = set()
count_input = 0
count = int(input())
count_lang = int(input())

while count - count_input > count_lang:
    lang = set()
    for i in range(count_lang):
        lang.add(input())
    res = languages & lang
    languages = languages | lang
    count_input += count_lang
    count_lang = int(input())
else:
    lang = set()
    for i in range(count_lang):
        lang.add(input())    
    res = languages & lang
    languages = languages | lang

print(f"All languages - {list(languages)}")
print(f"All know this language - {list(lang)}")