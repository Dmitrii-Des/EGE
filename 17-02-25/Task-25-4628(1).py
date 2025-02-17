from fnmatch import fnmatch

for i in range(161, 10**8, 161):
    if fnmatch(str(i), '12*4?65'):
        print(i, i//161)