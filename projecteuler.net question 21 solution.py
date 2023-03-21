def find_factor(n):
    temp_factor_list = []
    for factor in range(1, int((n)/2) + 1):
        if (n % factor == 0):
            temp_factor_list.append(factor)
    return temp_factor_list

def sum_of_element(array):
    sum = 0
    for element in array:
        sum += element
    return sum

amicable_array, scanned_array = [], []

if __name__ == '__main__':
    
    for check_amicable_number in range(1, 10000):
        
        lower = check_amicable_number
        scanned_array = find_factor(lower)
        
        upper = sum_of_element(scanned_array)
        scanned_array = find_factor(upper)
        
        sum_of_proper_div_upper = sum_of_element(scanned_array)
        if (sum_of_proper_div_upper == lower) and (lower != upper) and (lower not in amicable_array):
            amicable_array.append(lower)
            
    print(sum_of_element(amicable_array))
