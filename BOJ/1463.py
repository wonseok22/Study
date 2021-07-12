import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dp = [0 for _ in range(N+1)]
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    for i in range(3,N+1):
        dp[i] = dp[i-1]+1
        if i % 3 == 0:
            dp[i] = min(dp[i//3] + 1,dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i//2] + 1,dp[i])

    print(dp[N])
