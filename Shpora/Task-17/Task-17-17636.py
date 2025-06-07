with open('17_17636.txt') as file:
    data = [int(i) for i in file]

ans = []
max_3 = max([i for i in data if str(i)[-1] == '3' and len(str(abs(i))) == 3])

for i in range(len(data) - 2):
    a1, a2, a3 = data[i], data[i + 1], data[i + 2]
    summ = a1 + a2 + a3
    u1 = str(a1)[-1] == '3' and len(str(abs(a1))) == 3
    u2 = str(a2)[-1] == '3' and len(str(abs(a2))) == 3
    u3 = str(a3)[-1] == '3' and len(str(abs(a3))) == 3
    f1 = u1 + u2 + u3 >= 1
    f2 = summ < max_3
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))