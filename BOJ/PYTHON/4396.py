dx = [-1, -1, -1, 0, 0 ,1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


N = int(input())
board = [input() for _ in range(N)]
player = [input() for _ in range(N)]
answer = [['.' for _ in range(N)] for _ in range(N)]
flag = False
for i in range(N):
    for j in range(N):
        if player[i][j] == "x":
            if board[i][j] == "*":
                flag = True
            cnt = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0<= x < N and 0 <= y < N:
                    if board[x][y] == "*":
                        cnt += 1
            answer[i][j] = str(cnt)
if flag:
    for a in range(N):
        for b in range(N):
            if board[a][b] == "*":
                answer[a][b] = "*"
for i in range(N):
    print(''.join(answer[i]))
