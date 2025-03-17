from string import digits, ascii_uppercase

def f(num):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % 12]
        num //= 12
    return res[::-1]

ans = []

for N in range(1, 100_000):
    R = f(N)
    if N % 3 == 0:
        R = '1' + R + 'B'
    if N % 3 != 0:
        R = '2' + R + '0'
    R = int(R, 12)
    if R < 1996:
        ans.append(R)

print(max(ans))



