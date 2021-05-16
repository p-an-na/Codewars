def is_isogram(word):

    if word.isalpha() == False:
        raise TypeError('Argument should be a string')
    else:
        return (word, len(word) == len(set(word.lower())))


if __name__ == '__main__':
    print(is_isogram('abc'))
    print(is_isogram('helikopter'))
    print(is_isogram('1245'))
