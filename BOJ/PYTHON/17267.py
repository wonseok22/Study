import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


# 0: 갈 수 있는 땅
# 1: 벽이 있어 갈 수 없는 땅
# 2: 영조와 보성이가 있는 위치
# 5 5
# 1 1
# 00000
# 00000
# 02100
# 10000
# 00000

# 13

N, M = map(int,input().split())
L, R = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[[10e9,10e9] for _ in range(M)] for _ in range(N)]
queue = deque()
answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '2':
            queue.append([i,j,0,0])
            visited[i][j] = [0,0]
while queue:
    x,y,l,r = queue.popleft()
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        al,ar = l,r
        if ax < 0 or ay < 0 or ax >= N or ay >= M or board[ax][ay] == "1": continue
        if visited[ax][ay][0] <= l and visited[ax][ay][1] <= r:
            continue
        if i == 2 and l < L : # 좌
            al += 1
        elif i == 3 and r < R:
            ar += 1
        elif i < 2:
            pass
        else:
            continue
        visited[ax][ay][0] = al
        visited[ax][ay][1] = ar
        queue.append([ax,ay,al,ar])
for i in range(N):
    for j in range(M):
        if visited[i][j] != [10e9,10e9]:
            answer += 1
print(answer)