import sys
from heapq import heappop,heappush

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])


def dijkstra(start):
    distance = [float("inf") for _ in range(N+1)]
    distance[start] = 0
    heap = []
    heappush(heap,(0,start))
    while heap:
        cost,curr = heappop(heap)
        for next,next_cost in graph[curr]:
            totalCost = cost + next_cost
            if totalCost < distance[next]:
                heappush(heap,(totalCost,next))
                distance[next] = totalCost
    if start == X:
        return distance
    else:
        return distance[X]
ans = [0 for _ in range(N+1)]
for i in range(1,N+1):
    if i != X:
        ans[i] = dijkstra(i)
check = dijkstra(X)
m = 0
for i in range(1,N+1):
    m = max(m,ans[i] + check[i])
print(m)