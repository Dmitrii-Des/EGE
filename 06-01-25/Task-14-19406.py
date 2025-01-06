from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
alph = alph [:35]

for x in alph:
    num1 = int(f'6{x}QR{x}', 35)
    num2 = int(f'{x}59SH', 35)
    num3 = int(f'PH{x}69YW', 35)
    summ = num1 + num2 + num3
    summs = str(summ)
    cnt = []
    for i in '0123456789':
        chet = summs.count(i)
        cnt.append([chet, i])
    cnt = max(cnt)
    if summ % int(cnt[1])**2 == 0:
        print(summ // int(cnt[1])**2)







