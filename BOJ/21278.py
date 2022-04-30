import sys
input = sys.stdin.readline

N, M = map(int,input().split())
cost = [[float("inf") for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    cost[a-1][b-1] = 1
    cost[b-1][a-1] = 1
for i in range(N): # 자기 자신으로 가는 가중치는 0
    cost[i][i] = 0

for k in range(N): #걍유지
    for i in range(N): #출발지
        for j in range(N): #도착지
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

m = [0,0,float("inf")]
for x,y in list([x,y] for x in range(N) for y in range(N)): # 0,1 부터 n-1,n-1까지 모든 조합을 탐색
    tmp = [0 for _ in range(N)] #거리 합을 위해 사용
    for i in range(N):
        if i != x or i != y:
            tmp[i] = min(cost[x][i], cost[y][i])
    s = sum(tmp)*2 # 왕복이므로 거리는 편도의 두 배를 해줘야 함.
    if s < m[2]:
        m = [x+1, y+1, s]
print(' '.join(map(str,m)))
