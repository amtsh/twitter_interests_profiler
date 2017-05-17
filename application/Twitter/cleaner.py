import re
import string
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

def remove_urls(text):
    return re.sub('https?\S+', '', text)

def remove_hashtags(text):
    return re.sub('#\S+', '', text)

def remove_mentions(text):
    return re.sub('@\S+', '', text)

def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in cachedStopWords])

def replace_multi_whitespaces(text):
    return ' '.join(text.split())

def remove_punctuation(text):
    return ''.join([c for c in text if c not in string.punctuation])

def remove_unicode_notation(text):
    return text.decode('unicode_escape').encode('ascii','ignore')

def clean(text):
    text = remove_urls(text)
    text = remove_hashtags(text)
    text = remove_mentions(text)
    text = replace_multi_whitespaces(text)
    text = remove_stopwords(text)
    text = remove_punctuation(text)
    text = remove_unicode_notation(text)
    return text

def main():
    pass

if __name__ == '__main__':
    main()
