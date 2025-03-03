def f(num):
    res = ''
    while num:
        res += str(num % 7)
        num //= 7
    return res[::-1]

ans = []

for N in range(1, 100_000):
    R = f(N)
    if N % 2 == 0:
        R = '52' + R + '1'
    if N % 2 == 1:
        R = R[-1] + R[1:-1] + R[0] + '15'
    while R[0] == '0':
        R = R[1:]
    if N <= 1000 and len(R) == 4:
        ans.append(N)

print(max(ans))