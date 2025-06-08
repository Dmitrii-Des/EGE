from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, dot])
    return min(dists)[1]

with open('27A_18677.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)
print(int(p_x * 100_000), int(p_y * 100_000))

with open('27B_18677.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 0.5
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers)/ len(centers)
p_y = sum(center[1] for center in centers)/ len(centers)
print(int(p_x * 100_000), int(p_y * 100_000))