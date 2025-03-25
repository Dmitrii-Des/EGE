from itertools import product

alph = sorted(set('ЛУНАТИК'))
ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] == 'Н' and val.count('У') + val.count('И') + val.count('А') == 1:
        ans.append(pos)
print(max(ans))