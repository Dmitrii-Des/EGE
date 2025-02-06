from itertools import permutations

graph = 'FC CH HB BE EA AF GC GD DH AB'.split()
matrix = '248 157 456 136 23 34 28 17'.split()

print(*(range(1, 9)))

for i in permutations('FCGDHBEA'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(21+2)