with open('26_18967.txt') as file:
    N, K = map(int, file.readline().split())
    guests = [list(map(int, i.split())) for i in file]

guests = sorted(guests, key=lambda x: (x[1], x[0]))
lucky = []
angry = []
angry_cnt = 0
free_places = N

maxx_time = max(guests, key=lambda x: x[1])[1] + 1
timeline = [0] * maxx_time

for id, time, cnt in guests:
    if id not in angry and id not in lucky:
        if free_places >= cnt:
            free_places -= cnt
            lucky.append(id)
            for i in range(time, maxx_time):
                timeline[i] += cnt
        else:
            angry_cnt += cnt
            angry.append(id)
    elif id in lucky:
        free_places += cnt
        for i in range(time, maxx_time):
            timeline[i] -= cnt

print(angry_cnt, timeline.count(N))