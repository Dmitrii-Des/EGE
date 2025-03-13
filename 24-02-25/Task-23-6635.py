def f(cur, cnt):
    if cnt == 13:
        global ans
        ans.append(cur)
        return
    f(cur - 3, cnt + 1)
    f(cur * (-3), cnt + 1)

ans = []
f(333, 0)

cnt = 0
for i in set(ans):
    if i < 0:
        cnt += 1

print(cnt)