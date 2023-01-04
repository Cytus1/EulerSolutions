import math

string = str(math.factorial(100))
space_seperated_str_int = ""

for single_number in range(len(string)):
    space_seperated_str_int += string[single_number]
    space_seperated_str_int += " "

str_number_array = space_seperated_str_int.split(" ")
str_number_array.pop(-1)

int_number_array = []

for i in str_number_array:
    int_number_array.append(int(i))


sum = 0

for i in int_number_array:
    sum += i

print(sum)  #   648
