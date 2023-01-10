import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M,K = map(int,input().split())
board = [input().strip() for _ in range(N)]
x1,y1,x2,y2 = map(int,input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
answer = [[float("inf") for _ in range(M)] for _ in range(N)]
answer[x1][y1] = 0
queue = deque()
queue.append([x1,y1])
while queue:
    x,y = queue.popleft()
    w = answer[x][y]
    if x == x2 and y == y2:
        print(w)
        exit()
    for i in range(4):
        move_cnt = 1
        while move_cnt <= K:
            ax = x + move_cnt*dx[i]
            ay = y + move_cnt*dy[i]
            move_cnt += 1
            if ax < 0 or ay < 0 or ax >= N or ay >= M or board[ax][ay] == "#" or (answer[ax][ay] != float("inf") and answer[ax][ay] <= w): break
            if answer[ax][ay] != float("inf"): continue
            answer[ax][ay] = w + 1
            queue.append([ax,ay])
print(-1)



