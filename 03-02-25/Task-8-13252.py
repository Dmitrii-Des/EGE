from itertools import permutations
cnt = 0
alph = sorted(set('КИДАЛА'))

for val in permutations(alph, 5):
    val = ''.join(val)
    if 'АА' not in val and 'КК' not in val and 'ДД' not in val and 'ЛЛ' not in val:
        cnt += 1
print(cnt)