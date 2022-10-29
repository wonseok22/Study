from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    A, B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
queue = deque()
queue.append(1)
visited[1] = 1
while queue:
    node = queue.popleft()
    for i in graph[node]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = node
for i in visited[2:]:
    print(i)

