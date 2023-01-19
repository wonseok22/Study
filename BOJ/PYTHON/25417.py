from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

b = [list(map(int,input().split())) for _ in range(5)]
q = deque()
q.append(list(map(int,input().split())))
v = [[-1 for _ in range(5)] for _ in range(5)]
v[q[0][0]][q[0][1]] = 0
while q:
    x,y = q.popleft()
    if b[x][y] == 1:
        print(v[x][y])
        exit()
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if ax < 0 or ay < 0 or ax >= 5 or ay >= 5 or b[ax][ay] == -1 or v[ax][ay] != -1: continue
        q.append([ax,ay])
        v[ax][ay] = v[x][y] +1
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        while True:
            if ax < 0 or ay < 0 or ax >= 5 or ay >= 5 or b[ax][ay] == -1:
                ax -= dx[i]
                ay -= dy[i]
                break
            if b[ax][ay] == 7:
                break
            ax += dx[i]
            ay += dy[i]
        if v[ax][ay] == -1:
            q.append([ax,ay])
            v[ax][ay] = v[x][y] + 1
print(-1)