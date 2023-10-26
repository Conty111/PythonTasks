"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""

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