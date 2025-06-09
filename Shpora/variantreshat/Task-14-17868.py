from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:19]

for x in alph[::-1]:
    num1 = int(f'98897{x}21', 19)
    num2 = int(f'2{x}923', 19)
    summ = num1 + num2
    if summ % 18 == 0:
        print(summ // 18)
        break