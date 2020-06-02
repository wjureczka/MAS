from MAS.models.MP3.Person import Person


class Employee(Person):
    type = "Employee"

    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary

    def getName(self):
        return self.name

    def getSalaryBeforeTax(self):
        return self.salary

    def getSalaryAfterTax(self):
        return self.salary * 0.81
