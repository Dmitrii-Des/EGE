ans = []
for v in '0123456789':
    for v1 in '0123456789':
        for n in '13579':
            for ch in '02468':
                for ch1 in '02468':
                    num = int(ch + '9' + v + '23' + v1 + '23' + n + ch1)
                    if num % 1984 == 0 and num <= 10**10:
                        ans.append((num, num // 1984))

ans = sorted(ans)
for i in ans:
    print(*i)