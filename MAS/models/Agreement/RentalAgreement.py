from abc import ABC, abstractmethod


class RentalAgreement(ABC):
    _start_date = None
    _end_date = None
    _rules_of_use = []
    _max_rules_of_use = 30

    def __init__(self, start_date, end_date, rules_of_use=[]):
        self.start_date = start_date
        self.end_date = end_date
        self.rules_of_use = rules_of_use

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @property
    def rules_of_use(self):
        return self._rules_of_use

    @rules_of_use.setter
    def rules_of_use(self, value):
        if len(value) <= 30:
            self._rules_of_use = value
        else:
            raise Exception("Too much rules of use: {}".format(len(value)))

    def list_agreements(self):
        pass

    @abstractmethod
    def create_agreement(self):
        pass

    @abstractmethod
    def terminate(self):
        pass
