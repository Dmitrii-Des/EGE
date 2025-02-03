from itertools import permutations

alph = sorted('МАКАКА')
cnt = 0

for val in permutations(alph, 6):
    if 'ММ' not in val and 'АА' not in val and 'КК' not in val:
        cnt += 1
print(cnt)