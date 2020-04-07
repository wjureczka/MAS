from MAS.models.User.User import User


class LandLord(User):
    _bank_account_number = None

    def __init__(self, name, surname, email, bank_account_number):
        super().__init__(name, surname, email)
        self.bank_account_number = bank_account_number

    @property
    def bank_account_number(self):
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, value):
        self._bank_account_number = value
