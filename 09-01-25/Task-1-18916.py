from itertools import permutations

graph = 'ВА АБ БД ДЖ ЖЗ ЗЕ ЕГ ГВ ВБ ГД ЕЖ'.split()
matrix = '356 358 128 67 127 147 456 23'.split()

print(*range(1, 9))

for i in permutations('АБДЖЗЕГВ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        46138, 47528
ans = []
ans.append(2+2+1+5)
ans.append(8+4+2+4)
print(min(ans))