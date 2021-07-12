import sys
input = sys.stdin.readline
currSize = 2
eatCnt = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(start):
    queue = []
    queue.append(start)
    ans = 0
    c = [[-1 for _ in range(N)] for _ in range(N)]
    c[start[0]][start[1]] = 0
    board[start[0]][start[1]] = 0
    global eatCnt,currSize
    while queue:
        queue.sort(key = lambda x :(x[2],x[0],x[1]))
        x,y,z = queue[0]
        del queue[0]
        if 0 < board[x][y] < currSize :
            eatCnt += 1
            c = [[-1 for _ in range(N)] for _ in range(N)]
            c[x][y] = 0
            board[x][y] = 0
            if eatCnt == currSize:
                eatCnt = 0
                if currSize > 6:
                    currSize = 7
                else:
                    currSize += 1
            queue = [[x, y, 0]]
            ans += z
            continue
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=ax<N and 0<=ay<N:
                if c[ax][ay] == -1 and board[ax][ay] <= currSize:
                    queue.append([ax,ay,z+1])
                    c[ax][ay] = 0

    print(ans)



if __name__ == "__main__":
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                bfs([i,j,0])
