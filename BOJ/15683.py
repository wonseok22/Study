import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(dir,start):
    ax = start[0] + dx[dir]
    ay = start[1] + dy[dir]
    if 0<=ax<h and 0<=ay<w:
        if board[ax][ay] != :
            board[ax][ay] = '#'
            return dfs(dir,[ax,ay])+1
        else:
            return 0
    else:
        return 0

def reset(dir,cnt,start):
    ax,ay = start
    for _ in range(cnt):
        ax = ax + dx[dir]
        ay = ay + dy[dir]
        board[ax][ay] = 0

def search(start,case):
    check = [8]*4
    if case == 5:
        for j in range(4):
            check[j] = dfs(j,start)
    elif case == 4:
        for j in range(4):
            check[j] = dfs(j,start)
        m = min(check)
        reset(check.index(m),m,start)
    elif case == 3:
        for j in range(4):
            check[j] = dfs(j,start)

    elif case == 2:
        for j in range(4):
            check[j] = dfs(j,start)
    elif case == 1:
        for j in range(4):
            check[j] = dfs(j,start)
        m = max(check)
        a = True
        print(check)
        for idx,j in enumerate(check):
            if j != m or not a :
                reset(idx,j,start)
            else:
                a = False

if __name__ == "__main__":
    h,w = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(h)]
    cctv = [[] for _ in range(6)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 5:
                cctv[5].append([i,j])
            elif board[i][j] == 4:
                cctv[4].append([i,j])
            elif board[i][j] == 3:
                cctv[3].append([i,j])
            elif board[i][j] == 2:
                cctv[2].append([i,j])
            elif board[i][j] == 1:
                cctv[1].append([i,j])
    for i in range(5,0,-1):
        for start in cctv[i]:
            search(start,i)
    for z in range(h):
        print(board[z])

    '''for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                cnt += 1
    print(cnt)'''

