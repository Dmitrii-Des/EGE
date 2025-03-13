def f(cur, end, A):
    if cur == end: return 1
    if cur > end + 1: return 0
    if A != 1:
        return f(cur - 1, end, 1)+f(cur * 2, end, 0)+f(cur*3, end, 0)
    return f(cur*2, end, 0) + f(cur*3, end, 0)

print(f(3, 15, 0))
