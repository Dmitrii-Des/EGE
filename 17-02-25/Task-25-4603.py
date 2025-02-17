from itertools import product

for r in range(4):
    for i in product('0123456789', repeat = r):
        i = ''.join(i)
        num = int('1234' + i + '7')
        if num <= 10**8 and num % 141 == 0:
            print(num, num//141)

