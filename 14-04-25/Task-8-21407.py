from itertools import product

alph = sorted('ДГИАШЭ')
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    for i in 'ИАЭ':
        val = val.replace(i, 'И')
    if val[0] != 'И':
        for i in 'ДГШ':
            val = val.replace(i, 'Д')
        if val[-1] != 'Д':
            cnt += 1
print(cnt)