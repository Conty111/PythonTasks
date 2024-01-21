"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""
class Profile:
    def __init__(self, name: str, last_name: str, age: int, pasport: str) -> None:
        self.name = name
        self.age = age
        self._last_name = last_name
        self.__pasport = pasport

    def print_info(self) -> None:
        print(f"""
            Name: {self.name},\n
            Last name: {self._last_name},\n
            Age: {self.age}
        """)


class Address:
    def __init__(self, city: str, street: str, zipcode: str) -> None:
        self._city = city
        self._street = street
        self._zipcode = zipcode


class Role:
    def __init__(self, role, hours_worked) -> None:
        self.role = role
        self.hours_worked = hours_worked


class BankAccount():
    def __init__(self, name: str, balance: float, pasport: str, password: str) -> None:
        self._name = name
        self.__balance = balance
        self.__pasport= pasport
        self.__password = password
    
    def get_balance(self) -> float:
        return self.__balance
    
    def get_pasport(self) -> str:
        return self.__pasport
    
    def set_pasport(self, pasport: str, password: str) -> bool:
        if password == self.__password:
            self.__pasport = pasport
            return True
        return False
    
    def del_pasport(self, password: str) -> bool:
        if password == self.__password:
            del self.__pasport
            return True
        return False
    
    def set_balance(self, money: float):
        if not money < 0:
            self.__balance = money
        else:
            self.__balance = 0



class Order:
    def __init__(self, item, date, delivery, price) -> None:
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price


class User:
    def __init__(self) -> None:
        self.profile = None