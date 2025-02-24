def f(num):
    divs = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divs.append(i)
            divs.append(num // i)
    divs = sorted(set(divs))

    for i in divs:
        if str(i)[-1] == '8' and i != 8:      #i % 10 == 8
            return i
    return 0

cnt = 0
for i in range(500_001, 10**20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break

