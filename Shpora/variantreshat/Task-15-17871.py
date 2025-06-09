from itertools import combinations

def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

ans = []
data = [i + eps for i in range(14, 64) for eps in [0, 0.1, 0.9]]

for A1, A2 in combinations(data, 2):
    if all(f(x) for x in data):
        ans.append(A2-A1)
print(min(ans))