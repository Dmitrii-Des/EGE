def dell(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 10_000):
        f = dell(A, x) <= ((x == A) or (x == 1))
        if not f:
            return False
    return True

cnt = 0

for A in range(1, 11112):
    if f(A):
        cnt += 1
print(cnt)
