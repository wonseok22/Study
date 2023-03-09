import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline


N,K = map(int,input().split())
j = deque(sorted([list(map(int,input().split())) for _ in range(N)]))
k = sorted([int(input()) for _ in range(K)])
i = 0
answer = 0

tmp = []
for bag in k:
    while j and j[0][0] <= bag:
        a,b = j.popleft()
        hq.heappush(tmp,-b)
    if tmp:
        answer -= hq.heappop(tmp)
print(answer)
