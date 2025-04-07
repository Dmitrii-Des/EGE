def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums):
    if len(set(nums)) == 3:
        return True
    return False
with open('9_4614.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0

for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)