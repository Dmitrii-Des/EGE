def f(cur, end, B):
    if cur == end: return 1
    if cur > end: return 0
    if B:
        return f(cur + 2, end, False) +  f(cur * 3, end, False)
    if B != 2:
        return f(cur + 2, end, False) + f(cur**2, end, True) + f(cur*3, end, False)

print(f(2, 64, False))