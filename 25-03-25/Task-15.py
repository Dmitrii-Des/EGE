def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            u = (x + 2 <= 50) or (y < x + 10) or (x >= A)
            if not u:
                return False
    return True
for A in range(1, 1000)[::-1]:
    if f(A):
        print(A)
        break

