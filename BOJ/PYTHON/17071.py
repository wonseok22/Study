import sys
from collections import deque
input = sys.stdin.readline


N,K = map(int,input().split())
MAX_SEC = 0
MAX_LENGTH = 500000-K
i = 1
k_list = [0 for _ in range(1001)]
visited = [-1 for _ in range(500001)]
k_list[0] = K
while MAX_LENGTH > 0:
    k_list[i] = k_list[i-1] + i
    MAX_SEC += 1
    MAX_LENGTH -= i
    i += 1
q = deque()
q.append(N)
visited[N] = 0
while q:
    curr = q.popleft()
    if curr == k_list[visited[curr]]:
        print(visited[curr])
        exit()
    for i in [curr+1, curr-1, curr*2]:
        if i < 0 or i > 500000 or visited[i] != -1: continue
        q.append(i)
        visited[i] = visited[curr]+1
print(-1)






