def f(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    return res[::-1]

ans = []

for N in range(1, 100_000):
    R = f(N)
    summ = sum(map(int, R))
    if summ % 2 == 0:
        R = '1' + R + '2'
    else:
        R = '2' + R + '0'
    R = int(R, 3)
    if R > 100:
        ans.append(R)
print(min(ans))