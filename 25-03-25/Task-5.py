def f(num):
    res = ''
    while num:
        res += str(num % 4)
        num //= 4
    return res[::-1]

ans = []
for N in range(1, 100_00):
    R = f(N)
    summ = sum(map(int, R))
    if summ % 2 == 0:
        R = R + R[-2:]
    else:
        R = '2' + R + '0'
    R = int(R, 4)
    if R > 120 and R % 2 == 0:
        ans.append(R)

print(min(ans))