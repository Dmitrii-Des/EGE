def dell(x, d):
    return x % d == 0

def f(A):
    for x in range(1, 1_000):
        u = (dell(x, 10) and dell(x, 26) and (x >= 300)) <= (A <= x)
        if not u:
            return False
    return True

for A in range(1, 10_000)[::-1]:
    if f(A):
        print(A)
        break