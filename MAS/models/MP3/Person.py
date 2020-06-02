class Person:
    type = "Person"

    def __init__(self, name, sex="other"):
        self.sex = sex
        self.name = name

    def getName(self):
        return self.name
