# from is_prime import is_prime_v2, is_prime_v1
import is_prime

def list_of_primes_in_interval_v1(start,stop):
    list_of_prime=[]
    for i in range(start,stop+1):
        if is_prime.is_prime_v1(i)==True:
            list_of_prime.append(i)
    return list_of_prime


def list_of_primes_in_interval_v2(a, b):
    primes_list = []
    for nr in range(a, b + 1):
        if is_prime.is_prime_v2(nr):
            primes_list.append(nr)
    return primes_list


def list_of_primes_in_interval_v3(a, b):
    primes_list = []
    for nr in range(a, b + 1):
        prime = True
        for i in range(2, nr):
            if nr % i == 0:
                prime = False

        if prime:
            primes_list.append(nr)
    return primes_list