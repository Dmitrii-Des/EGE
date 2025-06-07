from math import isqrt

def f(num):
    res = set()
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if len(res) < 2:    return  0
    return max(res) + min(res)

cnt = 0
for n in range(700_001, 10**10):
    res = f(n)
    if res % 10 == 4:
        print(n, res)
        cnt += 1
        if cnt == 5:    break