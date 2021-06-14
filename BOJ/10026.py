from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(c,start):
    queue = deque([start])
    check[start[0]][start[1]] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < n and 0 <= ay < n:
                if c:
                    if maps[x][y] == "B":
                        if check[ax][ay] == 0:
                            if maps[ax][ay] == maps[x][y]:
                                queue.append([ax,ay])
                                check[ax][ay] = 1
                    else:
                        if check[ax][ay] == 0:
                            if maps[ax][ay] == "R" or maps[ax][ay] == 'G':
                                queue.append([ax,ay])
                                check[ax][ay] = 1
                else:
                    if check[ax][ay] == 0:
                        if maps[ax][ay] == maps[x][y]:
                            queue.append([ax,ay])
                            check[ax][ay] = 1


if __name__ == "__main__":
    n = int(input())
    maps = [list(input().strip('\n')) for _ in range(n)]
    check = [[0]*n for _ in range(n)]
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                bfs(False, [i,j])
                cnt1 += 1
    check = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                bfs(True,[i,j])
                cnt2 +=1
    print(cnt1,cnt2)