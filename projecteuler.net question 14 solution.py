def equation_one (n):
    n = n/2     #   n is even

    return n

def equation_two (n):
    n = 3*n + 1  #   n is odd

    return n

def is_odd (n):
    if n != 1:
        if n % 2 == 0:
            return False
        else:
            return True


i = 1
i_locked = i

largest_count = 0
largest_number = 0

while i_locked < 1000000:
    
    count = 0
    
    i_locked += 2
    i = i_locked

    while i != 1:
        if is_odd(i) == True:
            count += 1
            i = equation_two(i)
        if is_odd(i) == False:
            count +=1
            i = equation_one(i)
        
    if count > largest_count:
        largest_count = count
        largest_number = i_locked

print(f'The highest count is {largest_count}, number: [{largest_number}]')  #837799
