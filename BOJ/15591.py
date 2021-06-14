import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    c = [0 for _ in range(N+1)]
    queue.append(start)
    c[start] = 1
    while queue:
        node = queue.popleft()
        for idx in U[node]:

            if c[idx[0]] == 0:
                weight[idx[0]] = min(weight[idx[0]],idx[1])
                c[idx[0]] = 1
                if weight[node] > 0:
                    weight[idx[0]] = min(weight[node],weight[idx[0]])
                if weight[idx[0]] >= K:
                    queue.append(idx[0])

if __name__ == "__main__":
    N,Q = map(int,input().split())
    U = [[] for _ in range(N+1)]
    for _ in range(N-1):
        x,y,z = map(int,input().split())
        U[x].append([y,z])
        U[y].append([x,z])
    quest = [list(map(int,input().split())) for _ in range(Q)]
    for K,v in quest:
        cnt = 0
        weight = [1000000001 for _ in range(N+1)]
        weight[0] = -1
        weight[v] = -1
        bfs(v)
        for i in weight:
            if i>=K and i != 1000000001:
                cnt +=1
        print(cnt)
