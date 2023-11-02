"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""

class Duck():
    def sound(self):
        print("КРЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ")
    
    def wear_suit(self):
        print("Дональд дак в костюмчике, ну ничего себе")


class Human():
    def sound(self):
        print("Я тупая человечина, хочу быть уткой")

    def wear_suit(self):
        print("Костюмчик сел хорошо, но на утке смотрится лучше...")

h1 = Human()
d1 = Duck()
d2 = Duck()

for animal in [d1, h1, d2]:
    animal.sound()
    animal.wear_suit()