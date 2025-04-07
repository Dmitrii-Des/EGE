from itertools import combinations


def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums):
    return nums[0] + nums[1] == nums[2] + nums[3] or\
        nums[0] + nums[2] == nums[1] + nums[3] or\
        nums[0] + nums[3] == nums[2] + nums[1]

def f3(nums):
    return min(nums) + max(nums) == sum(nums) - min(nums) - max(nums)

def f4(nums):
    for i in combinations(nums, 2):
        if sum(i) == sum(nums) - sum(i):
            return True
    return False
with open('9_4589.txt') as file:
    data = [list(map(int, (i.split()))) for i in file]

cnt = 0

for i in data:
    if f1(i) and f2(i) and f3(i) and f4(i): #Все возможные функции для второго пункта задачи
        cnt += 1

print(cnt)