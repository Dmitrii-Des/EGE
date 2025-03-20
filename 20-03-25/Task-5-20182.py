def f(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    return res[::-1]


for N in range(1, 1_000_000):
    R = f(N)
    schet = sum(map(int, R))
    if schet % 2 == 0:
        R = '12' + R[2:] + '0'
    else:
        R = '10' + R[2:] + '2'
    R = int(R, 3)
    if R > 105:
        print(N)
        break