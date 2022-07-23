def fib(x):  # x = limit
    a = 0  # starting point
    b = 1
    addition = 0 # sum of a and b
    even_list = []
    while b < x:
        if addition % 2 == 0:
            even_list.append(addition)
            print(sum(even_list))

        addition = a + b
        b = a
        a = addition

fib(4000000)
