def f(x, y, s):
    if x + y >= 81: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, y, s - 1), f(x, y + 1, s - 1), f(x * 2, y, s - 1), f(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)   #Для 19 задачи all(h) изменить на any(h)

print('19', [i for i in range(1, 74) if f(7, i, 2)])
print('20', [i for i in range(1, 74) if f(7, i, 3) and not f(7, i, 1)])
print('21', min([i for i in range(1, 74) if f(7, i, 4) and not f(7, i, 2)]))
