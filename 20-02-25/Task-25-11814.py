from itertools import product

ans = []
for r in product('0123456789', repeat=3):
    r = ''.join(r)
    for v in '0123456789':
        num = int('21' + r + '68' + v + '79')
        if num % 1777 == 0 and num <= 10**10:
            ans.append((num, num // 1777))

ans = sorted(ans)
for i in ans:
    print(*i)