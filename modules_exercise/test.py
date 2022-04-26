# Create a new directory called modules_exercise inside your pycharm project.
# Inside modules_exercise, create a new file named is_prime.py and put in there all the previously defined is_prime implementations.
# Then create a file named primes_in_interval.py and put the list_of_primes_in_interval functions in there.
# 1. Let`s create a 3rd test.py file and using the import statement, import everything from is_prime.py and try to call is_prime_v2(13) and print the result.
# 1.1. (Bonus) Being in test.py, let try to actually test the function, not just print the result, so...
#      How can we make sure that our is_prime returns the expected result?, if it doesnt return the expected result, it should throw an expection... (tip: it is a specific statement)
# 2. Now, try to import the list_of_primes_in_interval_v3 function from primes_in_interval.py module, call it with 5, 35 and print its result.
# 2.2. Do the testing as well :).
# 3. Now let`s try to do the same with list_of_primes_in_interval_v2 function, what do we observe? What should we do?

# ex1
from is_prime import *
print(is_prime_v2(13))

assert is_prime_v2(13) == True
assert is_prime_v2(8) == False

# ex2
from primes_in_interval import list_of_primes_in_interval_v3, list_of_primes_in_interval_v2
print(list_of_primes_in_interval_v3(5, 35))

# ex3
print(list_of_primes_in_interval_v2(3, 35))