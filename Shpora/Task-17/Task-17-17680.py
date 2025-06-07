with open('17_17680.txt') as file:
    data = [int(i) for i in file]

ans = []
min_kr41 = min([i for i in data if i % 41 == 0 and i > 0])

for i in range(len(data) - 1):
    a1, a2 = data[i:i+2]
    f1 = a1 != a2
    f2 = abs(a2 - a1) % min_kr41 == 0
    if f1 and f2:
        ans.append(a1 + a2)

print(len(ans), max(ans))