from math import dist
def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, dot])
    return min(dists)[1]

with open('27_A_21599.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    cluster_A3 = []
    for i in file:
        x, y = map(float, i.split())
        if y < -7:
            cluster_A1.append([x, y])
        elif y > x - 10:
            cluster_A2.append([x, y])
        else:
            cluster_A3.append([x, y])

clusters = [cluster_A1, cluster_A2, cluster_A3]

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers)/ len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(abs(int(p_x * 10_000)), abs(int(p_y * 10_000)))
