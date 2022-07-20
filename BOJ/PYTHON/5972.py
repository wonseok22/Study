import sys
import heapq as hq
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A].append([B,C])
    graph[B].append([A,C])

def dijkstra(start,end):
    heap = [[0,start]]
    distance = [float("inf") for _ in range(N+1)]
    distance[start] = 0
    while heap:
        cost, curr = hq.heappop(heap)
        if distance[curr] < cost:
            continue
        for n, c in graph[curr]:
            if c + cost < distance[n]:
                distance[n] = c + cost
                hq.heappush(heap,[c+cost,n])
    return distance[end]

print(dijkstra(1,N))