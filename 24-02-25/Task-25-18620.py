def f(num):
    divs = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs |= {i, num // i}
    divs = sorted(divs)
    if len(divs) < 2:
        return 0
    return divs[-2] + divs[-1]

for i in range(112_500_000, 112_550_001):
    if f(i) % 10_000 == 1214:
        print(i)
