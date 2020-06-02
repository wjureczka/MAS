from MAS.models.MP3.Employee import Employee
from MAS.models.MP3.Student import Student


class StudentEmployee(Student, Employee):
    type = "StudentEmployee"

    def __init__(self, name, salary):
        Student.__init__(self, name)
        Employee.__init__(self, name, salary)

    def getName(self):
        return self.name

    def getSalaryAfterTax(self):
        return self.salary
