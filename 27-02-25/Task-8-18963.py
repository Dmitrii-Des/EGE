from itertools import product

alph = sorted('КОТБУС')
cnt = 0

for val in product(alph, repeat=8):
    val = ''.join(val)
    if 'КОТ' in val and 'О' not in val[0] and 'У' not in val[0]:
        cnt += 1

print(cnt)