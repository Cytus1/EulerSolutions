def find_largest_prime_factor(n):
    factor = 2 ; factor_list = []
    while n != 1:
        if (n % factor != 0): factor += 1       
        else: n = n / factor ; factor_list.append(factor)
    return factor
print(find_largest_prime_factor(600851475143)) # 6857
