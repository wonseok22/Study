import sys
input = sys.stdin.readline

N, M = map(int,input().split())
cost = [[float("inf") for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    cost[a-1][b-1] = 1
    cost[b-1][a-1] = 1
for i in range(N):
    cost[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

m = [0,0,float("inf")]
for x,y in list([x,y] for x in range(N) for y in range(N)):
    tmp = [0 for _ in range(N)]
    for i in range(N):
        if i != x or i != y:
            tmp[i] = min(cost[x][i], cost[y][i])
    s = sum(tmp)*2
    if s < m[2]:
        m = [x+1, y+1, s]
print(' '.join(map(str,m)))
