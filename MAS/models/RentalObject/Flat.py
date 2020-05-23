from MAS.models.RentalObject.RentalObject import RentalObject


class Flat(RentalObject):
    def __init__(self, description, area_description, photos, address, price, equipment, rooms=None):
        RentalObject.__init__(self, description, area_description, photos, address, price, equipment)

        if rooms is None:
            rooms = []
        self.rooms = rooms

    def __del__(self):
        print('Deleting Flat: ', self.description)
        for room in self._rooms:
            room.delete_flat_link()

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms = value

    def add_room(self, room):
        # print(room.description, room in self.rooms)
        if room is None or room in self.rooms:
            return

        self.rooms.append(room)
        room.flat = self

    def get_size(self):
        pass

    def delete_room_link(self, room):
        if room in self.rooms:
            self.rooms.remove(room)
