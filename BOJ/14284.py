import heapq as hq
import sys
input = sys.stdin.readline

def dijkstra(S,T):
    distance = [float('inf') for _ in range(N+1)]
    distance[S] = 0
    heap = [(0,S)]
    while heap:
        curr_cost, curr_node = hq.heappop(heap)
        if distance[curr_node] < curr_cost:
            continue
        for next_node, next_cost in graph[curr_node]:
            total_cost = next_cost + curr_cost
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                hq.heappush(heap,(total_cost, next_node))
    return distance[T]

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
S, T = map(int,input().split())
print(dijkstra(S, T))


