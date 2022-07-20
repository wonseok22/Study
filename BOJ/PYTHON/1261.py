import sys
from heapq import heappop,heappush
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

M,N = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
heap = []
heappush(heap,[0,0,0])
visited[0][0] = 1
while heap:
    wall, x, y = heappop(heap)
    if x == N-1 and y == M-1:
       print(wall)
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < N and 0 <= ay < M:
            if board[ax][ay] == '0' and visited[ax][ay] == -1:
                heappush(heap,[wall,ax,ay])
                visited[ax][ay] = 1
            if board[ax][ay] == '1' and visited[ax][ay] == -1:
                heappush(heap,[wall+1,ax,ay])
                visited[ax][ay] = 1
