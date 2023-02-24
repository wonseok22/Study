import sys
input = sys.stdin.readline


N = int(input())
dp = [[[0,10**9] for _ in range(3)] for _ in range(2)]
dp[0] = [[0,0] for _ in range(3)]

for i in range(1,N+1):
    arr = list(map(int,input().split()))
    for j in range(3):
        dp[i%2][j][0] = arr[j] + max(dp[(i+1)%2][j-1][0] if i > 0 else 0, dp[(i+1)%2][j][0], dp[(i+1)%2][j+1][0] if j < 2 else 0)
        dp[i%2][j][1] = arr[j] + min(dp[(i+1)%2][j-1][1] if i > 0 else 10**9, dp[(i+1)%2][j][1], dp[(i+1)%2][j+1][1] if j < 2 else 10**9)
print(max(value[0] for value in dp[N%2]), min(value[1] for value in dp[N%2]))