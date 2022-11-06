import math

a = []
b = []
c = 0
a_b_c = 0
a_b_c_list = []


for i in range(1, 500 + 1):
    a.append(i)
    b.append(i)
while a_b_c != 1000:
    for a_item in a:
        for b_item in b:
            c = math.sqrt(a_item**2 + b_item**2)
            if a_item + b_item + c == 1000:
                a_b_c = a_item + b_item + c
                if not a_b_c_list:
                    a_b_c_list.append(a_item)
                    a_b_c_list.append(b_item)
                    a_b_c_list.append(c)

print(a_b_c)
print(a_b_c_list)
print(a_b_c_list[0] * a_b_c_list[1] * a_b_c_list[2])    #31875000
