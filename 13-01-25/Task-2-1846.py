print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((not a) and (not b)) or (b == c) or d
                if f: # если нужны истинные значения
                    print(a, b, c, d)

                if not f: # если нужны ложные значения
                    print(a, b, c, d)

print('Answer: cdba')