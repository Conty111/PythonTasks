"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def check(name: str = None, surname: str = None, age: int = None) -> str:
    if name and surname and age:
        return f"{name} {surname}, {age} лет"
    return "You didn't type all arguments"


def main():
    print(check(name="Дима", surname="Барыга", age=15))


if __name__ == "__main__":
    main()
