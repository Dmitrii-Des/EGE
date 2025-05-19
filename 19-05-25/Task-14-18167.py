for x in range(1, 10_001)[::-1]:
    num = 6**900+6**10-x
    cnt1 = 0
    cnt2 = 0
    while num:
        if num % 6 == 3:
            cnt1 += 1
        if num % 6 == 5:
            cnt2 += 1
        num //= 6
    if cnt1 == cnt2:
        print(x)
        break
