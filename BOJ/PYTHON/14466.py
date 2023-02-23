import sys
from collections import deque

input = sys.stdin.readline
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

N, K, R = map(int,input().split())
board = [[[0 for _ in range(5)] for _ in range(N)] for _ in range(N)]
answer = list()
ans = 0
for _ in range(R):
    r1,c1,r2,c2 = map(int,input().split())
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
    result = (r1*N + c1) - (r2 * N + c2)
    if result == -1:
        board[r1][c1][4] = 1
        board[r2][c2][3] = 1
    elif result == 1:
        board[r1][c1][3] = 1
        board[r2][c2][4] = 1
    elif result == N:
        board[r1][c1][1] = 1
        board[r2][c2][2] = 1
    else:
        board[r1][c1][2] = 1
        board[r2][c2][1] = 1
for _ in range(K) :
    r,c = map(int,input().split())
    board[r-1][c-1][0] = 1

visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count = 0
            q = deque()
            q.append([i,j])
            visited[i][j] = True
            while q:
                x,y = q.popleft()
                if board[x][y][0] == 1:
                    count += 1
                for d in range(1,5):
                    if board[x][y][d] == 1: continue
                    ax = x + dx[d]
                    ay = y + dy[d]
                    if ax < 0 or ay < 0 or ax >= N or ay >= N or visited[ax][ay]: continue
                    q.append([ax,ay])
                    visited[ax][ay] = True
            answer.append(count)
for idx, ivalue in enumerate(answer):
    for jdx, jvalue in enumerate(answer):
        if idx != jdx:
            ans += ivalue * jvalue
print(ans//2)