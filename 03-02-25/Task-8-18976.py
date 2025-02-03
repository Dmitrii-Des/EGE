from itertools import product
from string import digits, ascii_uppercase

alph = (digits+ascii_uppercase)[:20]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and (int(val[0], 20) + int(val[-1], 20)) == 26:
        for i in alph[1::2]:
            val = val.replace(i, 'X')
        for k in alph[::2]:
            val = val.replace(k, 'Y')
        if 'XX' not in val and 'YY' not in val:
            cnt += 1
print(cnt)
