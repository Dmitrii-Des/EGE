from itertools import permutations

alph = sorted('МАКАКА')
cnt = 0

for val in set(permutations(alph)):
    val = ''.join(val)
    if 'АА' not in val and 'КК' not in val:
        cnt += 1
print(cnt)