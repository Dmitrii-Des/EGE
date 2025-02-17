with open('17_19486.txt') as file:
    data = [int(x) for x in file]

summ_7 = len([i for i in data if str(i)[-1] == '7'])
ans = []

for i in range(len(data) - 1):
    a1, a2 = data[i], data[i+1]
    summ = a1 + a2
    u1 = (len(str(a1)) == len(str(abs(a1)))) and ((len(str(a2))) != len(str(abs(a2))))
    u2 = (len(str(a2)) == len(str(abs(a2)))) and ((len(str(a1))) != len(str(abs(a1))))
    f1 = u1 + u2 == 1
    f2 = summ < summ_7
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))
