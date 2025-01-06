def convert(num):
    res = ''
    while num:
        res += str(num % 4)
        num //= 4
    return res[::-1]

for N in range(1, 100_000)[::-1]:
    R = convert(N)
    ost = convert((N % 4) * 5)
    if N % 4 == 0:
        R = '2' + R + '03'
    else:
        R = R + ost
    R = int(R, 4)
    if R < 567:
        print(N)
        break

