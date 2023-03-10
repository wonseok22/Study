import sys
input = sys.stdin.readline

while True:
    M, N = map(int,input().split())
    if N == 0 and M == 0:
        break
    board = [list(map(int,input().split())) for _ in range(M)]
    dp = [[0 for _ in range(N)] for _ in range(M)]
    if N == 1 and M == 1:
        print(board[0][0])
        continue
    elif N == 1:
        dp[0][0] = board[0][0]
        dp[1][0] = max(board[0][0], board[1][0])
        for i in range(2,M):
            dp[i][0] = max(dp[i-1][0], board[i][0] + dp[i-2][0])
    elif M == 1:
        dp[0][0] = board[0][0]
        dp[0][1] = max(board[0][0], board[0][1])
        for i in range(2,N):
            dp[0][i] = max(dp[0][i - 1], dp[0][i - 2] + board[0][i])
    else:
        for i in range(M):
            dp[i][0] = board[i][0]
            dp[i][1] = max(board[i][0], board[i][1])
        for i in range(2):
            for j in range(2,N):
                dp[i][j] = max(dp[i][j-1], dp[i][j-2] + board[i][j])
        dp[1][-1] = max(dp[0][-1], dp[1][-1])
        for i in range(2, M):
            for j in range(2,N):
                dp[i][j] = max(dp[i][j - 1], dp[i][j - 2] + board[i][j])
            dp[i][-1] = max(dp[i-1][-1], dp[i][-1] + dp[i-2][-1])

    print(dp[-1][-1])
