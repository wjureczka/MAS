import os
import dill

from flask import Flask


# application = Flask(__name__)
#
# @application.route('/')
# def hello():
#     return os.environ.get('DEBUG')

# application.run()
from MAS.models.Group import Group
from MAS.models.Opinion import Opinion
from MAS.models.User.Tenant import Tenant
from MAS.models.RentalObject.Flat import Flat
from MAS.models.RentalObject.Room import Room


# start zwykła asocjacja
print('---------- zwykła asocjacja')
tenant = Tenant("Name", "Surname", "Email")
opinion = Opinion(tenant, "Opinion", "0")

for opinion in tenant.sent_rental_object_opinions:
    print(opinion.comment, opinion.rate)

print(opinion.author.name, opinion.author.surname)
print('--------------------------')
# koniec zwykła asocjacja

# start asocjacja kwalifikowana
print('---------- asocjacja kwalifikowana')

tenant_with_group = Tenant("Tenant", "With", "Group")
group = Group(1000, [], 1, 50)
group.invite_to_group(tenant_with_group)

print(tenant_with_group.groups_belonging, tenant_with_group.groups_belonging[0])
print(group.users[tenant_with_group.pesel], group.users[tenant_with_group.pesel].name)
print('--------------------------')
# koniec asocjacja kwalifikowana

# start kompozycja
flat1 = Flat("Flat1", "Flat1", "Flat1", "Flat1", "Flat1", "Flat1")
flat2 = Flat("Flat2", "Flat2", "Flat2", "Flat2", "Flat2", "Flat2")

room1 = Room("Room1", "Room1", "Room1", "Room1", "Room1", "Room1", "Room1")
room2 = Room("Room2", "Room2", "Room2", "Room2", "Room2", "Room2", "Room2")
room3 = Room("Room3", "Room3", "Room3", "Room3", "Room3", "Room3", "Room3")
room4 = Room("Room4", "Room4", "Room4", "Room4", "Room4", "Room4", "Room4")
room5 = Room("Room5", "Room5", "Room5", "Room5", "Room5", "Room5", "Room5")

flat1.add_room(room1)
flat1.add_room(room2)

flat2.add_room(room3)
flat2.add_room(room4)
flat2.add_room(room5)

print('Flat1:')
for room in flat1.rooms:
    print('\t', room.size)
print('-------------')

print('Flat2:')
for room in flat2.rooms:
    print('\t', room.size)
print('-------------')


print('Delete room1 from flat1')
room1.flat = None
del room1
print('-------------')

print('Flat1:')
for room in flat1.rooms:
    print('\t', room.description)
print('-------------')

print('Change flat for room2 from flat1 to flat2')
room2.flat = flat2
print('-------------')
print('Change flat for room4 from flat2 to flat1')
room4.flat = flat1
print('-------------')

print('Flat1:')
for room in flat1.rooms:
    print('\t', room.description)
print('-------------')

print('Flat2:')
for room in flat2.rooms:
    print('\t', room.description)
print('-------------')

print('Change flat for room5 from flat2 to None')
room5.flat = None
print('-------------')

print('Flat1:')
for room in flat1.rooms:
    print('\t', room.description)
print('-------------')

print('Flat2:')
for room in flat2.rooms:
    print('\t', room.description)
print('-------------')

print('Delete flat2')
del flat2
try:
    print(room3.description, room3.flat)
except Exception as e:
    print(e)
print('-------------')

print('Flat1:')
for room in flat1.rooms:
    print('\t', room.description)
print('-------------')
try:
    print(room1.description, room1.flat)
except Exception as exception:
    print('Room1 already deleted')
try:
    print(room2.description, room2.flat)
except Exception as exception:
    print('Room2 already deleted')
try:
    print(room3.description, room3.flat)
except Exception as exception:
    print('Room3 already deleted')
try:
    print(room4.description, room4.flat)
except Exception as exception:
    print('Room1 already deleted')
try:
    print(room5.description, room5.flat)
except Exception as exception:
    print('Room5 already deleted')
print('------------------------------------------')

# end kompozycja