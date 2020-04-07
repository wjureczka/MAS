from MAS.models.Agreement.RentalAgreement import RentalAgreement


class OccasionalAgreement(RentalAgreement):
    _notary_confirmation = None

    def __init__(self, start_date, end_date, rules_of_use, notary_confirmation):
        super().__init__(start_date, end_date, rules_of_use)
        self.notary_confirmation = notary_confirmation

    @property
    def notary_confirmation(self):
        return self._notary_confirmation

    @notary_confirmation.setter
    def notary_confirmation(self, value):
        self._notary_confirmation = value

    def create_agreement(self):
        pass

    def terminate(self):
        pass
