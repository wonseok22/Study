import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(maps,start):
    queue = deque()
    queue.append(start)
    c = [[0 for _ in range(M)] for _ in range(N)]
    c[start[0]][start[1]] = 1
    cnt = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=ax<N and 0<=ay<M:
                if c[ax][ay] == 0 and maps[ax][ay] != 'X':
                    queue.append([ax,ay])
                    c[ax][ay] = 1
                    if maps[ax][ay] == 'P':
                        cnt += 1
    if cnt == 0:
        return 'TT'
    else:
        return cnt


if __name__ == "__main__":
    N,M = map(int,input().split())
    maps = [list(input().strip()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'I':
                print(bfs(maps,[i,j]))