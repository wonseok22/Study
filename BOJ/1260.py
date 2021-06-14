import sys
from collections import deque
input = sys.stdin.readline


def bfs(node,start):
    queue = deque([start])
    print(start,end = ' ')

    check = [0 for _ in range(N+1)]
    check[start] = 1
    while queue:
        x = queue.popleft()
        for i in node[x]:
            if check[i] == 0:
                print(i,end = ' ')
                queue.append(i)
                check[i] = 1


def dfs(node,start):
    visited[start] = 1
    print(start,end = ' ')
    for i in node[start]:
        if visited[i] == 0:
            dfs(node,i)

if __name__ == "__main__":
    N,M,V = map(int,input().split())
    nodes = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int,input().split())
        nodes[x].append(y)
        nodes[y].append(x)
    for i in range(N+1):
        nodes[i] = sorted(nodes[i])
    dfs(nodes,V)
    print('\n',end = '')
    bfs(nodes,V)
