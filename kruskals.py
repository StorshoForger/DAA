from networkx.utils import UnionFind

def KruskalsAlgo(graph):
    MCST = [[None for _ in range(len(graph))] for _ in range(len(graph))]
    cost = 0
    edges = []
    
    # Initialize UnionFind
    uf = UnionFind()

    # Create edge list from adjacency matrix
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] is not None:
                edges.append((graph[i][j], i, j))

    # Sort edges by weight (ascending)
    edges.sort()

    while edges:
        edge, u, v = edges.pop(0)  # Take the lightest edge
        if uf[u] != uf[v]:  # If they are not connected (no cycle)
            uf.union(u, v)
            MCST[u][v] = edge
            MCST[v][u] = edge
            cost += edge

    return MCST, cost

# Test the Kruskal's algorithm with UnionFind on the given adjacency matrix
graph = [
    [None, 4, 3, None, None, None],
    [4 , None, 1 , 2 , None, None],
    [3 , 1 , None, 4 , None, None],
    [None, 2 , 4 , None, 2 , None],
    [None, None, None, 2 , None, 6 ],
    [None, None, None, None, 6 , None],
]

MCST, cost = KruskalsAlgo(graph)

# Print the Minimum Cost Spanning Tree (MCST) and the total cost
print("MCST:")
for row in MCST:
    print(row)

print("\nCost:", cost)
