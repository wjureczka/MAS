from abc import ABC, abstractmethod


class UserAbstract(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def surname(self):
        pass

    @surname.setter
    @abstractmethod
    def surname(self, value):
        pass

    @property
    @abstractmethod
    def email(self):
        pass

    @email.setter
    @abstractmethod
    def email(self, value):
        pass
