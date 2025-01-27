def f(B):
    for x in range(0, 1_000):
        u = ((x & 500 != 0) and (x & 200 == 0)) <= (not(x & B == 0))
        if not u:
            return False
    return True

for B in range(0, 10_000):
    if f(B):
        print(B)
        break