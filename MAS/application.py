import os
import pickle

from flask import Flask

from MAS.models.Opinion import Opinion

# application = Flask(__name__)
#
# @application.route('/')
# def hello():
#     return os.environ.get('DEBUG')

# application.run()


fileToOpen = None
fileName = 'dump'

try:
    fileToOpen = open(fileName, 'rb')
    data = pickle.load(fileToOpen)

    fileToOpen.close()

    print(data.comment)

    exit()
except IOError:
    print("Plik nie istnieje kurde")

opinion0 = Opinion("Heheszki0", "0")
opinion1 = Opinion("Heheszki1", "1")
opinion2 = Opinion("Heheszki2", "2")
opinion3 = Opinion("Heheszki3", "3")
opinion4 = Opinion("Heheszki4", "4")
opinion5 = Opinion("Heheszki5", "5")

file = open(fileName, 'wb')

pickle.dump(opinion0, file)

file.close()

print(opinion0.comment)

# <MAS.models.Opinion.Opinion object at 0x7fb3b8afd978>