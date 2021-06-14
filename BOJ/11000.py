import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    lectures = sorted([list(map(int,input().split())) for _ in range(N)],key = lambda x : x[0])
    queue = []
    heapq.heappush(queue,lectures[0][1])
    for i in range(1,N):
        start,end = lectures[i]
        if queue[0] <= start:
            heapq.heappop(queue)
            heapq.heappush(queue,end)
        else:
            heapq.heappush(queue,end)
    print(len(queue))
