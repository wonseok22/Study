import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    global answer
    can_pool = True
    height_wall = 10
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    pool = list()
    while q:
        x,y = q.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if ax < 0 or ay < 0 or ax >= N or ay >= M or land[ax][ay] == 0:
                can_pool = False
                continue
            if visited[ax][ay]:
                continue
            if land[ax][ay] > land[x][y]:
                height_wall = min(height_wall, land[ax][ay])
            elif land[ax][ay] == land[x][y]:
                visited[ax][ay] = True
                pool.append([ax,ay])
                q.append([ax.ay])
            else


N,M = map(int,input().split())
land = [list(input().strip()) for _ in range(N)]
arr = [[] for _ in range(10)]
visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        land[i][j] = int(land[i][j])
        arr[land[i][j]].append([i,j])

for start in arr:
    for x,y in start:
        if not visited[x][y]:
            bfs(start)