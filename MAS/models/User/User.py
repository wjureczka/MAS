from MAS.models.User.UserAbstract import UserAbstract


class User(UserAbstract):

    _name = None
    _surname = None
    _email = None

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

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

