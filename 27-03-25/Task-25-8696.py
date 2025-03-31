def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def f(num):
    divs = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            divs |= {i, num//i}
    return sum(divs)

cnt = 0

for i in range(1_273_548, 10**10):
    M = f(i)
    if is_prime(M % 100_000):
        print(i, M)
        cnt += 1
        if cnt == 5:
            break
