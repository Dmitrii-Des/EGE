ans = []
for x in range(1, 5556):
    num = 5**150+5**135-x
    cnt = 0
    while num:
        if num % 5 == 4:
            cnt += 1
        num //= 5
    if cnt == 134:
        ans.append(x)
print(max(ans))


