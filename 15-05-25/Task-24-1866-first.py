# Если в условии задания просят, чтобы какие-то символы не стояли рядом,
# то разделяем их пробелом (при этом символы удалять нельзя)
with open('24_1866.txt') as file:
    data = file.readline()

while 'ad' in data:
    data = data.replace('ad', 'a d').replace('da', 'd a')
data = data.split()
print(len(max(data, key=len)))
