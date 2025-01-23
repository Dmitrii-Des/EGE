def convert(num):
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N)
    kratno = sum(list(map(int, R)))
    if kratno % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    R = int(R, 3)
    if R < 100:
        ans.append(N)
print(max(ans))