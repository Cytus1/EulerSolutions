grid, scan_dia = [x for x in range(1, (1001 * 1001) + 1) if x % 2 != 0], [1]
spiral_gap_till_edge, four_counter, base_rate = 0, 0, 1

while scan_dia[-1] != grid[-1]:
    
    if four_counter == 4:
        four_counter = 0
        base_rate += 1
    
    spiral_gap_till_edge += base_rate
    
    scan_dia.append(grid[spiral_gap_till_edge])
    four_counter += 1

sum = 0
for dia_num in scan_dia:
    sum += dia_num
print(sum)  #   669171001
