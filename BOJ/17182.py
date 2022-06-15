import sys
input = sys.stdin.readline


N,K = map(int,input().split())
time = [list(map(int,input().split())) for _ in range(N)]
distance = [[float("inf") for _ in range(N)] for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])
print(time)