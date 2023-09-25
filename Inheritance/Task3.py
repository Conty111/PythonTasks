"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""

class SpaceObject():
    def __init__(self, size) -> None:
        self.size = size

class Star(SpaceObject):
    def __init__(self, size, brightness) -> None:
        super().__init__(size)
        self.brightness = brightness
    
    def light(self):
        print('Звезда светит с силой', self.brightness)

class Planet(SpaceObject):
    def __init__(self, size, population, growth) -> None:
        super().__init__(size)
        self.population = population
        self.growth = growth

    def calculate_population(self, years):
        ans = self.population + self.growth * years
        print('Население через', years, 'лет будет равно', ans)

s1 = Star(444, 777)
p1 = Planet(444, 700000, 50000)
p1.calculate_population(5)
s1.light()