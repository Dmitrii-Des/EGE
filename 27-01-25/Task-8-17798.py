from itertools import product
from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:25]
for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0] != 0:
        if map(int(val, 25))