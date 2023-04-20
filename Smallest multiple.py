def smallest_multiple_1_to_20():
    factor_list = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    i = 0 ; flag = 1
    while flag != 0:
        flag = 0 ; i += 2
        for factor in factor_list:
            if i % factor == 0: pass
            else: flag = 1 ; break       
    return i

print(smallest_multiple_1_to_20())  #232792560
