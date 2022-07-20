
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
students = [list(map(int,input().split())) for _ in range(N**2)]
board = [[-1 for _ in range(N)] for _ in range(N)]

for s, f1, f2, f3, f4 in students:
    f = {f1,f2,f3,f4}
    m = 0
    flag = False
    visited = [[[-1,-1] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            b_cnt = 0
            if board[i][j] == -1:
                for a in range(4):
                    ax = i + dx[a]
                    ay = j + dy[a]
                    if board[ax][ay] == -1:
                        b_cnt +=1
                    if board[ax][ay] in f:
                        cnt += 1
                visited[i][j] = [cnt,b_cnt]
                m = max(m,cnt)
    for i in range(N):
        for j in range(N):
            