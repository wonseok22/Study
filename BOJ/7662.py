import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        heap = []
        heap2 = []
        for _ in range(int(input())):
            W,n = input().split()
            n = int(n)
            if W == "I":
                heapq.heappush(heap,n)
                heapq.heappush(heap2,-n)
            else:
                if heap:
                    if n == 1:
                        heap.remove(-heapq.heappop(heap2))
                    else:
                        heapq.heappop(heap)
        if heap:
            print(max(heap),min(heap))
        else:
            print('EMPTY')