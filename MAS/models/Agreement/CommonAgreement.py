from MAS.models.Agreement.RentalAgreement import RentalAgreement


class CommonAgreement(RentalAgreement):

    def __init__(self, start_date, end_date, rules_of_use):
        super().__init__(start_date, end_date, rules_of_use)

    def prolong(self):
        pass

    def create_agreement(self):
        pass

    def terminate(self):
        pass
