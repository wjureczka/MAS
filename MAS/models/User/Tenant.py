from MAS.models.User.User import User


class Tenant(User):
    _sent_rental_object_opinions = None
    _groups_belonging = None

    def __init__(self, name, surname, email):
        super().__init__(name, surname, email)
        self._sent_rental_object_opinions = []
        self._groups_belonging = []

    @property
    def sent_rental_object_opinions(self):
        return self._sent_rental_object_opinions

    def add_object_opinion(self, opinion):
        self._sent_rental_object_opinions.append(opinion)

    @property
    def groups_belonging(self):
        return self._groups_belonging

    def assign_to_group(self, group):
        self._groups_belonging.append(group)
