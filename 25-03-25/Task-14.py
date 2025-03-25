cnt_max = 0
x_max = 0
for x in range(1, 2030)[::-1]:
    num = 2**2025+2**2024-2**2021-x
    cnt = 0
    while num:
        if num % 4 == 0:
            cnt += 1
        num //= 4
    if cnt > cnt_max:
        cnt_max = cnt
        x_max = x
print(x_max)