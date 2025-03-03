from functools import lru_cache
from sys import setrecursionlimit


@lru_cache()
def F(n):
    if n < 11:
        return n
    if n >= 11:
        return n + F(n - 1)

for i in range(10, 2025):
    F(i)
#Если без @lru_cache, то setrecursionlimit()
print(F(2024) - (F(2021)))