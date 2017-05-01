import Twitter
import GoogleLang

def print_safe(text):
    print(text.encode('utf-8'))

def main():
    username = 'twitter'

    for tweet in Twitter.get_user_likes(username):
        print_safe(tweet)
        print(GoogleLang.get_entities(tweet))

if __name__ == '__main__':
    main()
