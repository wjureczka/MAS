from MAS.models.RentalObject.RentalObject import RentalObject


class Flat(RentalObject):
    _size = None

    def __init__(self, description, area_description, photos, address, price, equipment, size):
        super().__init__(description, area_description, photos, address, price, equipment)
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def create_room(self):
        pass
