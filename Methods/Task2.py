"""
Класс Vector3D
Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
Обязательно должны быть реализованы методы:
– приведение вектора к строке с выводом кооржинат (метод __str __),
– сложение векторов оператором `+` (метод __add__),
– вычитание векторов оператором `-` (метод __sub__),
– скалярное произведение оператором `*` (метод __mul__),
"""


class Vector3D():
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"x: {self.x}\ny: {self.y}\nz: {self.z}"

    def __add__(self, obj):
        self.x += obj.x
        self.y += obj.y
        self.z += obj.z
        return self

    def __sub__(self, obj):
        self.x -= obj.x
        self.y -= obj.y
        self.z -= obj.z
        return self

    def __mul__(self, obj):
        self.x *= obj.x
        self.y *= obj.y
        self.z *= obj.z
        return self


v1 = Vector3D(0, 1, 2)
v2 = Vector3D(1, 5, 1)
print(v1 * v2)
