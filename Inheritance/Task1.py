"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""

class Hero():
    def __init__(self, name, health, armor) -> None:
        self.name = name
        self.health = health
        self.armor = armor

    def print_info(self):
        print('Герой', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor, '\n')


class Magician(Hero):
    _damage = 7

    def hello(self):
        print('Из-за леса из-за гор появляется...')
        self.print_info()

    def attack(self, enemy: Hero):
        print('[HIT] Ныааааа, получай', self._damage*(-1), 'по лицу')
        if enemy.armor > self._damage:
            enemy.armor -= self._damage
        elif enemy.armor == self._damage:
            print('Герой', enemy.name, 'остался без щита!')
            enemy.armor = 0
        else:
            print('Герой', enemy.name, 'остался без щита!')
            enemy.health -= (self._damage-enemy.armor)
            if enemy.health <= 0:
                print('[DEATH] Умер герой', self.name)
        enemy.print_info()