from MAS.models.RentalObject.RentalObject import RentalObject


class Room(RentalObject):
    _flat = None

    def __init__(self, description, area_description, photos, address, price, equipment, size, flat=None):
        RentalObject.__init__(self, description, area_description, photos, address, price, equipment)
        self.size = size
        self.flat = flat

    def __del__(self):
        print('Deleting room: ', self.description)
        if self.flat is not None:
            self.flat.delete_room_link(self)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def flat(self):
        return self._flat

    @flat.setter
    def flat(self, value):
        if self.flat is not None:
            self.flat.delete_room_link(self)

        if value is not None:
            value.add_room(self)

        self._flat = value

    def delete_flat_link(self):
        self.flat = None
