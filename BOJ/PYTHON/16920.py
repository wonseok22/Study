import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


N,M,P = map(int,input().split())
S = [0] + list(map(int,input().split()))
for i in range(1,P+1):
    S[i] = min(S[i], 2001)

board = [list(input().strip()) for _ in range(N)]
queue_list = [deque() for _ in range(P+1)]
for i in range(N):
    for j in range(M):
        if board[i][j] == "#" or board[i][j] == ".": continue
        board[i][j] = int(board[i][j])
        queue_list[board[i][j]].append([i,j])
while True:
    for player in range(1,P+1):
        for _ in range(S[player]):
            for _ in range(len(queue_list[player])):
                x,y = queue_list[player].popleft()
                for i in range(4):
                    ax = x + dx[i]
                    ay = y + dy[i]
                    if ax < 0 or ay < 0 or ax >= N or ay >= M or board[ax][ay] !=".": continue
                    queue_list[player].append([ax,ay])
                    board[ax][ay] = player
    flag = False
    for q in queue_list:
        if q:
            flag = True
    if not flag:
        break
answer = [0 for _ in range(P)]
for i in range(N):
    for j in range(M):
        if board[i][j] != "#" and board[i][j] != ".":
            answer[board[i][j]-1] += 1
print(*answer, sep=" ")






