def is_prime_v1(nr):
    prime=True
    for i in range(2,nr):
        if nr%i==0:
            prime=False
    return prime


def is_prime_v2(nr):
    import math
    end_search_range = int(math.sqrt(nr))

    if nr == 1:
        return False
    if nr == 2:
        return True
    elif nr > 2 and nr % 2 == 0:  # if the number is even, we return really fast
        return False

    for divisor in range(3, end_search_range + 1, 2):  # we now only search through odd numbers smaller than
        if nr % divisor == 0:  # squared root of the number!
            return False  # if nr = sqrt(nr) * sqrt(nr), lets say sqrt(nr) * sqrt(nr) = a * b
    return True  # => 3 cases: a>sqrt(nr) , b<sqrt(nr), a,b = sqrt(nr), a<sqrt(nr) b>sqrt(nr)
