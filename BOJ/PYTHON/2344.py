import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dir = [1,0,3,2]


def out(x,y): # 빛이 나가는 좌표에 따른 번호
    if x == -1:
        return 2*N + 2*M -y
    elif y == -1:
        return x+1
    elif x == N:
        return N + y + 1
    else:
        return 2*N + M - x


def search(start,direction):
    x,y = start
    while 0 <= x < N and 0 <= y < M:
        if board[x][y] == 1:  #거울이 있다면 빛의 진행경로 변경
            direction = dir[direction]
        x += dx[direction]
        y += dy[direction]
    return str(out(x,y))

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = []

# 1번부터 2N + 2M번까지 입력 순서대로 실행
for i in range(N):
    direction = 1
    answer.append(search([i,0],direction))
for i in range(M):
    direction = 0
    answer.append(search([N-1, i], direction))
for i in range(N-1,-1,-1):
    direction = 3
    answer.append(search([i, M-1], direction))
for i in range(M-1,-1,-1):
    direction = 2
    answer.append(search([0, i], direction))
print(' '.join(answer))
