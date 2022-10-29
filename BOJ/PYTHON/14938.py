from heapq import heappush,heappop
import sys
input = sys.stdin.readline


N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
item = list(map(int,input().split()))
answer = 0

for _ in range(R):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

for i in range(1,N+1):
    heap = []
    heappush(heap,[0,i])
    distance = [float("inf") for _ in range(N + 1)]
    distance[i] = 0
    tmp = 0
    while heap:
        cost, curr =heappop(heap)
        for next, c in graph[curr]:
            totalCost = cost + c
            if distance[next] > totalCost:
                distance[next] = totalCost
                heappush(heap, [totalCost, next])
    for idx,i in enumerate(distance):
        if i != float("inf") and i <= M:
            tmp += item[idx-1]

    answer = max(answer,tmp)
print(answer)