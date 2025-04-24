from itertools import product

alph = sorted('ИНСТАВК')
cnt = 0
for val in product(alph, repeat=4):
    val = ''.join(val)
    for i in 'НСТВК':
        if val[0] == i:
            for i in 'ИА':
                if val[-1] == i:
                    cnt += 1
                    if 'НИКА' in val:
                        print(cnt)