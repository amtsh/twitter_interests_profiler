import os
import sys

required_vars = ['GOOGLE_APPLICATION_CREDENTIALS']

if not all([env_var in os.environ for env_var in required_vars]):
    print "Environment Variables not set.", repr(required_vars)
    sys.exit(0)
