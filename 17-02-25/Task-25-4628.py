from itertools import product

ans = []

for v in '0123456789':
    for r in range(3):
        for z in product('0123456789', repeat = r):
            z = ''.join(z)
            num = int('12' + z + '4' + v + '65')
            if num % 161 == 0:
                ans.append([num, num // 161])

ans = sorted(ans)
for i in ans:
    print(*i)