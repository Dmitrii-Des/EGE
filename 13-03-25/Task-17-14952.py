with open('17_14952.txt') as file:
    data = [int(i) for i in file]

ans = []
max_121 = max(i for i in data if str(i)[-3:] == '121')

for i in range(len(data)-2):
    a1, a2, a3 = data[i], data[i+1], data[i+2]
    summ = a1 + a2 + a3
    u1 = 1000 <= abs(a1) <= 9999 and abs(a1) % 2 == 0
    u2 = 1000 <= abs(a2) <= 9999 and abs(a2) % 2 == 0
    u3 = 1000 <= abs(a3) <= 9999 and abs(a3) % 2 == 0
    f1 = u1 + u2 + u3 <= 1
    f2 = summ <= max_121
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))