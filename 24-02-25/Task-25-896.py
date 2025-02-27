def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

ser_num = 1

for i in range(194441, 196501):
    if i % 100 == 93 and is_prime(i):
        print(ser_num, i)
        ser_num += 1