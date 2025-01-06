ans = []
for N in range(1, 100_000):
    R = oct(N)[2:]
    if N % 2 == 0:
        R += max(R)
    else:
        R += oct(int(min(R))*2)[2:]
    R = int(R, 8)
    if R < 313:
        ans.append(N)
print(max(ans))

