import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(int(input()))
        exit()
    cost = [[int(input())]]
    for _ in range(N-1):
        cost.append(list(map(int,input().split())))
    dp = [[] for _ in range(N+1)]
    dp[1] = [cost[0][0]+cost[1][0],cost[0][0]+cost[1][1]]
    for i in range(2,N):
        for j in range(i+1):
            if j==0:
                dp[i].append(dp[i-1][j]+cost[i][j])
            elif j==i:
                dp[i].append(dp[i-1][-1]+cost[i][j])
            else:
                dp[i].append(max(dp[i-1][j-1]+cost[i][j],dp[i-1][j]+cost[i][j]))
    print(max(dp[N-1]))

