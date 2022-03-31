import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N,M = map(int,input().split())
floor = [input() for _ in range(N)]
c = [[0]*M for _ in range(N)]
ans = 0
for a in range(N):
    for b in range(M):
        if c[a][b] == 0:
            ans += 1
            queue = deque()
            queue.append([a,b])
            c[a][b] = 1
            while queue:
                x,y = queue.popleft()
                if floor[x][y] == "-":
                    for i in range(2,4):
                        ax = x + dx[i]
                        ay = y + dy[i]
                        if 0<= ax < N and 0 <= ay < M:
                            if floor[a][b] == floor[ax][ay] and c[ax][ay]==0:
                                c[ax][ay] = 1
                                queue.append([ax,ay])
                else:
                    for i in range(2):
                        ax = x + dx[i]
                        ay = y + dy[i]
                        if 0<= ax < N and 0 <= ay < M:
                            if floor[a][b] == floor[ax][ay] and c[ax][ay]==0:
                                c[ax][ay] = 1
                                queue.append([ax,ay])
print(ans)