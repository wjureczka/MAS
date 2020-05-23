import uuid

from MAS.models.User.UserAbstract import UserAbstract


class User(UserAbstract):

    _name = None
    _surname = None
    _email = None
    _pesel = None

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.pesel = uuid.uuid4()

    @property
    def pesel(self):
        return self._pesel

    @pesel.setter
    def pesel(self, new_pesel):
        self._pesel = new_pesel

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

