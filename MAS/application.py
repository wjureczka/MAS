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
