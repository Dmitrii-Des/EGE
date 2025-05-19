with open('24_4643.txt') as file:
    data = file.readline()

data = data.replace('A', 'B').replace('1','2')
data = data.replace('22B', 'W')
data = data.replace('2', ' ').replace('B', ' ').split()

print(len(max(data, key=len)))