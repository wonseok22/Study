import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
cost = [[float("inf")]*N for _ in range(N)]
for _ in range(M):
    A,B,C = map(int,input().split())
    cost[A-1][B-1] = min(cost[A-1][B-1], C)

for k in range(N):  # 경유지
    for i in range(N): # 출발지
        for j in range(N): #도착지
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(N):
    ans = []
    for j in range(N):
        if i == j or cost[i][j] == float("inf"):
            ans.append(0)
        else:
            ans.append(cost[i][j])
    print(" ".join(map(str,ans)))
