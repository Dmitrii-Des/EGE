from itertools import product, permutations

for N in range(1, 100_000):
    R = bin(N)[2:]
    summ = R.count('1')%2
    R = R + str(summ)
    summ1 = R.count('1')%2
    R = R + str(summ1)
    R = int(R, 2)
    if R > 75:
        print(R)
        break

