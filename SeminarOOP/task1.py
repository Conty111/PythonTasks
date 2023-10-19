class Work():
    def __init__(self, place: str) -> None:
        self.place = place

    def work_info(self):
        print(f"Working place: {self.place}")

class WorkingStudent(Work):
    def __init__(self, place: str, name: str, edc_place: str) -> None:
        super().__init__(place)
        self.name = name
        self.edc_place = edc_place

    def info(self):
        print(f"Student name: {self.name}")
        print(f"Education place: {self.edc_place}")
        self.work_info()

student1 = WorkingStudent("Beze", "Ahmet", "Sirius")
student1.info()