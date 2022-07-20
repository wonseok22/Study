import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
    distance = [float("inf") for _ in range(N + 1)]
    heap = [[start, 0]]
    distance[start] = 0
    while heap:
        x, dis = hq.heappop(heap)
        if dis > distance[x]:
            continue
        for i in graph[x]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                hq.heappush(heap, (i[0], cost))
    return distance

if __name__ =="__main__":
    N,E = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        a,b,c = map(int,input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
    v1, v2 = map(int,input().split())
    one = dijkstra(1)
    v1_cost = dijkstra(v1)
    v2_cost = dijkstra(v2)
    answer = min(one[v1] + v1_cost[v2] + v2_cost[N], one[v2] + v2_cost[v1] + v1_cost[N])
    print(answer if answer < float("inf") else -1)



