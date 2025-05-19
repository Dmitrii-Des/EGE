from itertools import combinations


def f(x):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = A1 <= x <= A2
    return D <= (((not C) and (not A)) <= (not D))

ans = []
line = [x/10 for x in range(6*10, 102*10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2-A1)

print(min(ans))