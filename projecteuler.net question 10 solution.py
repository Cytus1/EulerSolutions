import math
factor_list = []
prime_list = [1]


def find_factors(value):
    factor_list.append(value)
    if value % 2 != 0:
        for check_factor in range(1, (int(math.sqrt(value)) + 1)):
            if value % check_factor == 0:
                factor_list.append(check_factor)
            if len(factor_list) > 2:
                break


i = 1
while prime_list[-1] < 2000000:
    factor_list = []
    find_factors(i)
    if len(factor_list) == 2:
        prime_list.append(i)
    i += 2

prime_list.pop(-1)
print(prime_list)

add_all_prime = 0
for item in prime_list:
    add_all_prime += item

print(add_all_prime)    #   142913828922
