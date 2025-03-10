def f(num):
    res = ''
    while num:
        res += str(num%7)
        num //= 7
    return res[::-1]

for x in range(1, 100_000):
    num = 7**666+7**333+49**x-343
    num = f(num)
    if num.count('6') == 49:
        print(x)
        break