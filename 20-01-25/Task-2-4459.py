from itertools import permutations, product

def f(x, y, z, w):
    return((not x) <= y) and ((not y) == z) and w

for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    table = [(0, a1, 0, a2), (0, a3, a4, a5), (a6, 0, a7, a8)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)