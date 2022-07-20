from heapq import heappush,heappop
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[b].append([a,c])
k_list = list(map(int,input().split()))
check = [float("inf") for _ in range(N+1)]

def dijkstra(start):
    heap = []
    heappush(heap,[0,start])
    distance = [float("inf") for _ in range(N + 1)]
    distance[start] = 0
    while heap:
        cost, curr = heappop(heap)
        if distance[curr] < cost:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        for next,c in graph[curr]:
            totalCost = cost + c
            if distance[next] > totalCost:
                distance[next] = totalCost
                heappush(heap,[totalCost,next])
                check[next] = totalCost


for i in k_list:
    d = dijkstra(i)
    print(check)
m = 0
idx = 0
check = check[1:]
for i in range(N):
    if m < check[i]:
        m = check[i]
        idx = i+1
print(idx)
print(m)
