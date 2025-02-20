from itertools import product

ans = []
for r in range(4):
    for B in product('13579', repeat=r):
        B = ''.join(B)
        for A in '02468':
            num = int('1' + A + '2157' + B + '4')
            if num % 133 == 0 and num <= 10**10:
                ans.append((num, num//133))

ans = sorted(ans)
for i in ans:
    print(*i)