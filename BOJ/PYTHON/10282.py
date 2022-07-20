import sys
from heapq import heappush,heappop
input = sys.stdin.readline


for _ in range(int(input())):
    N, D, C = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(D):
        a,b,c = map(int,input().split())
        graph[b].append([a,c])
    distance = [float("inf") for _ in range(N+1)]
    heap = []
    heappush(heap,[0,C])
    distance[C] = 0
    while heap:
        cost, curr = heappop(heap)
        for next, c in graph[curr]:
            totalCost = cost + c
            if distance[next] > totalCost:
                heappush(heap, [totalCost,next])
                distance[next] = totalCost
    ansCnt = 0
    ansMax = 0
    for i in distance[1:]:
        if i != float("inf"):
            ansCnt += 1
            ansMax = max(ansMax, i)
    print(ansCnt, ansMax)
