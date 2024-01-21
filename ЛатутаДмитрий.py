

class BeeElephant():
    def __init__(self, bee: int, elephant: int) -> None:
        self.bee = bee
        self.elephant = elephant
        self.recovery()
    
    def fly(self) -> bool:
        return self.bee >= self.elephant

    def trumpet(self) -> str:
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo!"
        return "wzzzzz"
    
    def recovery(self) -> None:
        if self.bee < 0:
            self.bee = 0
        elif self.bee > 100:
            self.bee = 100

        if self.elephant < 0:
            self.elephant = 0
        elif self.elephant > 100:
            self.elephant = 100

    def eat(self, meal: str, value: int) -> None:
        if value < 0:
            print("How does it possible?")
        elif meal == "grass":
            self.elephant += value
            self.bee -= value
        elif meal == "nectar":
            self.elephant -= value
            self.bee += value
        else:
            print("I don't eat it.")

        self.recovery()
    
    def get_parts(self) -> [int]:
        return [self.bee, self.elephant]
    

animal1 = BeeElephant(50, 50)
animal2 = BeeElephant(45, 55)
animal3 = BeeElephant(70, 30)
animal4 = BeeElephant(10, 90)

# ????? Это в процентах??????
# а остальное проверять на то, чтобы в сумме 100
animal1.eat("grass", 3)

print(animal1.get_parts())
print(animal2.fly())
print(animal3.trumpet())
print(animal4.trumpet())