with open('Task_17.txt') as file:
    data = [int(i) for i in file]

ans = []
minkv_19 = min(i for i in data if len(str(abs(i))) == 3 and str(i)[-2:] == '19')**2

for i in range(len(data)-2):
    a1, a2, a3 = data[i], data[i+1], data[i+2]
    summ = a1 + a2 + a3
    u1 = str(a1)[-2:] == '19' and len(str(abs(a1))) == 5
    u2 = str(a2)[-2:] == '19' and len(str(abs(a2))) == 5
    u3 = str(a3)[-2:] == '19' and len(str(abs(a3))) == 5
    f1 = u1 + u2 + u3 >= 1
    f2 = summ > minkv_19
    if f1 and f2:
        ans.append(summ)

print(len(ans), min(ans))