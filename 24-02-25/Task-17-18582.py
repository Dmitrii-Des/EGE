with open('17_18582.txt') as file:
    data = [int(i) for i in file]

min_last = str(min(i for i in data))[-1]

ans = []

for i in range(len(data)-2):
    a1, a2, a3 = data[i], data[i+1], data[i+2]
    summ = a1 + a2 + a3

    u1 = str(a1)[0] == '-'
    u2 = str(a2)[0] == '-'
    u3 = str(a3)[0] == '-'
    f1 = u1 + u2 + u3 >= 2
    f2 = str(summ)[-1] == min_last
    if f1 and f2:
        ans.append(abs(summ))

print(len(ans), max(ans))