import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    stair = [int(input()) for _ in range(N)]
    dp = [0 for _ in range(N)]
    if N < 3:
        print(sum(stair))
    else:
        dp[0] = stair[0]
        dp[1] = stair[1] + stair[0]
        dp[2] = max(stair[1] + stair[2] , stair[0] + stair[2])
        for i in range(3,N):
            dp[i] = max(dp[i-3] +stair[i] + stair[i-1] , dp[i-2] + stair[i])
        print(dp[N-1])