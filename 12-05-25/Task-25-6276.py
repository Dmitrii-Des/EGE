from fnmatch import fnmatch

ans = []

for i in range(10101011 - 10101011 % 2023, 10**10, 2023):
    if fnmatch(str(i), '1?1?1?1*1'):
        if sum(map(int, str(i))) == 22:
            print(i)