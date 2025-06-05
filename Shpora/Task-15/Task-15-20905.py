from itertools import combinations

def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = A1 <= x <= A2
    return P <= ((Q and (not(A))) <= (not(P)))

ans = []
data = [x + eps for x in range(16, 82) for eps in [0, 0.1, 0.9]]

for A1, A2 in combinations(data, 2):
    if all(f(x) for x in data):
        ans.append(A2-A1)

print(min(ans))