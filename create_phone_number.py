def create_phone_number(n):
    n=''.join([str(x) for x in n])


    return ('(' + str(n[0:3]) + ')' + ' ' + str(n[3:6]) + '-' + str(n[6:]))




if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
