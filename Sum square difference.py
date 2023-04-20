def sum_square_difference(lowest, highest):
    sum_of_square = sum([x**2 for x in range(lowest, highest)])
    square_of_sum = (sum([x for x in range(lowest, highest)]))**2
    return (square_of_sum) - (sum_of_square)

print(sum_square_difference(1, 101)) # 25164150
