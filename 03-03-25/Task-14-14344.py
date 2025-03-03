ans = []
for p in range(16, 37):
    num1 = int('17496', p)
    num2 = int('91F83', p)
    num3 = int('D9543', p)
    summ = num1 + num2 + num3
    if summ % 12 == 0:
        ans.append((p, summ//12))

print(min(ans))

