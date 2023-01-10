N,K = map(int,input().split())
T = []
for _ in range(N):
    T.append(list(map(int,input().split())))
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        w,v = T[i-1]
        if j >= w: dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else: dp[i][j] = dp[i-1][j]
print(dp[i][j])


    
