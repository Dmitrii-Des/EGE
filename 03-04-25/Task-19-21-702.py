def f(x, s):
    if 36 <= x <= 85:   return s % 2 == 0
    if x > 85:  return (s - 1) % 2 == 0
    if s == 0:  return False
    h = [f(x + 2, s - 1), f(x * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


for i in range(1, 10):
    if f(30, i):
        if i % 2:
            print(30, 'Петя')
        else:
            print(30, 'Ваня')
    if f(32, i):
        if i % 2:
            print(32, 'Петя')
        else:
            print(32, 'Ваня')
