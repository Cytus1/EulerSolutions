def generate_prime(nth_prime):
    scan_num = 1 ; prime_count = 1 ; prime = 0
    while prime_count < nth_prime:
        scan_num += 2 ; scan_range = int(scan_num**0.5) + 1
        count = 0
        for factor in range(1, scan_range):
            if (scan_num % factor == 0): count += 1
            if count > 1: break
        if count == 1: prime_count += 1 ; prime = scan_num
    return(prime)

print(generate_prime(10001)) # 104743
