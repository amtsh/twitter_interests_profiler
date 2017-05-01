import Twitter

def main():
    username = 'twitter'
    print Twitter.get_user_likes(username)
    print Twitter.get_user_timeline(username)

if __name__ == '__main__':
    main()
