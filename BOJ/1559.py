from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dic = {
    "N" : 0,
    "E" : 1,
    "S" : 2,
    "W" : 3
}
N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]
K = int(input())
box = [list(map(int,input().split())) for _ in range(K)]
tmp = input()
for i in range(N):
    for j in range(M):
        board[i][j] = dic[board[i][j]]
queue = deque()
queue.append([0,0])
visited = [[[-1, -1, -1, -1] for _ in range(M)] for _ in range(N)]
visited[0][0][board[0][0]] = 0

while queue:


