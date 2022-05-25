import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
M = int(input())
dp = [-float("inf") for _ in range(M+1)]
for i in range(N-1,-1,-1):
    p = P[i]
    for j in range(p, M+1):
        dp[j] = max(dp[j], i, dp[j-p]*10 + i)
print(dp[M])