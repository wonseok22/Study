import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
for mid in range(N):
    dp = [0 for _ in range(N+1)]
    dp[1] = 1
    for i in range(mid-1,-1,-1):
