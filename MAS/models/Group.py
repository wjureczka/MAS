class Group:
    _users = None
    _preferred_locations = None
    _preferred_room_quantity = None
    _preferred_size = None
    _budget = None

    def __init__(self, budget, preferred_locations, preferred_room_quantity, preferred_size):
        self._users = {}
        self._budget = budget
        self._preferred_locations = preferred_locations
        self._preferred_room_quantity = preferred_room_quantity
        self._preferred_size = preferred_size

    @property
    def users(self):
        return self._users

    def invite_to_group(self, user):
        print(self.users)
        self.users[user.pesel] = user
        user.assign_to_group(self)

