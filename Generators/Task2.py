"""
Пусть дан текст:

t = "Генератор – это итератор, элементы которого
можно перебирать (итерировать) только один раз.
Итератор – это объект, который поддерживает функцию next()
для перехода к следующему элементу коллекции."

Написать функцию-генератор для выделения слов из этого текста (слова разделяются пробелом, либо переносом строки ‘\n’).
"""


def get_words(text: str) -> str:
    yield text.replace("\n", " ").split()


t = """Генератор – это итератор, элементы которого
можно перебирать (итерировать) только один раз.
Итератор – это объект, который поддерживает функцию next()
для перехода к следующему элементу коллекции."""

for word in get_words(t):
    print(word)
