"""
Problem 30 Project Euler
"""

target_num_list = []

i = 2

while i < 1000000:

    convertor = str(i)
    total = 0

    for digit in range(len(convertor)):
        total += (int(convertor[digit]))**5

    if total == i:
        target_num_list.append(total)
    
    i += 1
    
print(target_num_list)

sum_of_list = 0
for num in target_num_list:
    sum_of_list += num

print(sum_of_list)  # 443839
