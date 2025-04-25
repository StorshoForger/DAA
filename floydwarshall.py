def floydWarshall(dist,INF):
    V = len(dist)
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
                    
dist = [
    [0, 4, 100000000, 5, 100000000],
    [100000000, 0, 1, 100000000, 6],
    [2, 100000000, 0, 3, 100000000],
    [100000000, 100000000, 1, 0, 2],
    [1, 100000000, 100000000, 4, 0]
]

INF = 100000000
floydWarshall(dist, INF)

for i in range(len(dist)):
    for j in range(len(dist)):
        if dist[i][j] == INF:
            print('INF',end = '')
        else:
            print(dist[i][j],end='')
    print()
