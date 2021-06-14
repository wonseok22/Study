import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
# [층수][세로][가로]

if __name__ =="__main__":
    N,M,H = map(int,input().split())
    t = [[list(map(int,input().split())) for _ in range(M)] for _ in range(H)]
    queue = deque([])
    c = [[[0 for _ in range(N)] for _ in range(M)] for _ in range(H)]
    flag = True
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if t[i][j][k] == 1:
                    c[i][j][k] = 1
                    queue.append([i,j,k])
    ans = 1
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            az = z + dz[i]
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=az<H and 0<=ax<M and 0<=ay<N:
                if t[az][ax][ay] == 0 and c[az][ax][ay] == 0:
                    queue.append([az,ax,ay])
                    c[az][ax][ay] = c[z][x][y] + 1
                    t[az][ax][ay] = 1
                    ans = max(ans,c[z][x][y] + 1)
    for i in range(H):
        for j in range(M):
            if 0 in t[i][j]:
                print(-1)
                exit()
    print(ans-1)