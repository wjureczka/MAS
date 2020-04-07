class Group:
    _users = []
    _preferred_locations = []
    _preferred_room_quantity = None
    _preferred_size = None
    _budget = None

    def __init__(self, users, budget, preferred_locations, preferred_room_quantity, preferred_size):
        self.users = users
        self.budget = budget
        self.preferred_locations = preferred_locations
        self.preferred_room_quantity = preferred_room_quantity
        self.preferred_size = preferred_size

    def invite_to_group(self, user):
        self._users.append(user)

