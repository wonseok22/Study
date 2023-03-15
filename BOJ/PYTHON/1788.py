import sys
input = sys.stdin.readline

N = int(input())
aN = abs(N)

if aN <= 1:
    print(N)
    print(aN)
    exit()
dp = [0 for _ in range(aN+1)]
dp[1] = 1
for i in range(2, aN+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000000
if N < 0:
    print(-1 if aN % 2 == 0 else 1)
else:
    print(1)
print(dp[aN])