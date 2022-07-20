import heapq as hq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [float("inf") for _ in range(N+1)]
start = 1
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
heap = [(0,start)]
while heap:
    cost, nxt = hq.heappop(heap)


