from collections import deque
def bfs(start):
    visited = [-1] * (N + 1)
    visited[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        for i,cost in tree[curr]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[curr] + cost
    m = max(visited)
    return [visited.index(m),m]
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    start,end,weight = map(int,input().split())
    tree[start].append([end,weight])
    tree[end].append([start,weight])
print(bfs(bfs(1)[0])[1])