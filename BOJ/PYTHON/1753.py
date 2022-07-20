from heapq import heappop,heappush
import sys
def dijkstra(start):
    heap = []
    answer[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in weight[n]:
            n_w = wei + w
            if n_w < answer[n_n]:
                answer[n_n] = n_w
                heappush(heap, [n_w, n_n])

if __name__ == "__main__":
    V,E = map(int,sys.stdin.readline().split())
    start = int(sys.stdin.readline())
    weight = [[] for _ in range(V+1)]
    answer = [10000000]*(V+1)
    for _ in range(E):
        a,b,c = map(int,sys.stdin.readline().split())
        weight[a].append([b,c])
    dijkstra(start)
    for ans in answer[1:]:
        if ans == 10000000:
            print("INF")
        else:
            print(ans)
