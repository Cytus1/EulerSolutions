sum=0
for number in range(3,1000):
    if number % 3 == 0:
        sum += number
    elif number % 5 == 0:
        sum += number
print(sum) #233168
