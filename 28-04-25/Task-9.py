def f1(nums):
    pov = [i for i in nums if nums.count(i) >= 3]
    return len(pov) >= 1

def f2(nums):
    nepov = [i for i in nums if nums.count(i) == 1]
    return len(nepov) >= 1

def f3(nums):
    pov = [i for i in nums if nums.count(i) >= 2]
    nepov = [i for i in nums if nums.count(i) == 1]
    return sum(pov)/len(pov) < sum(nepov)/len(nepov)

with open('9v2.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i) and f3(i):
        cnt += 1

print(cnt)