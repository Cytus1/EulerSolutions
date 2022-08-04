#   find product of palindrome


#   set the two product's range to 3 digit
product_range = []
first_list = []
second_list = []


def product():
    a = 800
    b = 1000
    c = 0
    while a < 999:
        a += 1
        first_list.append(a)
    while c <= 500:
        b -= 1
        c += 1
        second_list.append(b)


product()

#   times the product in list
list_of_products = []

for number_in_first_list in first_list:
    for number_in_second_list in second_list:
        list_of_products.append(number_in_first_list * number_in_second_list)
list_of_products.sort()

#   detect if it is a palindrome
palindrome_list = []


def is_palindrome():
    for item in list_of_products:
        a = str(item)[::-1]
        reverse = int(a)
        if item == reverse:
            palindrome_list.append(item)


is_palindrome()

print(palindrome_list)  # 906609

#   find the largest palindrome of those products
