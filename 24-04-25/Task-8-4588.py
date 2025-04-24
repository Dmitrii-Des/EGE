from itertools import product

alph = '01234567'
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        for i in '1357':
            if f'{i}6' in val or f'6{i}' in val:
                break
        else:
            cnt += 1

print(cnt)