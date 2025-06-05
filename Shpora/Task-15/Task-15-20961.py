from itertools import combinations

def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = A1 <= x <= A2
    return not(Q <= (((not A) and P) <= (not Q)))

ans = []
data = [x + eps for x in range(14, 168) for eps in [0, 0.1, 0.9]]

for A1, A2 in combinations(data, 2):
    if all(not f(x) for x in data):
        ans.append(A2-A1)

print(min(ans))