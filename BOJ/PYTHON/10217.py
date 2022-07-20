import sys
from heapq import heappush,heappop
input = sys.stdin.readline


for _ in range(int(input())):
    N, M, K = map(int,input().split())
    start = 1
    end = N
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d = map(int,input().split())
        graph[u].append([v,c,d])
    distance = [[float("inf"),float("inf")] for _ in range(N+1)]
    heap = []
    heappush(heap,[0,0,start])
    distance[start][0] = 0
    distance[start][1] = 0
    while heap:
        print(heap)
        cost, price, curr = heappop(heap)
        for next, c, time in graph[curr]:
            totalTime = cost+time
            totalCost = price+c
            print(totalCost,totalTime,next)
            if totalTime < distance[next][0] and totalCost <= M and totalCost < distance[next][1]:
                heappush(heap, [totalTime,totalCost,next])
                distance[next][0] = totalTime
                distance[next][1] = totalCost
    if distance[N][0] == float("inf"):
        print("Poor KCM")
    else:
        print(distance[N][0])