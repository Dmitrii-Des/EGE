from string import digits, ascii_uppercase
alph = (digits + ascii_uppercase)[:25]

ans = []

for x in alph:
    num1 = int(f'A4{x}7F2', 25)
    num2 = int(f'N{x}G5{x}H', 25)
    num3 = int(f'74{x}M26', 25)
    summ = num1 + num2 + num3
    if summ % 24 == 0:
        ans.append(summ//24)
print(max(ans))