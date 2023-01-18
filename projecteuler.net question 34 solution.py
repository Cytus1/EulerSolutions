import math

target_num_array = []


scan_num = 3

while scan_num < 100000:

    str_convertor = str(scan_num)

    total = 0
    for digit in range(len(str_convertor)):
        total += math.factorial(int(str_convertor[digit]))
        
    if total == scan_num:
        target_num_array.append(total)
        
    scan_num += 1

sum = 0
for num in target_num_array:
    sum += num

print(sum)  #40730
