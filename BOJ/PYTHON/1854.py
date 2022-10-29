import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

N,M,K = map(int,input().split())
weight = [[] for _ in range(N+1)]
distance = [[inf]*K for _ in range(N+1)]
heap = []

def dijkstra(start):
    heappush(heap,[0,start])
    distance[start][0] = 0
    while heap:
        cost,curr = heappop(heap)
        for i,c in weight[curr]:
            w = cost + c
            if w<distance[i][K-1]:
                distance[i][K - 1] = w
                distance[i].sort()
                heappush(heap,[w,i])
for i in range(M):
    a,b,c = map(int,input().split())
    weight[a].append([b,c])

dijkstra(1)

for i in range(1,N+1):
    if distance[i][K-1] == inf:
        print(-1)
    else:
        print(distance[i][K-1])