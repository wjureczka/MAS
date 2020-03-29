import os

from flask import Flask


application = Flask(__name__)


@application.route('/')
def hello():
    return os.environ.get('DEBUG')


application.run()