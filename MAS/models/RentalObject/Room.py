import weakref

from MAS.models.RentalObject.RentalObject import RentalObject


class Room(RentalObject):
    _flat = None

    def __init__(self, description, area_description, photos, address, price, equipment, size):
        RentalObject.__init__(self, description, area_description, photos, address, price, equipment)
        self.size = size

    def __del__(self):
        try:
            if self.flat is not None:
                self.flat.delete_room_link(self)
        except Exception as exception:
            print('Room already deleted', self.description)

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

        if value is None:
            self._flat = None
            del self
            return

        self._flat = weakref.proxy(value)
