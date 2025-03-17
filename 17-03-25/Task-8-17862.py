from string import digits, ascii_uppercase
from itertools import product

alph = (digits + ascii_uppercase)[:12]

cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count('7') == 1 and val[0] != '0':
        for i in '9AB':
            val = val.replace(i, '9')
        if val.count('9') <= 3:
            cnt += 1

print(cnt)
