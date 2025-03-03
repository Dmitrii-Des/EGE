from itertools import combinations

def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

ans = []
data = [x//10 for x in range(14*10, 64*10)]

for A1, A2 in combinations(data, 2):
    if all(f(x) for x in data):
        ans.append(A2-A1)

print(min(ans))