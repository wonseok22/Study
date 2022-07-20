import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    cost = []
    for _ in range(N):
        cost.append(list(map(int,input().split())))
    dp = [[] for _ in range(N+1)]
    dp[1] = cost[0]
    for i in range(2,N+1):
        for j in range(3):
            dp[i].append(cost[i-1][j]+min(dp[i-1][(j+1)%3],dp[i-1][(j+2)%3]))
    print(min(dp[N]))