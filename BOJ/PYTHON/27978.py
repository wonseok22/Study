import sys
from collections import deque
input = sys.stdin.readline

H,W = map(int,input().split())
board = [list(input().strip()) for _ in range(H)]
visited = [[float("inf") for _ in range(W)] for _ in range(H)]
# 오른쪽 3개먼저차고 왼쪽위부터
dx = [-1, 0, 1,-1, -1, 0 , 1, 1]
dy = [1, 1, 1, -1, 0, -1, -1, 0]
q = deque()
for i in range(H):
    for j in range(W):
        if board[i][j] == "K":
            q.append([i,j])
            visited[i][j] = 0
while q:
    x,y = q.popleft()
    if board[x][y] == "*":
        print(visited[x][y])
        exit()
    for i in range(8):
        ax = x + dx[i]
        ay = y + dy[i]
        if ax < 0 or ay < 0 or ax >= H or ay >= W or board[ax][ay] == "#" or visited[ax][ay] <= visited[x][y]: continue
        if i > 2:
            visited[ax][ay] = visited[x][y] + 1
        else:
            visited[ax][ay] = visited[x][y]
        q.append([ax,ay])
print(-1)
