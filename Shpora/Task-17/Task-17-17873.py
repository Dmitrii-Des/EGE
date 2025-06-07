with open('17_17873.txt') as file:
    data = [int(i) for i in file]

ans = []
min_el = min([i for i in data])

for i in range(len(data) - 1):
    a1, a2 = data[i:i+2]
    u1 = a1 % 16 == min_el
    u2 = a2 % 16 == min_el
    f1 = u1 + u2 >= 1
    if f1:
        ans.append(a1 + a2)

print(len(ans), max(ans))