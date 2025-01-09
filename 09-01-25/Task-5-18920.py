ans = []
for N in range(1, 26):
    R = bin(N)[2:]
    if N % 2 != 0:
        R = '10' + R + '1'
    else:
        R = '10' + R + '0111'
    R = int(R, 2)
    ans.append(R)
print(max(ans))