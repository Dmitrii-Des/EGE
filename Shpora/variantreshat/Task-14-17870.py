for x in range(1, 2031)[::-1]:
    num = 7**170+7**100-x
    cnt = 0
    while num:
        if num % 7 == 0:
            cnt +=1
        num //= 7
    if cnt == 71:
        print(x)
        break

