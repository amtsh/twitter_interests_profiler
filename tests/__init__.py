import nose
from nose.tools import *

from application.server import flask_app

test_app = flask_app.test_client()
