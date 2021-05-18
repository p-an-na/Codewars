def maskify(cc):

    if len(cc) > 4:
        cc = cc[-4:].rjust(len(cc), '#')

    return cc



if __name__ == '__main__':
    print(maskify('maskify'))
    print(maskify('ala'))
    print(maskify('1234'))

