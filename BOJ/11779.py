import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
start,end = map(int,input().split())
heap = []
heappush(heap,[0,start])
distance = [float("inf") for _ in range(N+1)]
distance[start] = 0
path = [None for _ in range(N+1)]
def trace(start, end):
    res = [end]
    path[start] = 0
    while path[end]:
        res.append(path[end])
        end = path[end]
    return res[::-1]

while heap:
    cost,curr = heappop(heap)
    if distance[curr] < cost:
        continue
    for next,c in graph[curr]:
        totalCost = cost + c
        if distance[next] > totalCost:
            heappush(heap,[cost+c,next])
            distance[next] = totalCost
            path[next] = curr
print(distance[end])
answer = trace(start,end)
print(len(answer))
print(" ".join(map(str,answer)))

