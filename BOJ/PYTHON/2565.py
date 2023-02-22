import sys
input = sys.stdin.readline


N = int(input())
lines = sorted(list(map(int,input().split())) for _ in range(N))
dp = [0 for _ in range(N+1)]
l = len(lines)
dp[0] = 1
for i in range(1, l): # 모든 줄에 대해
    for j in range(i): # 시작점이 낮으면서 도착점은 높다? min값으로 갱신
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[j], dp[i])
    dp[i] +=1
print(l - max(dp))
