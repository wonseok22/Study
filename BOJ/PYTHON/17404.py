import sys
input = sys.stdin.readline

N = int(input())
RGB = [list(map(int,input().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
dp[0] = RGB[0]
answer = float("inf")
for i in range(3):
    for j in range(1, N):
        dp[j][0] = RGB[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = RGB[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = RGB[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for j in range(3):
        if i != j:
            answer = min(answer, dp[N-1][j])
print(answer)