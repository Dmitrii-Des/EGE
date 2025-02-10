with open('17_9786.txt') as file:
    data = [int(i) for i in file]

max_25 = max([i for i in data if abs(i) % 100 == 25])
ans = []

for i in range(len(data) - 2):
    a1, a2, a3 = data[i], data[i + 1], data[i + 2]
    summ = a1 + a2 + a3

    u1 = len(str(abs(a1))) == 4
    u2 = 1000 <= abs(a2) <= 9999
    u3 = 1000 <= abs(a3) <= 9999
    f1 = u1 + u2 + u3 <= 2
    f2 = summ <= max_25
    if f1 and f2:
        ans.append(a1 + a2 + a3)
print(len(ans), max(ans))