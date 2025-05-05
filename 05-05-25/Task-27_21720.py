from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, dot])
    return min(dists)[1]

with open('27_A_21720.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps = 2
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)
print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
p_x = abs(sum(center[0] for center in centers) / len(centers))
p_y = abs(sum(center[1] for center in centers) / len(centers))
print(int(p_x * 10_000), int(p_y * 10_000))
