from fnmatch import fnmatch

for i in range(1021574 - 1021574 % 133, 10**10, 133):
    if fnmatch(str(i), '1[02468]21574') or\
            fnmatch(str(i), '1[02468]2157[13579]4') or\
            fnmatch(str(i), '1[02468]2157[13579][13579]4') or\
            fnmatch(str(i), '1[02468]2157[13579][13579][13579]4'):
        print(i, i//133)