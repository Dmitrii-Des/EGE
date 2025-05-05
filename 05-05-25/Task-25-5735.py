from math import isqrt

def f(num):
    cnt_2 = 0
    res = set()
    if num in pows2:
        cnt_2 += 1
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            if i in pows2:
                cnt_2 += 1
            else:
                res.add(i)
            if num // i in pows2:
                cnt_2 += 1
            else:
                res.add(num // i)
    if cnt_2 >= 20:
        return sum(res)
    return ('none')

pows2 = [2 ** i for i in range(1, 50)]
cnt = 0
for n in range(10 ** 6 + 1, 10 ** 9):
    res = f(n)
    if res != 'none':
        print(n, res)
        cnt += 1
        if cnt == 5:
            break