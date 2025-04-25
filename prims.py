import heapq
import random

def prims(graph):
    MCST = [[None for _ in range(len(graph))] for _ in range(len(graph))]
    priorityQueue = []
    cost = 0
    
    src = random.randrange(len(graph))
    print("Source: ",src)
    
    heapq.heappush(priorityQueue,(0,src,src))
    
    spanningTree = set()
    heapq.heappush(priorityQueue,(0,src,src))
    
    while priorityQueue:
        edge,prevnode,currentnode = heapq.heappop(priorityQueue)
        
        if currentnode in spanningTree:
            continue
        
        spanningTree.add(currentnode)
        
        if prevnode != currentnode:
            MCST[prevnode][currentnode] = edge
            MCST[currentnode][prevnode] = edge
            cost += edge
            
        for neighbour in range(len(graph)):
            if neighbour not in spanningTree and graph[currentnode][neighbour] is not None:
                heapq.heappush(priorityQueue,(graph[currentnode][neighbour],currentnode,neighbour))
                
    return MCST,cost
    
MCST, cost = prims(
    [
        [None, 4, 3, None, None, None],
        [4, None, 1, 2, None, None],
        [3, 1, None, 4, None, None],
        [None, 2, 4, None, 2, None],
        [None, None, None, 2, None, 6],
        [None, None, None, None, 6, None],
    ]
)

print("\nMCST:")
for i in MCST:
    print(i)

print("\nCost:", cost)
    
