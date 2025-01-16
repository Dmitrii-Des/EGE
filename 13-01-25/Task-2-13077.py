from itertools import permutations, product

def f(x, y, z, w):
    return((w == x) and (y <= z))

def y(x, y, z, w):
    return((w <= x) <= (y == z))

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(1, a1, 1, 1), (a2, 1, 0, 0), (a3, 0, 0, a4)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            for x in 0, 1:
                u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 0]
                r = [y(**dict(zip(p, t))) for t in table] == [0, x, 0]
                if u and r:
                        print(*p)