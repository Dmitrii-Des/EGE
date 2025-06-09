from itertools import permutations

graph = 'AB BD DF FE EC CA GD GF GC'.split()
matrix = '457 46 567 12 136 235 13'.split()

print(*range(1, 8))

for i in permutations('ABDFECG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(8 + 30)