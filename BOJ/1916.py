import sys
import heapq as hq
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    bus = [[] for _ in range(N+1)]
    for _ in range(M):
        start,end,cost = map(int,input().split())
        bus[start].append([end,cost])
    start,end = map(int,input().split())
    heap = [[0,start]]
    distance = [100000001 for _ in range(N+1)]
    distance[start] = 0
    while heap:
        dis,now = hq.heappop(heap)
        if distance[now] < dis:
            continue
        for i in bus[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(heap, (cost, i[0]))
    print(distance[end])





