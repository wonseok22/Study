import sys
from collections import deque
input = sys.stdin.readline


# 실패 이유 : 말 이동으로 넘어간 횟수를 3차원배열에 저장해야함,


dx = [-1,1,0,0]
dy = [0,0,-1,1]

cx = [-1,-1,1,1,-1,1,-1,1]
cy = [-1,1,-1,1,-1,-1,1,1]

def bfs(start,k):
    queue = deque([start])
    c = [[0]*w for _ in range(h)]
    cnt = 0
    c[start[0]][start[1]] = 1
    while queue:
        x,y = queue.popleft()
        if x == h-1 and y == w-1:
            return c[x][y]-1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < h and 0 <= ay < w:
                if c[ax][ay] == 0 and maps[ax][ay] != 1:
                    queue.append([ax,ay])
                    c[ax][ay] = c[x][y] + 1
        if cnt < k:
            for i in range(4):
                if i == 0:
                    for j in range(2):
                        ax = x + dx[i] + cx[j]
                        ay = y + dy[i] + cy[j]
                        if 0 <= ax < h and 0 <= ay < w:
                            if c[ax][ay] == 0 and maps[ax][ay] != 1:
                                queue.append([ax, ay])
                                c[ax][ay] = c[x][y] + 1
                elif i == 1:
                    for j in range(2,4):
                        ax = x + dx[i] + cx[j]
                        ay = y + dy[i] + cy[j]
                        if 0 <= ax < h and 0 <= ay < w:
                            if c[ax][ay] == 0 and maps[ax][ay] != 1:
                                queue.append([ax, ay])
                                c[ax][ay] = c[x][y] + 1
                elif i == 2:
                    for j in range(4,6):
                        ax = x + dx[i] + cx[j]
                        ay = y + dy[i] + cy[j]
                        if 0 <= ax < h and 0 <= ay < w:
                            if c[ax][ay] == 0 and maps[ax][ay] != 1:
                                queue.append([ax, ay])
                                c[ax][ay] = c[x][y] + 1
                else:
                    for j in range(6,8):
                        ax = x + dx[i] + cx[j]
                        ay = y + dy[i] + cy[j]
                        if 0 <= ax < h and 0 <= ay < w:
                            if c[ax][ay] == 0 and maps[ax][ay] != 1:
                                queue.append([ax, ay])
                                c[ax][ay] = c[x][y] + 1
            cnt += 1
    return(-1)
if __name__ == "__main__":
    k = int(input())
    w,h = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(h)]
    print(bfs([0,0],k))
