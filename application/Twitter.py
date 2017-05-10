import os
import datetime
import traceback

import tweepy

api_handle = None

def get_authorization():
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY', None)
    TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET', None)

    auth = tweepy.AppAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    return auth

def get_api():
    global api_handle

    if api_handle:
        return api_handle

    print("Connecting to twitter.")
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

def get_user_info(username):
    user = get_user(username)
    return {
        "id": user.id_str,
        "username": user.name,
        "screen_name": user.screen_name,
        "tweets_count": user.statuses_count,
        "following_count": user.friends_count,
        "followers_count": user.followers_count,
        "joined_at": user.created_at,
        "location": user.location
    }

def main():
    pass

if __name__ == '__main__':
    main()
