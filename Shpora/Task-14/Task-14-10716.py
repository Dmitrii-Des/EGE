ans = []
for x in range(1, 150):
    num1 = 5 * 150**4 + 1 * 150**3 + x * 150**2 + 2 * 150**1 + 9 * 150**0
    num2 = x * 150**3 + 0 * 150**2 + 2 * 150**1 + 3 * 150**0
    summ = num1 + num2
    if summ % 149 == 0:
        ans.append(summ//149)

print(max(ans))