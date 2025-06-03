def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(3) == 3 and cnt.count(1) == 3

def f2(nums):
    nepov = [i for i in nums if nums.count(i) == 1]
    pov = [i for i in nums if nums.count(i) != 1]
    return sum(map(int, pov))**2 > sum(map(int, nepov))**2

with open('09_17550.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)