from math import isqrt

def f(num):
    res = set()
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    for i in res:
        if i % 10 == 7 and i != 7:
            return i
    return 0

cnt = 0
for n in range(700_001, 10**10):
    res = f(n)
    if res:
        print(n, res)
        cnt += 1
        if cnt == 5:    break
    # if res := f(n):
    #     print(n, res)
    #     cnt += 1
    #     if cnt == 5:  break