import sys
import heapq as hq
from collections import deque

input = sys.stdin.readline
N = int(input())
station = deque(sorted([list(map(int,input().split())) for _ in range(N)],key = lambda x : (x[0],-x[1])))
L, P = map(int,input().split())
heap = []
answer = 0

if P >= L: # 시작부터 마을에 갈 수 있는 경우
    print(0)
    exit()

while True:
    while station: # 남은 주요소가 있는 경우
        if station[0][0] <= P: # 주요소를 갈 수 있는 경우
            hq.heappush(heap, -station.popleft()[1]) # 최대힙에 삽입
        else:
            break
    if heap: # 갈 수 있는 주유소가 있는 경우
        P += -hq.heappop(heap)
        answer += 1
        if P >= L: # 도착한 경우
            print(answer)
            exit()
    else: # 갈 수 있는 주유소가 없는 경우
        print(-1)
        exit()


