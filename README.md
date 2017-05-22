# Twitter Interests Profiler

## How to use

```
export TWITTER_API_KEY = 'Insert Twitter API KEY here'
export TWITTER_API_SECRET = 'Insert Twitter API SECRET here'
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
```

Run webserver
```
python application/server.py
```
Get Interests
```
Open your browser to http://127.0.0.1:8080//api/interests/<your-twitter_username>
```
## How to run tests

Make sure you have 'nosetests' installed. If not use following command:
```
easy_install nose
```

Run tests
```
./testrunner.sh
```

## To Do
- Create a webpage to display the interests for a given twitter-username
- Deploy it to Heroku/AWS/Google Cloud
- Basic analytics to show topic weight based on occurence
- Recommend content from Youtube, Medium based on topics.
