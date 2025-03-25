from itertools import permutations

graph = 'BE EG GH HC CD DF FB AB AD AG AC'.split()
matrix = '36 478 178 258 46 158 23 2346'.split()

print(*range(1, 9))

for i in permutations('BEGHCDFA'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)