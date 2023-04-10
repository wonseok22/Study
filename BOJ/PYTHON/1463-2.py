
N = int(input())
dp = [0 for _ in range(N+1)]
dp[N] = 0


for i in range(N-1, 0,-1):
    dp[i] = min(dp[i+1],
                dp[i*3] if i*3 <= N else float("inf"),
                dp[i*2] if i*2 <= N else float("inf")
                ) + 1
print(dp[1])