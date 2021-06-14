import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(x, y):
    visit = [[0]*M for _ in range(N)]
    q = deque()
    visit[x][y] = 1
    q.append([x, y, 0])

    while q:
        x, y, cost = q.popleft()
        if space[x][y]:
            return cost
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append([nx, ny, cost + 1])

if __name__ == '__main__':
    N,M = map(int,input().split())
    space = [list(map(int,input().split())) for _ in range(N)]
    ans  = 0
    for i in range(N):
        for j in range(M):
            if space[i][j] != 1:
                ans = max(ans,bfs(i,j))
    print(ans)

