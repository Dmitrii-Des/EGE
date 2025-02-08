with open('26_8512.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
cells = [0] * K
last_cell = 0
cnt = 0
for start, end in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = end
            last_cell = i + 1
            cnt += 1
            break

print(cnt, last_cell)
