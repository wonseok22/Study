import sys

N = int(sys.stdin.readline())
houses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 집 갯수 3개 이하일 때 고려해주기!!!!!!!!!!!!!
if N <= 2:
    v = 2000
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            tmp = houses[0][i] + houses[1][j]
            if tmp < v:
                v = tmp
    print(v)
else:
    answer = 1e9
    dp = [1e9] * N
    color = -1
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if j == k:
                    continue
                v = houses[0][i] + houses[1][j] + houses[2][k]
                if v < dp[2]:
                    dp[2] = v
                    dp[1] = houses[0][i] + houses[1][j]
                    dp[0] = houses[0][i]
                    color = i
    idx = 0
    while idx < N - 3:
        idx += 1
        next_color = -1
        for i in range(3):
            if i == color:
                continue
            for j in range(3):
                if i == j:
                    continue
                for k in range(3):
                    if j == k:
                        continue
                    v = dp[idx - 1] + houses[idx][i] + houses[idx + 1][j] + houses[idx + 2][k]
                    if v < dp[idx + 2]:
                        dp[idx + 2] = v
                        next_color = i
        color = next_color

    print(dp[N - 1])