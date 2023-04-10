"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""
from datetime import date


class Person:

    name: str
    age: int
    
    def __init__(self, name: str, year: int) -> None:
        self.name = name
        self.age = date.today().year - year


    def get_info(self) -> str:
        return f"Имя - {self.name}\nВозраст - {self.age}"


    @staticmethod
    def check_age(age) -> bool:
        return age >= 18