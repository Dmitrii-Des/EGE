def f(cur, end):
    if cur == end:
        return 1
    if cur > end or cur == 8:
        return 0
    return f(cur + 1, end) + f(cur * 2, end) + f(cur * 5, end)

print(f(2, 27)*f(27, 54))