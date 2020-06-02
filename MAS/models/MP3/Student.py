from MAS.models.MP3.Person import Person


class Student(Person):
    type = "Student"

    def __init__(self, name):
        Person.__init__(self, name)
        self.grades = []

    def getName(self):
        return self.name

    def addGrade(self, grade):
        self.grades.append(grade)