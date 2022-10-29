import sys
from heapq import heappop,heappush
input = sys.stdin.readline


N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [float('inf') for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append([b,1])
heap = []
heappush(heap,[0,X])
distance[X] = 0
while heap:
    cost,curr = heappop(heap)
    for next, c in graph[curr]:
        totalCost = cost+c
        if distance[next] > totalCost:
            distance[next] = totalCost
            heappush(heap,[totalCost,next])
if K not in distance:
    print(-1)
    exit()
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
