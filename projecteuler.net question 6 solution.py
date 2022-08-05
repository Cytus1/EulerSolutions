#   define a range regard the sum of squares
sum_of_squares = 0
for i in range(1, 100+1):
    i = i ** 2
    sum_of_squares  += i
    i = 0
print(sum_of_squares)

#   define the square of a range of sums
range_of_sum_to_square = 0
for x in range(1, 100+1):
    range_of_sum_to_square += x

range_of_sum_to_square = range_of_sum_to_square ** 2
print(range_of_sum_to_square)

#   subtract goal 1 - goal 2 = differance
print(range_of_sum_to_square - sum_of_squares)
