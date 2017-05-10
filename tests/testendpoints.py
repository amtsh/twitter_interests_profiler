import json
import nose
from nose.tools import *

from tests import test_app

def test_entities_route():
    response = test_app.get('/')
    # check headers
    check_content_type(response.headers)
    # check status code
    eq_(response.status_code, 200)
    # check body
    body = json.loads(response.data)
    eq_(body, {"app": "interest profiler"})

# Helper functions
def check_content_type(headers):
    eq_(headers['Content-Type'], 'application/json')
