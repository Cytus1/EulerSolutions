def find_multiples_in_range(multiple, range = 999):
    n = (((range//multiple) * multiple) + multiple) / 2
    return n * (range//multiple)
print(find_multiples_in_range(3) + find_multiples_in_range(5) - find_multiples_in_range(15)) #233168
