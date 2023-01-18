sum = 0

for i in range(1, 1001):
    sum += i**i
    
convertor = str(sum)

print(convertor[-10:])  #9110846700
