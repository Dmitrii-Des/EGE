from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, dot])   #dists = distance
    return min(dists)[1]

with open('27_A_17882.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    for i in file:
        x, y = map(float, i.split())
        if y < 3: cluster_A1.append([x, y])
        else: cluster_A2.append([x, y])

clusters = [cluster_A1, cluster_A2]
centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(int(p_x * 10_000), int(p_y * 10_000))

with open('27_B_17882 (1).txt') as file:
    cluster_B1 = []
    cluster_B2 = []
    cluster_B3 = []
    for i in file:
        x, y = map(float, i.split())
        if x > 5: cluster_B1.append([x, y])
        elif x < 3 and y < 4: cluster_B2.append([x, y])
        else: cluster_B3.append([x, y])

clusters = [cluster_B1, cluster_B2, cluster_B3]
centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(int(p_x * 10_000), int(p_y * 10_000))