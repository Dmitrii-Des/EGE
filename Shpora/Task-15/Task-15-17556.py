def dell(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 10_000):
        B = 70 <= x <= 90
        f = dell(x, A) or (B <= (not(dell(x, 22))))
        if not f:
            return False
    return True

for A in range(1, 10_000)[::-1]:
    if f(A):
        print(A)
        break