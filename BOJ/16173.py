from collections import deque
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
queue.append([0,0])
while queue:
    x,y = queue.popleft()
    if board[x][y] == 0:
        continue
    if x == N-1 and y == N-1:
        print("HaruHaru")
        exit()
    if 0 <= x+board[x][y] < N and 0 <= y < N:
        queue.append([x+board[x][y],y])
    if 0 <= x < N and 0 <= y+board[x][y] < N:
        queue.append([x,y+board[x][y]])
print("Hing")