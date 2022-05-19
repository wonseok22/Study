import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    s = {start}
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                s.add(i)
                q.append(i)
    return s

for i in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    for _ in range(int(input())):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    sets = []
    for j in range(1,N+1):
        if not visited[i]:
            visited[j] = True
            sets.append(bfs(j))
    print("Scenario {}:".format(i+1))
    for _ in range(int(input())):
        u,v = map(int,input().split())
        for s in sets:
            if u in s:
                if v in s:
                    print(1)
                else:
                    print(0)
                break
    print()
