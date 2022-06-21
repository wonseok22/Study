import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]
d = [0,1,2,1]
dd = [0,1,3,2,0]
answer = float("inf")
def dfs(x,y,dir, cnt):
    global answer
    if x == tx-1 and y == ty-1 :
        answer = min(answer, cnt+d[abs(dir-dd[td])])
        return
    if cnt < answer:
        for i in range(4):
            rot = abs(dir - i) % 4
            ax,ay = x,y
            for _ in range(3):
                ax += dx[i]
                ay += dy[i]
                if 0 <= ax < N and 0 <= ay < M and board[ax][ay] == 0:
                    board[ax][ay] = 1
                    dfs(ax,ay,i,cnt + 1 + d[rot])
                    board[ax][ay] = 0
                else:
                    break


N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
fx,fy,fd = map(int,input().split())
tx,ty,td = map(int,input().split())
board[fx-1][fy-1] = 1
dfs(fx-1,fy-1,dd[fd],0)
print(answer)



import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append([fx-1,fy-1,dd[fd],0])
    visited = [[[-1 for _ in range(4)] for _ in range(M)] for _ in range(N)]
    visited[fx-1][fy-1][dd[fd]] = 0
    while queue:
        x,y,dir,cnt = queue.popleft()
        if x == tx-1 and y == ty-1 and dir == dd[td]:
            return cnt
        ax,ay = x,y
        for _ in range(3):
            ax += dx[dir]
            ay += dy[dir]
            if 0 <= ax < N and 0 <= ay < M and board[ax][ay] == 0:
                    if visited[ax][ay][dir] == -1:
                        visited[ax][ay][dir] = 0
                        queue.append([ax,ay,dir,cnt+1])
            else:
                break
        for i in range(4):
            if visited[x][y][i] == -1 and dir != i:
                visited[x][y][i] = 0
                queue.append([x,y,i,cnt+d[abs(i-dir)]])

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
fx,fy,fd = map(int,input().split())
tx,ty,td = map(int,input().split())
print(bfs())
