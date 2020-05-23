from MAS.models.RentalObject.RentalObject import RentalObject


class Flat(RentalObject):
    def __init__(self, description, area_description, photos, address, price, equipment, rooms=None):
        RentalObject.__init__(self, description, area_description, photos, address, price, equipment)

        if rooms is None:
            rooms = []
        self.rooms = rooms

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms = value

    def add_room(self, room):
        if room is None or room in self.rooms:
            return

        self.rooms.append(room)
        room.flat = self

    def get_size(self):
        pass

    def delete_room_link(self, room):
        if room in self.rooms:
            self.rooms.remove(room)
