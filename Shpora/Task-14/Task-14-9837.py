from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:23]
ans = []

for x in alph:
    num1 = int(f'7{x}38596', 23)
    num2 = int(f'14{x}36', 23)
    num3 = int(f'61{x}7', 23)
    summ = num1 + num2 + num3
    if summ % 22 == 0:
        ans.append(summ//22)
print(min(ans))