def f(num):
    divs = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs |= {i, num // i}
    divs = sorted(divs)
    if len(divs) < 2:
        return 0
    return max(divs) - min(divs)

cnt = 0

for i in range(300_000, 10**10):
    M = f(i)
    if str(M)[-1] == '6':
        print(i, M)
        cnt += 1
        if cnt == 5:
            break