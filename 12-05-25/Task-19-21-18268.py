from math import ceil
def f(x, y, s):
    if x + y <= 72: return s % 2 == 0
    if s == 0:  return False
    h = [f(x-3, y, s-1), f(x, y-3, s-1), f(ceil(x/2), y, s - 1), f(x, ceil(y/2), s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19', max([i for i in range(23, 200) if f(50, i, 2)]))
print('20', [i for i in range(23, 200) if f(50, i, 3) and not f(50, i , 1)])
print('21', [i for i in range(23, 300) if f(50, i, 4) and not f(50, i, 2)])