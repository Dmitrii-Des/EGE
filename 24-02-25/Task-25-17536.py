def f(num):
    divs = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divs.append(i)
            divs.append(num // i)
    divs = set(divs)

    if len(divs) <= 1:
        return 0
    return min(divs) + max(divs)

cnt = 0

for i in range(800_001, 10**20):
    M = f(i)
    if str(M)[-1] == '4':
        print(i, M)
        cnt += 1
        if cnt == 5:
            break

