import os
import sys

required_vars = ['TWITTER_API_KEY', 'TWITTER_API_SECRET']

if not all([env_var in os.environ for env_var in required_vars]):
    print "Environment Variables not set.", repr(required_vars)
    sys.exit(0)
