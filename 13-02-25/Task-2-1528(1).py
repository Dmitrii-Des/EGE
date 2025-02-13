print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                u = (not w) and ((y or z) <= (y and (not x)))
                if u:
                    print(x, y, z, w)