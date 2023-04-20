def generate_fib_sequence (limit):
    sum, a, b = 0, 1, 0
    while a < limit:
        if a % 2 == 0: sum += a
        a, b = (a + b), (a)
    return sum
print(generate_fib_sequence(4000000)) #4613732
