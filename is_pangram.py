import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    s = set(s.lower())

    if alphabet.issubset(s):
        return True
    return False

#set(string.ascii_lowercase).issubset(s.lower())





if __name__ == '__main__':
    print(is_pangram("The quick, brown fox jumps over the lazy dog!"))