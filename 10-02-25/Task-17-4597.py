with open('17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)
ans = []

for i in range(len(data) - 1):
    a1, a2 = data[i], data[i + 1]

    u1 = a1 % 117 == minn
    u2 = a2 % 117 == minn

    if u1 + u2 >= 1:
        ans.append(a1 + a2)

print(len(ans), max(ans))