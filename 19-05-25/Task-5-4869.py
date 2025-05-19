for N in range(2, 100_000):
    R = bin(N)[2:]
    chet = R[::2].count('0')
    nechet = R[1::2].count('1')
    R = abs(chet-nechet)
    if R == 5:
        print(N)
        break

