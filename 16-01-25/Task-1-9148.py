from itertools import permutations

graph = 'АГ ГЖ ЖЗ ЗД ДВ ВА АБ БВ ГБ ЖЕ ДЕ ЗЕ ГД'.split()
matrix = '256 1458 478 237 126 158 348 2367'.split()

print(*range(1, 9))

for i in permutations('АБГЖЗЕДВ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)