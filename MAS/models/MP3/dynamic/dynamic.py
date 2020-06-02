from MAS.models.MP3.Employee import Employee
from MAS.models.MP3.Pensioner import Pensioner

person = Employee("EmployeeName", 200)

print(person.type, person.__dict__)

person = Pensioner.makePensioner(person, 100)

print(person.type, person.__dict__)
