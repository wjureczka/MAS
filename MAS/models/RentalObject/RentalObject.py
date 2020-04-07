class RentalObject:
    _description = None
    _area_description = None
    _photos = []
    _address = None
    _price = None
    _equipment = None

    def __init__(self, description, area_description, photos, address, price, equipment):
        self.description = description
        self.area_description = area_description
        self.photos = photos
        self.address = address
        self.price = price
        self.equipment = equipment

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def area_description(self):
        return self._area_description

    @area_description.setter
    def area_description(self, value):
        self._area_description = value

    @property
    def photos(self):
        return self._photos

    @photos.setter
    def photos(self, value):
        self._photos = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, value):
        self._equipment = value

    def post_opinion(self, opinion):
        pass

    def list_objects(self):
        pass

    def list_objects(self, price):
        pass

