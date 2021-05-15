def digital_root(n):
    sum_of_digits = sum(int(digit) for digit in str(n))
    return sum_of_digits



if __name__ == '__main__':
    print(digital_root(15))



