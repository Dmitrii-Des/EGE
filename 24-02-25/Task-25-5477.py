def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

cnt = 0

for i in range(600_001, 10**20):
    if  i % 6 == 0 and is_prime(i - 1) and is_prime(i + 1):
        print(i-1, i+1)
        cnt += 1
        if cnt == 6:
            break