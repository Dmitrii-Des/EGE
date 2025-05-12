def f(cur, end, A):
    if cur == end and A != 1:
        return 1
    if cur > end:
        return 0

    return f(cur + 2, end, False) + f(cur + 5, end, False) + f(cur**2, end, True)

print(f(4, 36, False))