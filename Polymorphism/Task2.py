"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""

class OlympicParticipant:
    def __init__(self, name: str, all_tests: int, succesfull_tests: int) -> None:
        self.name = name
        self.__all_tests = all_tests
        self.__succesfull_tests = succesfull_tests
    
    def get_all_tests(self) -> int:
        return self.__all_tests
    
    def get_successfull_tests(self) -> int:
        return self.__succesfull_tests


class TransctionsTask(OlympicParticipant):
    def __init__(self, name: str, all_tests: int, succesfull_tests: int) -> None:
        super().__init__(name, all_tests, succesfull_tests)
        self.set_score()

    def set_score(self, score: int = 0) -> None:
        if self.get_all_tests() == self.get_successfull_tests():
            self.__max_score = 100
            return
        self.__max_score = score
    
    def get_score(self) -> int:
        return self.__max_score
    
    def __add__(self, other):
        if type(other) is int:
            self.set_score(self.get_score() + other)
        else:
            self.set_score(self.get_score() + other.get_score())
        return self
        

class SpeedTask(OlympicParticipant):
    def __init__(self, name: str, all_tests: int, succesfull_tests: int, 
                 time_to_solve: float, best_time: float, max_score: float, reduction: float) -> None:
        super().__init__(name, all_tests, succesfull_tests)
        self.time_to_solve = time_to_solve
        self.best_time = best_time
        self.max_score = max_score
        self.reduction = reduction
        self.set_score()
    
    def set_score(self, scores: int = 0) -> None:
        if self.time_to_solve > self.best_time:
            self.__score = self.max_score-(self.time_to_solve-self.best_time)*self.reduction
            return
        if scores != 0:
            self.__score += scores
        else:
            self.__score = self.max_score
    
    def get_score(self) -> int:
        return self.__score

    def __add__(self, other):
        if type(other) is int:
            self.set_score(self.get_score() + other)
        else:
            self.set_score(self.get_score() + other.get_score())
        return self


def main():
    arr = [TransctionsTask(name="Ivan", all_tests=30, succesfull_tests=25), 
           SpeedTask(name="Sergey", all_tests=15, succesfull_tests=10, time_to_solve=20, best_time=15, max_score=150, reduction=2), 
           SpeedTask(name="Ahmet", all_tests=20, succesfull_tests=20, time_to_solve=15, best_time=16, max_score=150, reduction=2), 
           TransctionsTask(name="Ivan", all_tests=30, succesfull_tests=25),
           ]
    
    for student in sorted(arr, key=lambda x: -x.get_score()):
        print(student.name, f"score: {student.get_score()}")


main()