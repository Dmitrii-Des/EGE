def f(num):
    res = ''
    while num:
        res += str(num % 5)
        num //= 5
    return res[::-1]

for N in range(1, 100_000):
    R = f(N)
    if len(R) % 2 == 0:
        R = R[len(R) // 2:] + R[:len(R) // 2]
    else:
        R += str(N % 5)
        R = R[len(R) // 2:] + R[:len(R) // 2]
    R = int(R, 5)
    if R > 50:
        print(N)
        break