from itertools import product
from string import digits, ascii_uppercase

alph = str(digits + ascii_uppercase)[:15]
cnt = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') == 2:
        for i in alph[10:15]:
            val = val.replace(i, 'А')
        if val.count('А') <= 3:
            cnt += 1
print(cnt)