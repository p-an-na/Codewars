def nb_year(p0, percent, aug, p):

    n=0

    while p0 <= p:

        p0 = p0 + (p0 * percent/100) + aug


        n += 1

    return n


if __name__ == '__main__':
    nb_year(1000, 2, 50, 1200)
    nb_year(1500, 5, 100, 5000)
    nb_year(1500000, 2.5, 10000, 2000000)