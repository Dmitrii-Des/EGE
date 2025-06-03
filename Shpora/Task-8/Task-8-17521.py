from itertools import product
from string import digits

alph = digits[:8]
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') <= 2 and val[0] not in '1357' and val[-1] not in '26':
        cnt += 1

print(cnt)