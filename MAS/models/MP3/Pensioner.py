from MAS.models.MP3.Person import Person


class Pensioner(Person):
    type = "Pensioner"

    def __init__(self, name, pension):
        Person.__init__(self, name)
        self.pension = pension

    @staticmethod
    def makePensioner(person, pension):
        new_pensioner = Pensioner(person.getName(), pension)
        return new_pensioner
