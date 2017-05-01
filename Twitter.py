import os
import datetime
import traceback

import tweepy

api_handle = None

def get_authorization():
    API_KEY = os.getenv('API_KEY', None)
    API_SECRET = os.getenv('API_SECRET', None)

    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
    return auth

def get_api():
    global api_handle

    if api_handle:
        return api_handle

    print_safe("Connecting to twitter.")
    auth = get_authorization()
    api = tweepy.API(auth, wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True)
    if (not api):
        raise Exception("Cannot connect to twitter using provided credentials.")

    api_handle = api
    return api

def get_user(username):
    api = get_api()
    return api.get_user(username)

def get_user_timeline(username):
    api = get_api()
    return [tweet.text for tweet in api.user_timeline(username)]

def get_user_likes(username):
    api = get_api()
    return [tweet.text for tweet in api.favorites(username)]

def print_user(user):
    print_safe("Id : {}".format(user.id_str))
    print_safe("User : {} @{}".format(user.name, user.screen_name))
    print_safe("Tweets: {}".format(user.statuses_count))
    print_safe("Follows: {}".format(user.friends_count))
    print_safe("Followers: {}".format(user.followers_count))
    # print_safe("Location : {}".format(user.location or 'No Location specified'))
    print_safe("Joined at : {}".format(user.created_at))

def print_safe(text):
    print(text.encode('utf-8'))

def main():
    pass

if __name__ == '__main__':
    main()
