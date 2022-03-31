dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(int(input())):
    R, C, tmp = input().split()
    R = int(R)
    C = int(C)
    board = []
    for i in range(R):
        board.append(list(tmp[i*R:i*R+C]))
    D = 1
    x = 0
    y = 0
    ans = ""
    visited = [[0]*C for _ in range(R)]
    visited[0][0] = 1
    for _ in range(R*C):
        ax = x + dx[D]
        ay = y + dy[D]
        if 0 <= ax < R and 0 <= ay < C:
            if visited[ax][ay] == 0:
                ans += board[x][y]
                x = ax
                y = ay


