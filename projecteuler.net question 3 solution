import logging
import math
logging.basicConfig(level=logging.DEBUG)


#   find factor with optimization
def find_factor(value):
    factors = []
    for check_factor in range(1, int(math.sqrt(value)) + 1):
        if value % check_factor == 0:
            factors.append(check_factor)
            factors.append(value // check_factor)
    return factors


logging.debug(find_factor(17))


#   detect if it is prime
def is_prime(value):
    return len(find_factor(value)) == 2


logging.debug("Check for prime: %s" % (is_prime(17)))

#   detect the largest prime
factors_find = find_factor(600851475143)
largest_prime_factor = 0
for factor in factors_find:
    if is_prime(factor) and factor > largest_prime_factor:
        largest_prime_factor = factor

print(largest_prime_factor)  # 6857

#   I had finished this attempt under the guidance of the following video. https://www.youtube.com/watch?v=Y3n-PA3QoAE
