def convert(num):
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]
ans = []
for N in range(1, 100_000):
    R = convert(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        summ = convert(sum(map(int, R)))
        R += summ
    R = int(R, 3)
    if R > 220 and R % 2 == 0:
        ans.append(R)

print(min(ans))


