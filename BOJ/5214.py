import sys
from collections import deque
input = sys.stdin.readline

N, K,M = map(int,input().split())
graph = [set() for _ in range(N+1)]
for _ in range(M):
    g = list(map(int,input().split()))
    for i in range(K):
        for j in range(i+1,K):
            graph[g[i]].add(g[j])
            graph[g[j]].add(g[i])

queue = deque()
queue.append(1)
visited = [0 for _ in range(N+1)]
visited[1] = 1
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = visited[x] + 1
            queue.append(i)
print(visited[N])

