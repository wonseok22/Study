import sys
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    queue = deque([start])
    cnt = [[-1]*m for _ in range(n)]
    ma = 0
    cnt[start[0]][start[1]] = 0
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0 <= ax < n and 0 <= ay < m:
                if cnt[ax][ay] == -1 and maze[ax][ay] == "L":
                    queue.append([ax,ay])
                    cnt[ax][ay] = cnt[x][y]+1
                    ma = max(ma, cnt[ax][ay])

    return ma

if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    maze = [list(input()) for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "L":
                answer = max(answer,bfs([i,j]))
    print(answer)
