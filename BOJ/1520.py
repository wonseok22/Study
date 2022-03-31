from collections import deque
import heapq as hq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
queue = []
visited[0][0] = 1
hq.heappush(queue,[-board[0][0],0,0])
while queue:
    curr,x,y = hq.heappop(queue)
    curr = -curr
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < N and 0 <= ay < M:
            if board[x][y] > board[ax][ay]:
                if visited[ax][ay] == 0:
                    hq.heappush(queue, (-board[ax][ay], ax, ay))
                visited[ax][ay] += visited[x][y]
print(visited[N-1][M-1])