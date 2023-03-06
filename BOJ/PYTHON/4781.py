import sys
input = sys.stdin.readline

while True:
    N, M = map(float,input().split())
    N = int(N)
    M = int(M * 100+ 0.5)
    if N == 0 and M == 0:
        break
    candy = list()
    for _ in range(N):
        c,p = map(float,input().split())
        candy.append([int(c), int(p * 100 + 0.5)])
    dp = [0 for _ in range(M + 1)]
    for i in range(1, M+1):
        for c, p in candy:
            if i-p >= 0:
                dp[i] = max(dp[i-p] + c, dp[i])
    print(dp[i])

