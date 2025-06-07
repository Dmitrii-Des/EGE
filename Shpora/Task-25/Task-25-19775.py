from math import isqrt

def is_prime(num):
    if num < 2: return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    res = set()
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            if is_prime(i): res |= {i}
            if is_prime(num // i):  res |= {num // i}
    res = sorted(res)
    if len(res) < 1:
        return 0
    return sum(res)

cnt = 0
for n in range(32_500_001, 10**15):
    res = f(n)
    if res != 0 and res % 145 == 0:
        print(n, res)
        cnt += 1
        if cnt == 7:    break