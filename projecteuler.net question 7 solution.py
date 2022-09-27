#   find nth prime number

factor_list = []
prime_list = [1]


def find_factors(value):
    if value % 2 != 0:
        for check_factor in range(1, value + 1):
            if value % check_factor == 0:
                factor_list.append(check_factor)


i = 1
while len(prime_list) < 10001:
    factor_list = []
    find_factors(i)
    if len(factor_list) == 2:
        prime_list.append(i)
    i += 1

print(prime_list[-1]) # 104743
