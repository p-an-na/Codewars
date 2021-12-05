def get_sum(a,b):
    suma = 0

    if a==b:
        return a
    elif a>b:
        for n in range(b, a+1):
            suma += n
        return suma
    else:
        for n in range (a,b+1):
            suma +=n
        return suma





if __name__ == '__main__':
    print (get_sum(1,0))
    print (get_sum(0,-1))
    print(get_sum(1,1 ))
    print(get_sum(-1,2))