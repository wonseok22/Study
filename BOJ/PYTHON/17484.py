import sys
def dp(direction,cnt):
    if cnt == N:
        return
    if cnt == 0:
        for i in range(M):
            dp[0][i] = arr[0][i]
            for
    else:
        for i in range(M):
            dp[cnt][i] = min(dp[cnt-1])
input = sys.stdin.readline
dir = [-1,0,1]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[601 for _ in range(M)] for _ in range(N)]


