#   divisible 1-20
def no_remainder(value):
    for i in range(4, 20 + 1):
        if value % i != 0:
            return False
    return True


#   find the smallest number, op 2520 as it was test through 1-10
#   += 20 for the evenly divisible range of 20

value = 2520
while True:
    if no_remainder(value) is True:
        break
    value += 20

print(value)
