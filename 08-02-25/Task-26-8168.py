with open('26_8168.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
cells = [0] * K
timeline = [""] * 1500
cnt = 0

for start, duration in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = start + duration
            cnt += 1
            for j in range(start + 1, start + duration):
                timeline[j] = timeline[j] + '+'
            break
print(N - cnt, timeline.count('+' * K))