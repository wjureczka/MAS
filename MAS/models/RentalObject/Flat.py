from MAS.models.RentalObject.RentalObject import RentalObject


class Flat(RentalObject):
    _rooms = []

    def __init__(self, description, area_description, photos, address, price, equipment, rooms=[]):
        super().__init__(description, area_description, photos, address, price, equipment)
        self.rooms = rooms

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms = value

    def add_room(self, room):
        self._rooms.insert(room)

    def get_size(self):
        pass
