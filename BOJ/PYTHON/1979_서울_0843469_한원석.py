
import copy
T = int(input())


for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    row_board = [list(map(int,input().split())) for _ in range(N)]
    col_board = copy.deepcopy(row_board)
    answer = 0

    for i in range(N):
        for j in range(N):
            if row_board[i][j] == 1:
                x,y = i,j
                cnt = 1
                row_board[i][j] = 0
                while True:
                    y += 1
                    if 0 <= y < N and row_board[x][y] == 1:
                        cnt += 1
                        row_board[x][y] = 0
                    else:
                        break

                if cnt == K:
                    answer += 1
    for i in range(N):
        for j in range(N):
            if col_board[i][j] == 1:
                x,y = i,j
                cnt = 1
                col_board[i][j] = 0
                while True:
                    x +=  1
                    if 0 <= x < N and col_board[x][y] == 1:
                        cnt += 1
                        col_board[x][y] = 0
                    else:
                        break
                if cnt == K:
                    answer += 1
    print("#{}".format(test_case), answer)