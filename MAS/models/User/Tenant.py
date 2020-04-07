from MAS.models.User.User import User


class Tenant(User):

    def __init__(self, name, surname, email):
        super().__init__(name, surname, email)
