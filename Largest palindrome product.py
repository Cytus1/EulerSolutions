def generate_palindromic(min_range, max_range):
    largest = 0
    for a in range(min_range, max_range, 2):
        for b in range(min_range, max_range, 2):
            if str(a*b) == str(a*b)[::-1] and a*b > largest: largest = a*b
    return largest
        
print(generate_palindromic(101, 1000)) # 906609
