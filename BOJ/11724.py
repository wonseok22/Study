import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        D = queue.popleft()
        for i in D:
            if c[i] == -1:
                queue.append(graph[i])
                c[i] = 0

if __name__ == "__main__":

    N,M = list(map(int,input().split()))
    c = [-1 for _ in range(N + 1)]
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = list(map(int,input().split()))
        graph[b].append(a)
        graph[a].append(b)
    cnt = 0
    for i in range(1,N+1):
        if c[i] == -1:
            c[i] = 0
            bfs(graph[i])
            cnt += 1
    if N == 1:
        print(1)
    else:
        print(cnt)
