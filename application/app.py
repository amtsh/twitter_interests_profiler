import utils
import os
from Twitter.cleaner import clean, replace_multi_whitespaces
from Twitter import twitter as TW
from GoogleLang import google_lang as GLang

MEMORY_STORE = {}

def get_favorites(username):
    user_likes = MEMORY_STORE.get(username)

    if not user_likes:
        user_likes = TW.get_user_likes(username, 20)
        MEMORY_STORE[username] = user_likes

    response = []
    for tweet in user_likes:
        cleaned_tweet = clean(tweet).strip()
        if cleaned_tweet:
            f = {}
            f['tweet'] = tweet
            f['clean_tweet'] = cleaned_tweet
            response.append(f)
    return response

def get_entities(username, text_body):
    entity_key = username + '_' + 'entities'

    if MEMORY_STORE.get(entity_key):
        return MEMORY_STORE.get(entity_key)

    text_body = replace_multi_whitespaces(text_body)
    text_list = utils.split_string(text_body, 999)

    response = {}
    response['entities'] = []
    response['text'] = []

    for chunk in text_list:
        response['entities'].extend(GLang.get_entities(chunk))
        response['text'].extend(chunk)

    MEMORY_STORE[entity_key] = response
    return response

def user_interests(username):
    tweets = get_favorites(username)

    user_entities = get_entities(username, ' '.join([x['clean_tweet'] for x in tweets]))
    return user_entities

def main():
    pass

if __name__ == '__main__':
    main()
