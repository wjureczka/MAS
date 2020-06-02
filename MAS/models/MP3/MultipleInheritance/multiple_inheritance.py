from MAS.models.MP3.Employee import Employee
from MAS.models.MP3.Student import Student
from MAS.models.MP3.StudentEmployee import StudentEmployee


employee = Employee("EmployeeName", 1000)
student = Student("StudentName")
student_employee = StudentEmployee("StudentEmployeeName", 1000)


print(student, student.type, student.getName(), student.addGrade(10), student.grades)

print(employee, employee.type, employee.salary, employee.getName(), employee.getSalaryBeforeTax(), employee.getSalaryAfterTax())

print(student_employee,
      student_employee.type,
      student_employee.salary,
      student_employee.getName(),
      student_employee.addGrade(20),
      student_employee.grades,
      student_employee.getSalaryBeforeTax(),
      student_employee.getSalaryAfterTax()
      )