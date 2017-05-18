def split_string(text, n):
    return (text[i:i+n] for i in range(0, len(text), n))
