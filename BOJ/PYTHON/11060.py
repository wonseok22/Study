N = int(input())
maps = list(map(int,input().split()))
dp = [float('inf') for _ in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(1,maps[i]+1):
        if i+j < N:
            dp[i+j] = min(dp[i+j],dp[i]+1)
if dp[N-1] == float("inf"):
    print(-1)
else:
    print(dp[N-1])