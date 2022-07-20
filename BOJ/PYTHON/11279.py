import heapq
import sys
input = sys.stdin.readline

if __name__ =="__main__":
    heap = []
    for _ in range(int(input())):
        N = int(input())
        if N == 0:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)
        else:
            heapq.heappush(heap, (-N,N))
