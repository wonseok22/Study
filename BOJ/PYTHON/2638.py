from collections import deque
import sys
input = sys.stdin.readline


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def check_air():
    air = [[False]*m for _ in range(n)]
    queue = deque([[0,0]])
    air[0][0] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < n and 0 <= ay < m:
                if maps[ax][ay] != 1 and not air[ax][ay]:
                    queue.append([ax,ay])
                    air[ax][ay] = True
    return air


def bfs(start,air):
    x,y = start
    cnt = 0
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < n and 0 <= ay < m:
            if air[ax][ay]:
                cnt +=1
    if cnt >= 2:
        maps[x][y] = 0


if __name__ == "__main__":
    n,m = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(n)]
    answer = 0
    while True:
        cnt = 0
        air = check_air()
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 1:
                    bfs([i,j],air)
        answer += 1
        for i in range(n):
            if 1 not in maps[i]:
                cnt += 1
        if cnt == n:
            break
    print(answer)